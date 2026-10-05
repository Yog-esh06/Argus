export default function SystemPage() {
  const metrics = [
    ['FPS', '24.1'],
    ['Inference latency', '32.4ms'],
    ['Queue depth', '2'],
    ['CPU usage', '35.2%'],
    ['Memory usage', '51.8%'],
  ];

  return (
    <div className="p-8">
      <div className="card p-8">
        <h1 className="text-3xl font-bold text-offWhite">System performance</h1>
        <div className="mt-6 grid gap-4 md:grid-cols-2 xl:grid-cols-3">
          {metrics.map(([label, value]) => (
            <div key={label} className="rounded-2xl border border-slate-700 bg-slate-900 p-4">
              <div className="text-xs uppercase tracking-[0.2em] text-slate-400">{label}</div>
              <div className="metric mt-3 text-2xl">{value}</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
