export default function ZonesPage() {
  return (
    <div className="p-8">
      <div className="card p-8">
        <h1 className="text-3xl font-bold text-offWhite">Zone editor</h1>
        <div className="mt-6 grid gap-4 md:grid-cols-3">
          <ZoneCard type="Restricted" color="text-red" />
          <ZoneCard type="Danger" color="text-amber" />
          <ZoneCard type="Safe" color="text-emerald" />
        </div>
      </div>
    </div>
  );
}

function ZoneCard({ type, color }: { type: string; color: string }) {
  return (
    <div className="rounded-2xl border border-slate-700 bg-slate-900 p-4">
      <div className={`text-lg font-semibold ${color}`}>{type}</div>
      <div className="mt-4 h-28 rounded-xl border border-dashed border-slate-600 bg-slate-950" />
    </div>
  );
}
