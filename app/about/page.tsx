import Link from "next/link";

const values = [
  {
    title: "Results First",
    description: "We measure success by what your business achieves — leads, sales, and growth.",
  },
  {
    title: "Clear Communication",
    description: "No jargon. We explain everything in plain English and keep you in the loop.",
  },
  {
    title: "Built to Last",
    description: "We build websites with clean code and modern practices that stand the test of time.",
  },
  {
    title: "Always Available",
    description: "When you need updates or have questions, we're quick to respond and easy to reach.",
  },
];

export default function AboutPage() {
  return (
    <main className="bg-black text-white pt-24 min-h-screen">
      {/* Hero */}
      <section className="py-20 px-6">
        <div className="max-w-4xl mx-auto text-center">
          <h1 className="text-4xl md:text-6xl font-extrabold mb-6">
            About <span className="text-blue-500">Apex Growth</span>
          </h1>
          <p className="text-white/60 text-lg md:text-xl leading-relaxed max-w-2xl mx-auto">
            Apex Growth Management was built with one goal: help small and medium businesses compete online. We handle the technical side so you can focus on what you do best.
          </p>
        </div>
      </section>

      {/* Story */}
      <section className="py-16 px-6 bg-white/[0.02]">
        <div className="max-w-3xl mx-auto">
          <h2 className="text-2xl md:text-3xl font-bold mb-6 text-blue-400">Our Story</h2>
          <div className="text-white/60 leading-relaxed space-y-4 text-lg">
            <p>
              We started Apex Growth Management because we kept seeing the same problem: great local businesses with no online presence, or worse — a website that was doing them more harm than good.
            </p>
            <p>
              We built this company to fix that. We offer professional-grade web services at a price that makes sense for real businesses — not just enterprise clients with big budgets.
            </p>
            <p>
              Whether you're launching a new business or refreshing an existing one, we'll build you something you're proud of and keep it running smoothly.
            </p>
          </div>
        </div>
      </section>

      {/* Values */}
      <section className="py-20 px-6">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-2xl md:text-3xl font-bold mb-12 text-center">What We Stand For</h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
            {values.map((v) => (
              <div
                key={v.title}
                className="border border-white/10 bg-white/[0.03] rounded-2xl p-6 hover:border-blue-500/40 transition-colors"
              >
                <h3 className="text-lg font-semibold text-blue-400 mb-2">{v.title}</h3>
                <p className="text-white/50 leading-relaxed">{v.description}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="py-16 px-6 text-center">
        <h3 className="text-2xl font-bold mb-4">Let's work together</h3>
        <p className="text-white/50 mb-8">Reach out and let's talk about what your business needs.</p>
        <Link
          href="/contact"
          className="bg-blue-600 hover:bg-blue-500 text-white font-semibold px-8 py-4 rounded-full text-lg transition-colors"
        >
          Get in Touch
        </Link>
      </section>

      <footer className="border-t border-white/10 py-8 px-6 text-center text-white/30 text-sm">
        © {new Date().getFullYear()} Apex Growth Management. All rights reserved.
      </footer>
    </main>
  );
}
