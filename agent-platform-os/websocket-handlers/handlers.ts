/**
 * WebSocket Handlers — real-time status updates for agent + task events
 * Events: agent_online, agent_offline, task_dispatched, task_completed, task_failed
 * Consumed by vex-hero-site dashboard in Round 3
 */

import { EventEmitter } from 'events';
import { AgentRegistry } from '../agent-registry/registry';
import { TaskQueue } from '../task-queue/queue';
import { TaskDispatcher } from '../dispatch-engine/dispatcher';

export interface WebSocketEvent {
  event: string;
  agent_id?: string;
  task_id?: string;
  timestamp: Date;
  status?: string;
  payload?: Record<string, any>;
}

export class WebSocketEventBus extends EventEmitter {
  private registry: AgentRegistry;
  private queue: TaskQueue;
  private dispatcher: TaskDispatcher;
  private subscribers: Set<(event: WebSocketEvent) => void> = new Set();

  constructor(registry: AgentRegistry, queue: TaskQueue, dispatcher: TaskDispatcher) {
    super();
    this.registry = registry;
    this.queue = queue;
    this.dispatcher = dispatcher;
  }

  /**
   * Subscribe to all events
   */
  subscribe(callback: (event: WebSocketEvent) => void): () => void {
    this.subscribers.add(callback);
    return () => this.subscribers.delete(callback);
  }

  /**
   * Broadcast event to all subscribers
   */
  private broadcast(event: WebSocketEvent): void {
    for (const cb of this.subscribers) {
      try {
        cb(event);
      } catch (err) {
        console.error('[WebSocketEventBus] Subscriber error:', err);
      }
    }
  }

  /**
   * Agent came online
   */
  emit_agent_online(agent_id: string, agent_name: string): void {
    const event: WebSocketEvent = {
      event: 'agent_online',
      agent_id,
      timestamp: new Date(),
      status: 'online',
      payload: { agent_name },
    };
    this.broadcast(event);
    console.log(`[WebSocketEventBus] ${agent_name} came online`);
  }

  /**
   * Agent went offline
   */
  emit_agent_offline(agent_id: string, agent_name: string): void {
    const event: WebSocketEvent = {
      event: 'agent_offline',
      agent_id,
      timestamp: new Date(),
      status: 'offline',
      payload: { agent_name },
    };
    this.broadcast(event);
    console.log(`[WebSocketEventBus] ${agent_name} went offline`);
  }

  /**
   * Task dispatched to agent
   */
  emit_task_dispatched(task_id: string, agent_id: string, agent_name: string, dispatch_score: number): void {
    const event: WebSocketEvent = {
      event: 'task_dispatched',
      task_id,
      agent_id,
      timestamp: new Date(),
      status: 'dispatched',
      payload: {
        agent_name,
        dispatch_score,
      },
    };
    this.broadcast(event);
    console.log(`[WebSocketEventBus] Task ${task_id} dispatched to ${agent_name} (score: ${dispatch_score.toFixed(2)})`);
  }

  /**
   * Task completed
   */
  emit_task_completed(task_id: string, agent_id: string, duration_ms: number): void {
    const event: WebSocketEvent = {
      event: 'task_completed',
      task_id,
      agent_id,
      timestamp: new Date(),
      status: 'completed',
      payload: {
        duration_ms,
      },
    };
    this.broadcast(event);
    console.log(`[WebSocketEventBus] Task ${task_id} completed in ${duration_ms}ms`);
  }

  /**
   * Task failed
   */
  emit_task_failed(task_id: string, agent_id: string, error: string, retry_count: number, max_retries: number): void {
    const event: WebSocketEvent = {
      event: 'task_failed',
      task_id,
      agent_id,
      timestamp: new Date(),
      status: retry_count < max_retries ? 'retrying' : 'failed',
      payload: {
        error,
        retry_count,
        max_retries,
      },
    };
    this.broadcast(event);
    const status = retry_count < max_retries ? `retrying (${retry_count}/${max_retries})` : 'failed';
    console.log(`[WebSocketEventBus] Task ${task_id} ${status}: ${error}`);
  }

  /**
   * Agent availability changed
   */
  emit_agent_availability_changed(agent_id: string, agent_name: string, available: boolean): void {
    const event: WebSocketEvent = {
      event: 'agent_availability_changed',
      agent_id,
      timestamp: new Date(),
      status: available ? 'available' : 'unavailable',
      payload: {
        agent_name,
        available,
      },
    };
    this.broadcast(event);
    console.log(`[WebSocketEventBus] ${agent_name} availability: ${available ? 'available' : 'unavailable'}`);
  }

  /**
   * Queue statistics update (periodic broadcast)
   */
  emit_queue_stats_update(): void {
    const stats = this.queue.stats();
    const event: WebSocketEvent = {
      event: 'queue_stats_update',
      timestamp: new Date(),
      payload: stats,
    };
    this.broadcast(event);
  }

  /**
   * Get subscriber count (for monitoring)
   */
  get_subscriber_count(): number {
    return this.subscribers.size;
  }
}

/**
 * Setup a periodic queue stats broadcast (every 5 seconds)
 */
export function setup_stats_broadcaster(bus: WebSocketEventBus, interval_ms: number = 5000): () => void {
  const timer = setInterval(() => {
    bus.emit_queue_stats_update();
  }, interval_ms);

  return () => clearInterval(timer);
}
