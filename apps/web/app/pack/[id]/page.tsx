import Link from "next/link";
import { Button } from "@/components/ui/button";
import { notFound } from "next/navigation";

// Mock Data - In real app, fetch from API
const getPack = (id: string) => {
  const packs = {
    "1": {
      title: "FastAPI Production Vibes",
      author: "KenanDev",
      description: "Strict rules for building high-performance APIs.",
      terms: [
        { term: "Lifespan", definition: "Context manager for startup/shutdown events.", insight: "Use this instead of on_event startup." },
      ],
      vibes: [
        { instruction: "Use Pydantic V2", context: "V1 is deprecated and slower.", tags: ["Syntax", "Performance"] },
      ],
      antiPatterns: [
        { instruction: "Do NOT use generic try/except", reason: "It hides critical DB connection errors." },
      ],
    },
     "2": {
      title: "Modern React Anti-Patterns",
      author: "JaneDoe",
      description: "Common mistakes in Next.js 14 and React 18.",
      terms: [
        { term: "Hydration Error", definition: "Mismatch between server-rendered HTML and client-side DOM.", insight: "Usually caused by random numbers or dates generated during render." },
      ],
      vibes: [
        { instruction: "Use clsx and tailwind-merge", context: "For conditional classes in Shadcn components.", tags: ["CSS", "UI"] },
      ],
      antiPatterns: [
        { instruction: "Do not use useEffect for data fetching", reason: "Use Server Components or React Query instead." },
      ],
    },
    "3": {
      title: "Generic Python Data Science",
      author: "Pythonista",
      description: "Standard practices for Pandas and NumPy.",
      terms: [
        { term: "Broadcasting", definition: "How NumPy treats arrays with different shapes during arithmetic operations.", insight: "Magic way to multiply big arrays without loops." },
      ],
      vibes: [
        { instruction: "Use vectorized operations", context: "Avoid loops in Pandas for better performance.", tags: ["Performance", "Pandas"] },
      ],
      antiPatterns: [],
    }
  };
  return packs[id as keyof typeof packs];
};

export default function PackDetail({ params }: { params: { id: string } }) {
  const pack = getPack(params.id);

  if (!pack) {
    return notFound();
  }

  const systemPrompt = `ROLE: Expert Developer
CONTEXT: ${pack.description}
RULES:
${pack.vibes.map(v => `- ${v.instruction} (${v.context})`).join("\n")}
ANTI-PATTERNS:
${pack.antiPatterns.map(a => `- ${a.instruction} (${a.reason})`).join("\n")}
GLOSSARY:
${pack.terms.map(t => `- ${t.term}: ${t.insight}`).join("\n")}
`;

  return (
    <div className="min-h-screen bg-slate-950 text-white p-8">
      <div className="max-w-5xl mx-auto">
        <Link href="/marketplace" className="text-slate-500 hover:text-white mb-6 block">← Back to Marketplace</Link>

        <header className="flex justify-between items-start mb-12">
          <div>
            <h1 className="text-4xl font-bold mb-2">{pack.title}</h1>
            <p className="text-emerald-400 font-mono text-sm mb-4">by @{pack.author}</p>
            <p className="text-slate-400 text-lg">{pack.description}</p>
          </div>
          <div className="flex gap-4">
             <Button variant="outline" className="border-slate-700 text-slate-300">Fork Pack</Button>
             <Button className="bg-emerald-600 hover:bg-emerald-700">Copy System Prompt</Button>
          </div>
        </header>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">

          {/* Column 1: Terms */}
          <div className="bg-slate-900/50 rounded-xl p-6 border border-slate-800">
            <h2 className="text-xl font-bold mb-4 text-purple-400">📖 Smart Glossary</h2>
            <div className="space-y-4">
              {pack.terms.map((t, i) => (
                <div key={i} className="p-4 bg-slate-950 rounded border border-slate-800">
                  <h3 className="font-bold text-white mb-1">{t.term}</h3>
                  <p className="text-xs text-slate-500 mb-2">{t.definition}</p>
                  <p className="text-sm text-yellow-100/80 italic">"{t.insight}"</p>
                </div>
              ))}
            </div>
          </div>

          {/* Column 2: Vibes */}
          <div className="bg-slate-900/50 rounded-xl p-6 border border-slate-800">
            <h2 className="text-xl font-bold mb-4 text-emerald-400">🟢 Directives</h2>
            <div className="space-y-4">
              {pack.vibes.map((v, i) => (
                <div key={i} className="p-4 bg-slate-950 rounded border border-slate-800 border-l-4 border-l-emerald-500">
                  <p className="font-bold text-white mb-2">{v.instruction}</p>
                  <p className="text-sm text-slate-400">{v.context}</p>
                  <div className="flex gap-2 mt-3">
                    {v.tags.map(tag => (
                      <span key={tag} className="text-[10px] bg-slate-800 text-slate-400 px-1.5 py-0.5 rounded uppercase tracking-wider">{tag}</span>
                    ))}
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Column 3: Anti-Patterns */}
          <div className="bg-slate-900/50 rounded-xl p-6 border border-slate-800">
            <h2 className="text-xl font-bold mb-4 text-red-400">🔴 Anti-Patterns</h2>
            <div className="space-y-4">
              {pack.antiPatterns.map((a, i) => (
                <div key={i} className="p-4 bg-slate-950 rounded border border-slate-800 border-l-4 border-l-red-900">
                   <p className="font-bold text-white mb-2">{a.instruction}</p>
                   <p className="text-sm text-slate-400">{a.reason}</p>
                </div>
              ))}
            </div>
          </div>

        </div>

        <div className="mt-12 p-6 bg-black rounded-xl border border-slate-800 font-mono text-sm text-slate-300">
          <div className="flex justify-between items-center mb-4">
            <span className="text-slate-500">Preview: System Prompt</span>
          </div>
          <pre className="whitespace-pre-wrap">{systemPrompt}</pre>
        </div>
      </div>
    </div>
  );
}
