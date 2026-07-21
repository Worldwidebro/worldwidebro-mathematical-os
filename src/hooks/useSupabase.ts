import { useEffect, useState } from 'react';

interface Task {
  id: string;
  title: string;
  status: 'pending' | 'in_progress' | 'completed' | 'failed';
  venture_id: string;
  agent_id: string;
  created_at: string;
}

interface AuditLog {
  id: string;
  action: string;
  actor: string;
  timestamp: string;
  resource: string;
}

interface Decision {
  id: string;
  title: string;
  status: 'open' | 'decided' | 'archived';
  confidence: number;
  created_at: string;
  agent_id: string;
}

export function useSupabaseTasks() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetch() {
      try {
        const res = await fetch('/api/supabase/tasks');
        const data = await res.json();
        setTasks(data.tasks || []);
      } catch (err) {
        console.error('Tasks fetch failed:', err);
      } finally {
        setLoading(false);
      }
    }
    fetch();
  }, []);

  return { tasks, loading };
}

export function useSupabaseAuditLog() {
  const [logs, setLogs] = useState<AuditLog[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetch() {
      try {
        const res = await fetch('/api/supabase/audit?limit=100');
        const data = await res.json();
        setLogs(data.logs || []);
      } catch (err) {
        console.error('Audit log fetch failed:', err);
      } finally {
        setLoading(false);
      }
    }
    fetch();
  }, []);

  return { logs, loading };
}

export function useSupabaseDecisions() {
  const [decisions, setDecisions] = useState<Decision[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetch() {
      try {
        const res = await fetch('/api/supabase/decisions');
        const data = await res.json();
        setDecisions(data.decisions || []);
      } catch (err) {
        console.error('Decisions fetch failed:', err);
      } finally {
        setLoading(false);
      }
    }
    fetch();
  }, []);

  return { decisions, loading };
}
