import type { Config } from 'tailwindcss';

const config: Config = {
  content: ['./app/**/*.{js,ts,jsx,tsx,mdx}', './components/**/*.{js,ts,jsx,tsx,mdx}'],
  theme: {
    extend: {
      colors: {
        nearBlack: '#070b14',
        charcoal: '#101827',
        offWhite: '#f1f5f9',
        cyan: '#22d3ee',
        lime: '#a3e635',
        amber: '#fbbf24',
        orange: '#f97316',
        red: '#ef4444',
        magenta: '#d946ef',
        violet: '#8b5cf6',
      },
      boxShadow: {
        glow: '0 0 0 1px rgba(34, 211, 238, 0.25), 0 30px 60px rgba(15, 23, 42, 0.5)',
      },
    },
  },
  plugins: [],
};

export default config;
