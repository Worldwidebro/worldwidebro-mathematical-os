#!/usr/bin/env python3
"""
Venture Operations Task Watcher
Polls ClickUp every 5 minutes for new/updated tasks in 'Venture Operations—Autonomous' list
Maps tasks to skills and invokes executor

---
created: 2026-06-01T00:00:00Z
last_edited: 2026-06-01T00:00:00Z
edited_by: Claude Haiku 4.5
version: 1.0
---
"""

import os
import time
import json
import logging
import requests
from datetime import datetime
from typing import Dict, List, Optional
from dotenv import load_dotenv

load_dotenv()

# Configuration
CLICKUP_API_KEY = os.getenv("CLICKUP_API_KEY")
CLICKUP_LIST_ID = os.getenv("CLICKUP_LIST_VENTURE_OPS", "901003877")  # Venture Ops list
POLL_INTERVAL = 300  # 5 minutes
CLICKUP_API_URL = "https://api.clickup.com/api/v2"

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

# Task type to skill mapping
TASK_TYPE_TO_SKILL = {
    "DEPLOY": "deployment-workflow",
    "MIGRATE": "supabase-migration",
    "INTEGRATE": "api-integration",
    "TEST": "test-runner",
    "SYNC": "kg-sync",
    "DOCUMENT": "doc-generator",
    "MONITOR": "metrics-fetch",
    "BACKUP": "backup-trigger",
    "ONBOARD": "venture-setup",
    "REPORT": "report-generator",
    "SCALE": "provision-resources",
    "INCIDENT": "incident-routing",
}


class TaskWatcher:
    def __init__(self, api_key: str, list_id: str):
        self.api_key = api_key
        self.list_id = list_id
        self.headers = {
            "Authorization": api_key,
            "Content-Type": "application/json",
        }
        self.last_sync = None
        self.processed_tasks = set()

    def get_pending_tasks(self) -> List[Dict]:
        """Fetch all pending/in_progress tasks from ClickUp"""
        try:
            # Get tasks with status = pending or in_progress
            url = f"{CLICKUP_API_URL}/list/{self.list_id}/task"
            params = {
                "statuses": ["pending", "in_progress"],
                "archived": False,
                "include_subtasks": False,
            }

            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()

            data = response.json()
            tasks = data.get("tasks", [])

            logger.info(f"Fetched {len(tasks)} pending tasks from ClickUp")
            return tasks

        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch tasks from ClickUp: {e}")
            return []

    def parse_task(self, task: Dict) -> Optional[Dict]:
        """Parse ClickUp task into executable format"""
        try:
            task_id = task.get("id")
            name = task.get("name", "")
            status = task.get("status", {}).get("status", "unknown")

            # Extract custom fields
            custom_fields = {f["id"]: f.get("value") for f in task.get("custom_fields", [])}

            # Determine task type from name or custom field
            task_type = None
            for t_type in TASK_TYPE_TO_SKILL.keys():
                if name.startswith(t_type):
                    task_type = t_type
                    break

            if not task_type:
                logger.warning(f"Task {task_id} has unknown type, skipping")
                return None

            venture_id = custom_fields.get("venture_id", "")
            if not venture_id:
                logger.warning(f"Task {task_id} missing venture_id, skipping")
                return None

            return {
                "task_id": task_id,
                "task_type": task_type,
                "venture_id": venture_id,
                "status": status,
                "name": name,
                "custom_fields": custom_fields,
                "skill": TASK_TYPE_TO_SKILL[task_type],
            }

        except Exception as e:
            logger.error(f"Failed to parse task {task.get('id')}: {e}")
            return None

    def update_task_status(
        self, task_id: str, status: str, comment: str = ""
    ) -> bool:
        """Update task status in ClickUp"""
        try:
            url = f"{CLICKUP_API_URL}/task/{task_id}"
            payload = {"status": status}

            if comment:
                # Add comment to task
                comment_url = f"{CLICKUP_API_URL}/task/{task_id}/comment"
                comment_payload = {"comment_text": comment}
                requests.post(
                    comment_url, headers=self.headers, json=comment_payload
                )

            response = requests.put(url, headers=self.headers, json=payload)
            response.raise_for_status()
            logger.info(f"Updated task {task_id} status to {status}")
            return True

        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to update task {task_id}: {e}")
            return False

    def invoke_executor(self, task: Dict) -> bool:
        """Invoke task executor with task context"""
        try:
            from task_executor import TaskExecutor

            executor = TaskExecutor()
            result = executor.execute(task)

            # Update ClickUp with result
            if result["success"]:
                self.update_task_status(
                    task["task_id"],
                    "success",
                    f"✅ Completed: {result.get('message', 'Task executed')}",
                )
            else:
                self.update_task_status(
                    task["task_id"],
                    "failed",
                    f"❌ Failed: {result.get('error', 'Unknown error')}",
                )

            return result["success"]

        except ImportError:
            logger.error("TaskExecutor not found, create task_executor.py first")
            return False
        except Exception as e:
            logger.error(f"Failed to invoke executor for task {task['task_id']}: {e}")
            self.update_task_status(task["task_id"], "failed", f"Error: {str(e)}")
            return False

    def poll(self):
        """Main polling loop"""
        logger.info("Starting task watcher...")

        while True:
            try:
                logger.info(f"Polling ClickUp at {datetime.now().isoformat()}")

                # Fetch pending tasks
                tasks = self.get_pending_tasks()

                # Process each task
                for task in tasks:
                    task_id = task.get("id")

                    # Skip if already processed in this cycle
                    if task_id in self.processed_tasks:
                        continue

                    # Parse and execute
                    parsed_task = self.parse_task(task)
                    if parsed_task:
                        logger.info(
                            f"Processing task {task_id}: {parsed_task['task_type']} for {parsed_task['venture_id']}"
                        )
                        self.update_task_status(task_id, "in_progress", "🔄 Started")
                        self.invoke_executor(parsed_task)
                        self.processed_tasks.add(task_id)

                # Reset processed tasks after full cycle
                if len(self.processed_tasks) > 100:
                    self.processed_tasks.clear()

                # Wait for next poll
                logger.info(f"Next poll in {POLL_INTERVAL} seconds...")
                time.sleep(POLL_INTERVAL)

            except KeyboardInterrupt:
                logger.info("Task watcher stopped by user")
                break
            except Exception as e:
                logger.error(f"Unexpected error in poll loop: {e}")
                time.sleep(POLL_INTERVAL)


def main():
    if not CLICKUP_API_KEY:
        logger.error("CLICKUP_API_KEY not found in .env")
        logger.info("Set CLICKUP_API_KEY in .env file to continue")
        return

    watcher = TaskWatcher(CLICKUP_API_KEY, CLICKUP_LIST_ID)
    watcher.poll()


if __name__ == "__main__":
    main()
