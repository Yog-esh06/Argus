export default function CamerasPage() {
  const cameras = [
    ['cam-001', 'Dock 12', 'Warehouse North', 'online'],
    ['cam-002', 'Loading Bay', 'Inbound Logistics', 'online'],
    ['cam-003', 'Forklift Lane', 'Loading dock', 'warning'],
  ];

  return (
    <div className="p-8">
      <div className="card p-6">
        <h1 className="text-3xl font-bold text-offWhite">Camera management</h1>
        <div className="mt-6 grid gap-4 md:grid-cols-3">
          {cameras.map(([id, name, location, status]) => (
            <div key={id} className="rounded-2xl border border-slate-700 bg-slate-900 p-5">
              <div className="flex items-center justify-between">
                <div className="text-lg font-semibold text-offWhite">{name}</div>
                <span className={status === 'warning' ? 'text-amber' : 'text-emerald'}>{status}</span>
              </div>
              <div className="mt-3 text-sm text-slate-400">{location}</div>
              <div className="mt-5 text-xs uppercase tracking-[0.2em] text-violet">{id}</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
