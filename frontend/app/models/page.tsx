export default function ModelsPage() {
  return (
    <div className="p-8">
      <div className="card p-8">
        <h1 className="text-3xl font-bold text-offWhite">Model and inference configuration</h1>
        <div className="mt-6 space-y-4">
          {[
            ['yolov8n.pt', 'object_detection', 'ready'],
            ['yolov8n-pose', 'pose_estimation', 'degraded'],
            ['ppe-suite', 'safety_equipment', 'disabled'],
          ].map(([name, type, status]) => (
            <div key={name} className="rounded-xl border border-slate-700 bg-slate-900 p-4">
              <div className="flex items-center justify-between"><div className="text-lg font-semibold text-offWhite">{name}</div><span className={status === 'ready' ? 'text-emerald' : status === 'degraded' ? 'text-amber' : 'text-slate-400'}>{status}</span></div>
              <div className="mt-2 text-sm text-slate-300">{type}</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
