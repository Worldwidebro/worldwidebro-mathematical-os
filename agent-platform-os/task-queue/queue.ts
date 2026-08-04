/**
 * Task Queue — async scheduling with retry logic and state tracking
 * No external queue library (BullMQ); uses async/await + priority ordering
 * Round 3: Feeds completed tasks to 01_loop_feedback_collector.py
 */

import { Task, TaskDispatcher, DispatchDecision } from '../dispatch-engine/dispatcher';

export type TaskState = 'pending' | 'in_progress' | 'completed' | 'failed';

export interface QueuedTask {
  id: string;
  task: Task;
  state: TaskState;
  dispatch_decision?: DispatchDecision;
  retry_count: number;
  max_retries: number;
  created_at: Date;
  started_at?: Date;
  completed_at?: Date;
  error?: string;
}

export class TaskQueue {
  private queue: Map<string, QueuedTask> = new Map();
  private dispatcher: TaskDispatcher;
  private processing: boolean = false;

  constructor(dispatcher: TaskDispatcher) {
    this.dispatcher = dispatcher;
  }

  /**
   * Enqueue a task with automatic priority ordering
   */
  enqueue(task: Task, max_retries: number = 3): QueuedTask {
    const queued: QueuedTask = {
      id: task.id,
      task,
      state: 'pending',
      retry_count: 0,
      max_retries,
      created_at: new Date(),
    };
    this.queue.set(task.id, queued);
    console.log(`[TaskQueue] Enqueued task ${task.id} (priority: ${task.priority}, queue_size: ${this.queue.size})`);
    return queued;
  }

  /**
   * Dequeue next task by priority + deadline + cost
   * Priority order: critical → high → normal → low
   * Tiebreaker: earliest deadline, then lowest cost
   */
  dequeue(): QueuedTask | null {
    const pending = Array.from(this.queue.values()).filter((q) => q.state === 'pending');
    if (pending.length === 0) return null;

    pending.sort((a, b) => {
      const priority_order = { critical: 0, high: 1, normal: 2, low: 3 };
      const p_cmp = priority_order[a.task.priority] - priority_order[b.task.priority];
      if (p_cmp !== 0) return p_cmp;

      // Deadline: earlier first (or no deadline = lower priority)
      const a_deadline = a.task.deadline?.getTime() ?? Infinity;
      const b_deadline = b.task.deadline?.getTime() ?? Infinity;
      const d_cmp = a_deadline - b_deadline;
      if (d_cmp !== 0) return d_cmp;

      // Cost: lower cost first
      return a.task.estimated_cost_hours - b.task.estimated_cost_hours;
    });

    const next = pending[0];
    next.state = 'in_progress';
    next.started_at = new Date();

    // Dispatch to agent
    const decision = this.dispatcher.dispatch(next.task);
    if (decision) {
      next.dispatch_decision = decision;
    }

    console.log(
      `[TaskQueue] Dequeued task ${next.id} → ${decision?.agent_name || 'NO_AGENT'} (pending_count: ${pending.length - 1})`
    );
    return next;
  }

  /**
   * Mark task as completed
   */
  mark_completed(task_id: string): QueuedTask | null {
    const queued = this.queue.get(task_id);
    if (!queued) return null;

    queued.state = 'completed';
    queued.completed_at = new Date();
    queued.retry_count = 0; // reset on success
    console.log(
      `[TaskQueue] Task ${task_id} completed in ${queued.completed_at.getTime() - (queued.started_at?.getTime() ?? 0)}ms`
    );
    return queued;
  }

  /**
   * Handle task failure with exponential backoff retry
   * Retry immediately (no backoff for now; upgrade if queue congestion matters)
   */
  mark_failed(task_id: string, error: string): QueuedTask | null {
    const queued = this.queue.get(task_id);
    if (!queued) return null;

    queued.retry_count++;
    queued.error = error;
    queued.state = queued.retry_count >= queued.max_retries ? 'failed' : 'pending';

    if (queued.state === 'failed') {
      console.error(`[TaskQueue] Task ${task_id} failed after ${queued.retry_count} retries: ${error}`);
    } else {
      console.warn(
        `[TaskQueue] Task ${task_id} failed (attempt ${queued.retry_count}/${queued.max_retries}), retrying: ${error}`
      );
      // Reset dispatch for retry
      queued.dispatch_decision = undefined;
      queued.started_at = undefined;
    }

    return queued;
  }

  /**
   * Get task state by ID
   */
  get_task(task_id: string): QueuedTask | undefined {
    return this.queue.get(task_id);
  }

  /**
   * Get all tasks in a specific state
   */
  get_tasks_by_state(state: TaskState): QueuedTask[] {
    return Array.from(this.queue.values()).filter((q) => q.state === state);
  }

  /**
   * Get queue statistics
   */
  stats() {
    const all = Array.from(this.queue.values());
    return {
      total: all.length,
      pending: all.filter((q) => q.state === 'pending').length,
      in_progress: all.filter((q) => q.state === 'in_progress').length,
      completed: all.filter((q) => q.state === 'completed').length,
      failed: all.filter((q) => q.state === 'failed').length,
    };
  }

  /**
   * Retry all failed tasks (manual override)
   */
  retry_failed(): number {
    const failed = this.get_tasks_by_state('failed');
    for (const queued of failed) {
      queued.state = 'pending';
      queued.retry_count = 0;
      queued.error = undefined;
      queued.started_at = undefined;
    }
    console.log(`[TaskQueue] Retried ${failed.length} failed tasks`);
    return failed.length;
  }
}
