'use client';

import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, Cell } from 'recharts';

interface MaintenanceData {
  status: string;
  count: number;
}

interface MaintenancePipelineProps {
  data: MaintenanceData[];
}

const statusColors: Record<string, string> = {
  open: '#F59E0B',
  assigned: '#3B82F6',
  in_progress: '#8B5CF6',
  completed: '#10B981'
};

const statusLabels: Record<string, string> = {
  open: 'Open',
  assigned: 'Assigned',
  in_progress: 'In Progress',
  completed: 'Completed'
};

export function MaintenancePipeline({ data }: MaintenancePipelineProps) {
  return (
    <div className="bg-gray-900 border border-gray-800 rounded-xl p-6">
      <h3 className="text-sm font-bold text-white mb-4">Maintenance Pipeline</h3>
      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={data}>
          <CartesianGrid strokeDasharray="3 3" stroke="#374151" />
          <XAxis
            dataKey="status"
            stroke="#9CA3AF"
            style={{ fontSize: '12px' }}
            tickFormatter={(val) => statusLabels[val] || val}
          />
          <YAxis
            stroke="#9CA3AF"
            style={{ fontSize: '12px' }}
          />
          <Tooltip
            contentStyle={{
              backgroundColor: '#111827',
              border: '1px solid #374151',
              borderRadius: '8px',
              color: '#E5E7EB'
            }}
            labelFormatter={(val) => statusLabels[val as string] || val}
            labelStyle={{ color: '#E5E7EB' }}
          />
          <Legend wrapperStyle={{ paddingTop: '20px' }} />
          <Bar dataKey="count" name="Tickets" radius={[4, 4, 0, 0]}>
            {data.map((entry, index) => (
              <Cell key={`cell-${index}`} fill={statusColors[entry.status] || '#3B82F6'} />
            ))}
          </Bar>
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
