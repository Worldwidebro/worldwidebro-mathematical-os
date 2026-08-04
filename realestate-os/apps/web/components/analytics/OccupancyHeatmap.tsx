'use client';

interface OccupancyUnit {
  propertyId: string;
  propertyAddress: string;
  propertyCity: string;
  unitId: string;
  unitNumber: string;
  occupied: boolean;
}

interface OccupancyHeatmapProps {
  data: OccupancyUnit[];
}

export function OccupancyHeatmap({ data }: OccupancyHeatmapProps) {
  // Group by property
  const byProperty = data.reduce((acc, unit) => {
    const key = unit.propertyId;
    if (!acc[key]) {
      acc[key] = {
        address: unit.propertyAddress,
        city: unit.propertyCity,
        units: []
      };
    }
    acc[key].units.push(unit);
    return acc;
  }, {} as Record<string, { address: string; city: string; units: OccupancyUnit[] }>);

  return (
    <div className="bg-gray-900 border border-gray-800 rounded-xl p-6">
      <h3 className="text-sm font-bold text-white mb-4">Property Occupancy Heatmap</h3>
      <div className="space-y-6 max-h-96 overflow-y-auto">
        {Object.entries(byProperty).length === 0 ? (
          <p className="text-xs text-gray-400 text-center py-8">No properties</p>
        ) : (
          Object.entries(byProperty).map(([propId, prop]) => (
            <div key={propId} className="space-y-2">
              <div>
                <h4 className="text-xs font-semibold text-gray-300">{prop.address}</h4>
                <p className="text-[10px] text-gray-500">{prop.city}</p>
              </div>
              <div className="grid grid-cols-4 gap-2">
                {prop.units.map(unit => (
                  <div
                    key={unit.unitId}
                    className={`p-3 rounded-lg text-center text-xs font-semibold transition-all ${
                      unit.occupied
                        ? 'bg-emerald-950 text-emerald-400 border border-emerald-800'
                        : 'bg-red-950 text-red-400 border border-red-800'
                    }`}
                  >
                    <div className="text-[10px] opacity-75">Unit</div>
                    <div>{unit.unitNumber}</div>
                  </div>
                ))}
              </div>
            </div>
          ))
        )}
      </div>
      <div className="mt-4 flex gap-4 text-xs">
        <div className="flex items-center gap-2">
          <div className="h-3 w-3 rounded bg-emerald-950 border border-emerald-800" />
          <span className="text-gray-400">Occupied</span>
        </div>
        <div className="flex items-center gap-2">
          <div className="h-3 w-3 rounded bg-red-950 border border-red-800" />
          <span className="text-gray-400">Vacant</span>
        </div>
      </div>
    </div>
  );
}
