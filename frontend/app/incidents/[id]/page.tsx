export default function IncidentDetailPage({ params }: { params: { id: string } }) {
  return (
    <div className="p-8">
      <div className="card p-8">
        <h1 className="text-3xl font-bold text-offWhite">Incident {params.id}</h1>
        <div className="mt-6 grid gap-4 md:grid-cols-2">
          <Info label="Event type" value="ZONE_BREACH" />
          <Info label="Severity" value="HIGH" />
          <Info label="Camera" value="cam-001" />
          <Info label="Confidence" value="0.88" />
        </div>
      </div>
    </div>
  );
}

function Info({ label, value }: { label: string; value: string }) { return <div className="rounded-2xl border border-slate-700 bg-slate-900 p-4"><div className="text-xs uppercase tracking-[0.2em] text-slate-400">{label}</div><div className="mt-3 text-xl font-semibold text-offWhite">{value}</div></div>; }
