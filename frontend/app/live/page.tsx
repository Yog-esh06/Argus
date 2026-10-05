export default function LivePage() {
  return (
    <div className="p-8">
      <div className="card p-6">
        <div className="mb-4 flex items-center justify-between">
          <h1 className="text-3xl font-bold text-offWhite">Live monitoring</h1>
          <span className="status-pill bg-cyan/10 text-cyan">STREAMING</span>
        </div>
        <div className="grid gap-4 lg:grid-cols-[1.5fr_0.5fr]">
          <div className="rounded-2xl border border-slate-700 bg-slate-950 p-4">
            <div className="h-[420px] rounded-2xl bg-[radial-gradient(circle_at_center,_rgba(34,211,238,0.2),_rgba(15,23,42,0.8)_40%)] p-4">
              <div className="flex h-full items-center justify-center text-lg text-slate-300">Video stream preview</div>
            </div>
          </div>
          <div className="space-y-4">
            {['Detection', 'Tracking', 'Trajectories', 'Zones', 'Pose', 'Alerts'].map((toggle) => (
              <div key={toggle} className="rounded-xl border border-slate-700 bg-slate-900 p-3 text-sm text-slate-200">{toggle}</div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
