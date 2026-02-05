import Link from "next/link";
import { Button } from "@/components/ui/button";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24 bg-slate-950 text-white">
      <div className="z-10 max-w-5xl w-full items-center justify-between font-mono text-sm lg:flex">
        <p className="fixed left-0 top-0 flex w-full justify-center border-b border-gray-300 bg-gradient-to-b from-zinc-200 pb-6 pt-8 backdrop-blur-2xl dark:border-neutral-800 dark:bg-zinc-800/30 dark:from-inherit lg:static lg:w-auto  lg:rounded-xl lg:border lg:bg-gray-200 lg:p-4 lg:dark:bg-zinc-800/30">
          The Vibe Collective
        </p>
      </div>

      <div className="relative flex place-items-center before:absolute before:h-[300px] before:w-[480px] before:-translate-x-1/2 before:rounded-full before:bg-gradient-to-br before:from-transparent before:to-blue-500 before:opacity-10 before:blur-2xl after:absolute after:h-[180px] after:w-[240px] after:translate-x-1/3 after:bg-gradient-to-t after:from-sky-900 after:via-[#0141ff] after:opacity-40 after:blur-2xl z-[-1]">
        <div className="text-center">
          <h1 className="text-6xl font-bold tracking-tighter mb-4 bg-clip-text text-transparent bg-gradient-to-r from-cyan-400 to-emerald-400">
            Stop repeating yourself to AI.
          </h1>
          <p className="text-xl text-slate-400 mb-8 max-w-2xl mx-auto">
            Build, share, and fork "Context Packs" for your AI Agents.
            The GitHub for System Prompts.
          </p>
          <div className="flex gap-4 justify-center">
             <Link href="/marketplace">
              <Button size="lg" className="bg-emerald-600 hover:bg-emerald-700 text-white">
                Browse Marketplace
              </Button>
            </Link>
            <Link href="/create">
              <Button size="lg" variant="outline" className="border-slate-700 text-slate-300 hover:bg-slate-900">
                Extract Vibe
              </Button>
            </Link>
          </div>
        </div>
      </div>

      <div className="mb-32 grid text-center lg:max-w-5xl lg:w-full lg:mb-0 lg:grid-cols-3 lg:text-left mt-20 gap-8">
        <div className="group rounded-lg border border-transparent px-5 py-4 transition-colors hover:border-neutral-700 hover:bg-neutral-800/30">
          <h2 className={`mb-3 text-2xl font-semibold`}>
            Marketplace{" "}
            <span className="inline-block transition-transform group-hover:translate-x-1 motion-reduce:transform-none">
              -&gt;
            </span>
          </h2>
          <p className={`m-0 max-w-[30ch] text-sm opacity-50`}>
            Discover high-quality system prompts ranked by developers.
          </p>
        </div>

        <div className="group rounded-lg border border-transparent px-5 py-4 transition-colors hover:border-neutral-700 hover:bg-neutral-800/30">
          <h2 className={`mb-3 text-2xl font-semibold`}>
            Extraction Engine{" "}
            <span className="inline-block transition-transform group-hover:translate-x-1 motion-reduce:transform-none">
              -&gt;
            </span>
          </h2>
          <p className={`m-0 max-w-[30ch] text-sm opacity-50`}>
            Turn messy chat logs into structured context with one click.
          </p>
        </div>

        <div className="group rounded-lg border border-transparent px-5 py-4 transition-colors hover:border-neutral-700 hover:bg-neutral-800/30">
          <h2 className={`mb-3 text-2xl font-semibold`}>
            Fork & Improve{" "}
            <span className="inline-block transition-transform group-hover:translate-x-1 motion-reduce:transform-none">
              -&gt;
            </span>
          </h2>
          <p className={`m-0 max-w-[30ch] text-sm opacity-50`}>
            Customize vibe packs for your specific stack and style.
          </p>
        </div>
      </div>
    </main>
  );
}
