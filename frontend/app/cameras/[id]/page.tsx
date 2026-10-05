export default function CameraDetailPage({ params }: { params: { id: string } }) {
  return (
    <div className="p-8">
      <div className="card p-8">
        <h1 className="text-3xl font-bold text-offWhite">Camera {params.id}</h1>
        <div className="mt-5 grid gap-4 md:grid-cols-3">
          <Stat label="Avg FPS" value="24.8" />
          <Stat label="Dropped frames" value="3" />
          <Stat label="Tracks" value="14" />
        </div>
      </div>
    </div>
  );
}

function Stat({ label, value }: { label: string; value: string }) { return <div className="rounded-2xl border border-slate-700 bg-slate-900 p-4"><div className="text-xs uppercase tracking-[0.2em] text-slate-400">{label}</div><div className="metric mt-3 text-2xl">{value}</div></div>; }
