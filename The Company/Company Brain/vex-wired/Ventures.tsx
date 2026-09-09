import React from 'react';
import { useSearchParams } from 'react-router-dom';
import { SECTORS } from '../data/sectors';

export default function Ventures() {
  const [searchParams] = useSearchParams();
  const opcoId = searchParams.get('opco') || 'OPCO-Technology';

  // Real ventures from Supabase (wired via /api/dashboard-metrics)
  const [ventures, setVentures] = React.useState<any[]>([]);
  const [loading, setLoading] = React.useState(true);

  React.useEffect(() => {
    const fetchVentures = async () => {
      try {
        const response = await fetch(`/api/ventures?opco=${opcoId}`);
        if (response.ok) {
          const data = await response.json();
          setVentures(data);
        }
      } catch (error) {
        console.error('Failed to fetch ventures:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchVentures();
  }, [opcoId]);

  const opcoName = Object.values(SECTORS).find(s => s.opco === opcoId)?.name || opcoId;

  return (
    <div className="p-6 space-y-6">
      <div>
        <div className="text-sm text-gray-500 mb-2">
          <a href="/holdings/organization" className="hover:text-blue-400">← Back to Organization</a>
        </div>
        <h1 className="text-3xl font-bold mb-1">Ventures</h1>
        <p className="text-gray-400">{ventures.length} ventures in {opcoName}</p>
      </div>

      {loading ? (
        <div className="border border-white/10 bg-gray-900 rounded-lg p-8 text-center">
          <p className="text-gray-400">Loading ventures...</p>
        </div>
      ) : ventures.length === 0 ? (
        <div className="border border-white/10 bg-gray-900 rounded-lg p-8 text-center">
          <p className="text-gray-400">No ventures in this OPCO</p>
        </div>
      ) : (
        <div className="space-y-3">
          {ventures.map((v: any) => (
            <div key={v.id} className="border border-white/10 bg-gray-900 rounded-lg p-4 hover:border-white/20 cursor-pointer transition-colors">
              <div className="flex justify-between items-start mb-2">
                <div>
                  <div className="text-xs text-cyan-400 font-mono">{v.id}</div>
                  <div className="text-lg font-bold mt-1">{v.name}</div>
                </div>
                <div className="text-right">
                  <div className={`text-xs px-2 py-1 rounded font-bold ${v.stage === 'Revenue' ? 'bg-green-500/20 text-green-400' : v.stage === 'MVP' ? 'bg-blue-500/20 text-blue-400' : 'bg-gray-700 text-gray-300'}`}>
                    {v.stage}
                  </div>
                  {v.mrr && <div className="text-sm text-green-400 mt-2 font-bold">{v.mrr}/mo</div>}
                </div>
              </div>
              <div className="text-sm text-gray-400">
                {Object.values(SECTORS).find(s => s.id === v.sector)?.name} • {v.status}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
