import Link from "next/link";

const services = [
  {
    icon: "🖥️",
    title: "Website Design",
    description:
      "We design custom, mobile-friendly websites tailored to your brand. From layout to color scheme to copywriting guidance — we handle it all. Your site will look great on every device and be built to convert visitors into leads.",
    features: ["Custom design", "Mobile responsive", "Fast load times", "Modern tech stack"],
  },
  {
    icon: "⚡",
    title: "Hosting & Performance",
    description:
      "Your website needs a reliable home. We provide fast, secure hosting with 99.9% uptime. No more worrying about downtime, slow load speeds, or expired SSL certificates.",
    features: ["99.9% uptime guarantee", "SSL certificate included", "Daily backups", "24/7 monitoring"],
  },
  {
    icon: "🔧",
    title: "Minor Updates",
    description:
      "Business changes, and your website should too. Whether you need new photos, updated pricing, a new page, or a small design tweak — we take care of it quickly so you don't have to learn code.",
    features: ["Text & image updates", "New pages or sections", "Layout adjustments", "Quick turnaround"],
  },
  {
    icon: "📈",
    title: "SEO Optimization",
    description:
      "Ranking on Google is how customers find you. We optimize your site's content, structure, and technical setup to improve your visibility in search results and drive real organic traffic.",
    features: ["Keyword research", "On-page SEO", "Technical SEO audit", "Monthly reporting"],
  },
];

export default function ServicesPage() {
  return (
    <main className="bg-black text-white pt-24 min-h-screen">
      <section className="py-20 px-6">
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-20">
            <h1 className="text-4xl md:text-6xl font-extrabold mb-4">Our Services</h1>
            <p className="text-white/50 text-lg max-w-xl mx-auto">
              Everything you need to build, grow, and maintain your online presence.
            </p>
          </div>

          <div className="flex flex-col gap-12">
            {services.map((s, i) => (
              <div
                key={s.title}
                className={`flex flex-col md:flex-row gap-8 items-start p-8 rounded-2xl border border-white/10 bg-white/[0.03] ${
                  i % 2 === 1 ? "md:flex-row-reverse" : ""
                }`}
              >
                <div className="text-5xl md:text-6xl shrink-0">{s.icon}</div>
                <div>
                  <h2 className="text-2xl font-bold mb-3">{s.title}</h2>
                  <p className="text-white/60 leading-relaxed mb-6">{s.description}</p>
                  <ul className="flex flex-wrap gap-2">
                    {s.features.map((f) => (
                      <li
                        key={f}
                        className="bg-blue-600/20 border border-blue-500/30 text-blue-300 text-sm px-3 py-1 rounded-full"
                      >
                        {f}
                      </li>
                    ))}
                  </ul>
                </div>
              </div>
            ))}
          </div>

          <div className="text-center mt-20">
            <h3 className="text-2xl font-bold mb-4">Ready to get started?</h3>
            <Link
              href="/contact"
              className="bg-blue-600 hover:bg-blue-500 text-white font-semibold px-8 py-4 rounded-full text-lg transition-colors"
            >
              Contact Us
            </Link>
          </div>
        </div>
      </section>

      <footer className="border-t border-white/10 py-8 px-6 text-center text-white/30 text-sm">
        © {new Date().getFullYear()} Apex Growth Management. All rights reserved.
      </footer>
    </main>
  );
}
