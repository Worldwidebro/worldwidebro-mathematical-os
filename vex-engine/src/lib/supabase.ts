import { createClient } from '@supabase/supabase-js';

const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL || '';
const supabaseAnonKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY || '';

export const supabase = createClient(supabaseUrl, supabaseAnonKey);

export async function getAgents() {
  try {
    const { data } = await supabase.from('aoc_agents').select('*').limit(100);
    return data || [];
  } catch (e) {
    console.error('Error fetching agents:', e);
    return [];
  }
}

export async function getAgentTasks() {
  try {
    const { data } = await supabase.from('agent_tasks').select('*').limit(100);
    return data || [];
  } catch (e) {
    console.error('Error fetching tasks:', e);
    return [];
  }
}

export async function getAgentDecisions() {
  try {
    const { data } = await supabase.from('agent_decisions').select('*').limit(50);
    return data || [];
  } catch (e) {
    console.error('Error fetching decisions:', e);
    return [];
  }
}

export async function getSkillExecutions() {
  try {
    const { data } = await supabase.from('skill_executions').select('*').limit(100);
    return data || [];
  } catch (e) {
    console.error('Error fetching skill executions:', e);
    return [];
  }
}
