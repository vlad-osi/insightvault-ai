export default function Home() {
  return (
    <main className="min-h-screen flex items-center justify-center bg-zinc-950 text-white">
      <div className="text-center">
        <h1 className="text-5xl font-bold">InsightVault AI</h1>

        <p className="mt-4 text-zinc-400">
          AI-powered knowledge base for your documents
        </p>

        <button className="mt-8 rounded-xl bg-white px-6 py-3 text-black font-medium">
          Upload Documents
        </button>
      </div>
    </main>
  );
}
