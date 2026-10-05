export default function IncidentsPage() {
  const incidents = [
    ['inc-001', 'ZONE_BREACH', 'HIGH', 'Person entered restricted machine zone'],
    ['inc-002', 'PROXIMITY_WARNING', 'MEDIUM', 'Forklift and pedestrian proximity threshold exceeded'],
    ['inc-003', 'UNUSUAL_MOVEMENT', 'LOW', 'Trajectory deviates from expected pattern'],
  ];

  return (
    <div className="p-8">
      <div className="card p-6">
        <h1 className="text-3xl font-bold text-offWhite">Incident list</h1>
        <div className="mt-6 space-y-4">
          {incidents.map(([id, type, severity, summary]) => (
            <div key={id} className="rounded-xl border border-slate-700 bg-slate-900 p-4">
              <div className="flex items-center justify-between">
                <div className="font-semibold text-offWhite">{type}</div>
                <span className={severity === 'HIGH' ? 'text-red' : severity === 'MEDIUM' ? 'text-amber' : 'text-emerald'}>{severity}</span>
              </div>
              <div className="mt-2 text-sm text-slate-300">{summary}</div>
              <div className="mt-3 text-xs uppercase tracking-[0.2em] text-slate-500">{id}</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
