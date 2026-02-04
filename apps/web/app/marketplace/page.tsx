import Link from "next/link";
import { Button } from "@/components/ui/button";

// Mock Data for MVP
const packs = [
  {
    id: 1,
    title: "FastAPI Production Vibes",
    author: "KenanDev",
    description: "Strict rules for building high-performance APIs.",
    tags: ["Python", "FastAPI", "Backend"],
    stars: 452,
    forks: 120,
  },
  {
    id: 2,
    title: "Modern React Anti-Patterns",
    author: "JaneDoe",
    description: "Common mistakes in Next.js 14 and React 18.",
    tags: ["React", "Frontend", "Next.js"],
    stars: 320,
    forks: 85,
  },
  {
    id: 3,
    title: "Generic Python Data Science",
    author: "Pythonista",
    description: "Standard practices for Pandas and NumPy.",
    tags: ["Data Science", "Python"],
    stars: 150,
    forks: 30,
  },
];

export default function Marketplace() {
  return (
    <div className="min-h-screen bg-slate-950 text-white p-8">
      <div className="max-w-6xl mx-auto">
        <header className="flex justify-between items-center mb-12">
          <div>
            <h1 className="text-4xl font-bold mb-2">Marketplace</h1>
            <p className="text-slate-400">Discover and fork community Vibe Packs.</p>
          </div>
          <Link href="/create">
            <Button className="bg-emerald-600 hover:bg-emerald-700">Create New Pack</Button>
          </Link>
        </header>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {packs.map((pack) => (
            <Link href={`/pack/${pack.id}`} key={pack.id} className="block group">
              <div className="h-full bg-slate-900 border border-slate-800 rounded-xl p-6 hover:border-emerald-500/50 transition-colors">
                <div className="flex justify-between items-start mb-4">
                  <span className="text-xs font-mono text-emerald-400 bg-emerald-950/30 px-2 py-1 rounded">
                    @{pack.author}
                  </span>
                  <div className="flex gap-2 text-slate-500 text-xs">
                    <span>⭐ {pack.stars}</span>
                    <span>🍴 {pack.forks}</span>
                  </div>
                </div>
                <h3 className="text-xl font-bold mb-2 group-hover:text-emerald-400 transition-colors">
                  {pack.title}
                </h3>
                <p className="text-slate-400 text-sm mb-6 line-clamp-2">
                  {pack.description}
                </p>
                <div className="flex flex-wrap gap-2 mt-auto">
                  {pack.tags.map((tag) => (
                    <span key={tag} className="text-xs bg-slate-800 text-slate-300 px-2 py-1 rounded-full">
                      {tag}
                    </span>
                  ))}
                </div>
              </div>
            </Link>
          ))}
        </div>
      </div>
    </div>
  );
}
