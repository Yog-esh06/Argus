import Link from 'next/link';

const routes = [
  { href: '/overview', label: 'Overview' },
  { href: '/live', label: 'Live' },
  { href: '/cameras', label: 'Cameras' },
  { href: '/incidents', label: 'Incidents' },
  { href: '/zones', label: 'Zones' },
  { href: '/analytics', label: 'Analytics' },
  { href: '/models', label: 'Models' },
  { href: '/system', label: 'System' },
];

export default function HomePage() {
  return (
    <main className="min-h-screen px-6 py-10">
      <div className="mx-auto max-w-6xl">
        <header className="mb-8 flex items-center justify-between border-b border-slate-700/80 pb-5">
          <div>
            <p className="text-xs uppercase tracking-[0.3em] text-cyan">Argus</p>
            <h1 className="mt-2 text-4xl font-black text-offWhite">Industrial safety command center</h1>
          </div>
          <div className="status-pill bg-emerald-500/10 text-emerald-300">
            <span className="h-2 w-2 rounded-full bg-emerald-400" /> LIVE
          </div>
        </header>

        <section className="mb-8 grid gap-6 md:grid-cols-3">
          <div className="card p-6">
            <p className="text-sm uppercase tracking-[0.2em] text-slate-400">Cameras online</p>
            <div className="metric mt-4 text-4xl">12</div>
          </div>
          <div className="card p-6">
            <p className="text-sm uppercase tracking-[0.2em] text-slate-400">Active incidents</p>
            <div className="metric mt-4 text-4xl text-amber">03</div>
          </div>
          <div className="card p-6">
            <p className="text-sm uppercase tracking-[0.2em] text-slate-400">Current FPS</p>
            <div className="metric mt-4 text-4xl text-cyan">24.8</div>
          </div>
        </section>

        <section className="grid gap-6 lg:grid-cols-[1.3fr_0.7fr]">
          <div className="card p-6">
            <div className="mb-4 flex items-center justify-between">
              <h2 className="text-xl font-bold text-offWhite">Control room views</h2>
              <span className="text-xs uppercase tracking-[0.2em] text-violet">Operations</span>
            </div>
            <div className="grid gap-4 sm:grid-cols-2">
              {routes.map((route) => (
                <Link key={route.href} href={route.href} className="rounded-2xl border border-slate-700 bg-slate-900/80 p-4 hover:border-cyan/70 transition-colors">
                  <div className="text-lg font-semibold text-offWhite">{route.label}</div>
                  <div className="mt-2 text-sm text-slate-400">View operational status and monitoring data</div>
                </Link>
              ))}
            </div>
          </div>

          <div className="card p-6">
            <h2 className="text-xl font-bold text-offWhite">Event stream</h2>
            <div className="mt-6 space-y-4">
              {[
                ['ZONE_BREACH', 'HIGH', 'Restricted area access detected'],
                ['PROXIMITY_WARNING', 'MEDIUM', 'Forklift and pedestrian proximity threshold exceeded'],
                ['UNUSUAL_MOVEMENT', 'LOW', 'Trajectory deviates from the established pattern'],
              ].map(([event, level, description]) => (
                <div key={event} className="rounded-xl border border-slate-700 bg-slate-950/60 p-3">
                  <div className="flex items-center justify-between">
                    <span className="font-semibold text-offWhite">{event}</span>
                    <span className={level === 'HIGH' ? 'text-red' : level === 'MEDIUM' ? 'text-amber' : 'text-emerald'}>{level}</span>
                  </div>
                  <p className="mt-2 text-sm text-slate-300">{description}</p>
                </div>
              ))}
            </div>
          </div>
        </section>
      </div>
    </main>
  );
}
