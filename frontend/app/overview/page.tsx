export default function OverviewPage() {
  return (
    <div className="p-8">
      <div className="card p-8">
        <h1 className="text-3xl font-bold text-offWhite">Operational Overview</h1>
        <div className="mt-6 grid gap-4 md:grid-cols-4">
          <Metric label="Cameras online" value="12" />
          <Metric label="Critical alerts" value="1" />
          <Metric label="Monitored people" value="148" />
          <Metric label="System health" value="97%" />
        </div>
      </div>
    </div>
  );
}

function Metric({ label, value }: { label: string; value: string }) {
  return (
    <div className="rounded-2xl border border-slate-700 bg-slate-900 p-4">
      <div className="text-xs uppercase tracking-[0.2em] text-slate-400">{label}</div>
      <div className="metric mt-3 text-3xl">{value}</div>
    </div>
  );
}
