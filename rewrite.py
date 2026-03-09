import os

base = "C:/Users/walke/Desktop/my-website"

globals_css = r'''@import "tailwindcss";
@plugin "@tailwindcss/typography";

:root {
  --background: #ffffff;
  --foreground: #111111;
}

body {
  background: var(--background);
  color: var(--foreground);
  font-family: var(--font-geist-sans), Arial, Helvetica, sans-serif;
}

html {
  scroll-behavior: smooth;
}
'''

navbar = r'''"use client";

import { useState } from "react";
import Link from "next/link";

export default function Navbar() {
  const [open, setOpen] = useState(false);

  return (
    <nav className="fixed top-0 left-0 right-0 z-50 bg-gray-900/95 backdrop-blur border-b border-white/10">
      <div className="max-w-6xl mx-auto px-6 flex items-center justify-between h-16">
        <Link href="/" className="text-xl font-bold tracking-tight">
          <span className="text-white">Apex</span>
          <span className="text-blue-400"> Growth</span>
        </Link>

        {/* Desktop nav */}
        <div className="hidden md:flex items-center gap-8 text-sm font-medium">
          <a href="tel:9197440504" className="text-white/60 hover:text-white transition-colors">(919) 744-0504</a>
          <Link href="/" className="text-white/60 hover:text-white transition-colors">Home</Link>
          <Link href="/services" className="text-white/60 hover:text-white transition-colors">Services</Link>
          <Link href="/pricing" className="text-white/60 hover:text-white transition-colors">Pricing</Link>
          <Link href="/about" className="text-white/60 hover:text-white transition-colors">About</Link>
          <Link href="/portfolio" className="text-white/60 hover:text-white transition-colors">Portfolio</Link>
          <Link href="/blog" className="text-white/60 hover:text-white transition-colors">Blog</Link>
          <a href="https://calendly.com/admin-apexgrowthmanagement/30min" target="_blank" rel="noopener noreferrer" className="text-white/60 hover:text-white transition-colors">Book a Call</a>
          <Link href="/contact" className="bg-blue-600 hover:bg-blue-500 text-white px-5 py-2 rounded-full transition-colors">
            Get Started
          </Link>
        </div>

        {/* Mobile hamburger */}
        <button className="md:hidden text-white/70 hover:text-white" onClick={() => setOpen(!open)} aria-label="Toggle menu">
          <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            {open ? (
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            ) : (
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
            )}
          </svg>
        </button>
      </div>

      {open && (
        <div className="md:hidden border-t border-white/10 bg-gray-900 px-6 py-4 flex flex-col gap-4 text-sm font-medium">
          <Link href="/" onClick={() => setOpen(false)} className="text-white/60 hover:text-white transition-colors">Home</Link>
          <Link href="/services" onClick={() => setOpen(false)} className="text-white/60 hover:text-white transition-colors">Services</Link>
          <Link href="/pricing" onClick={() => setOpen(false)} className="text-white/60 hover:text-white transition-colors">Pricing</Link>
          <Link href="/about" onClick={() => setOpen(false)} className="text-white/60 hover:text-white transition-colors">About</Link>
          <Link href="/portfolio" onClick={() => setOpen(false)} className="text-white/60 hover:text-white transition-colors">Portfolio</Link>
          <Link href="/blog" onClick={() => setOpen(false)} className="text-white/60 hover:text-white transition-colors">Blog</Link>
          <a href="https://calendly.com/admin-apexgrowthmanagement/30min" target="_blank" rel="noopener noreferrer" onClick={() => setOpen(false)} className="text-white/60 hover:text-white transition-colors">Book a Call</a>
          <Link href="/contact" onClick={() => setOpen(false)} className="bg-blue-600 hover:bg-blue-500 text-white px-5 py-2 rounded-full text-center transition-colors">Get Started</Link>
        </div>
      )}
    </nav>
  );
}
'''

home = r'''import Link from "next/link";
import Image from "next/image";
import { Monitor, Zap, Wrench, TrendingUp } from "lucide-react";

const services = [
  { Icon: Monitor, title: "Website Design", description: "Custom, professional websites built to convert visitors into customers." },
  { Icon: Zap, title: "Hosting & Performance", description: "Fast, reliable hosting with 99.9% uptime so your site is always live." },
  { Icon: Wrench, title: "Minor Updates", description: "Need a change? We handle text, images, and layout updates quickly." },
  { Icon: TrendingUp, title: "SEO Optimization", description: "Rank higher on Google and drive organic traffic to your business." },
];

export default function Home() {
  return (
    <main className="bg-white text-gray-900">
      {/* Hero */}
      <section className="relative min-h-screen flex flex-col items-center justify-center text-center px-6 pt-16 overflow-hidden">
        <Image src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1920&q=80&fit=crop" alt="Web design workspace" fill className="object-cover" priority />
        <div className="absolute inset-0 bg-black/72" />
        <div className="max-w-4xl mx-auto relative z-10 text-white">
          <div className="inline-block bg-blue-600/20 border border-blue-500/30 text-blue-300 text-sm font-medium px-4 py-1.5 rounded-full mb-6">
            Website Design · Hosting · SEO
          </div>
          <h1 className="text-5xl md:text-7xl font-extrabold tracking-tight leading-tight mb-6">
            Grow Your Business<br />
            <span className="text-blue-400">Online.</span>
          </h1>
          <p className="text-lg md:text-xl text-white/70 max-w-2xl mx-auto mb-10">
            Apex Growth Management builds fast, professional websites and handles everything — design, hosting, updates, and SEO — so you can focus on running your business.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link href="/contact" className="bg-blue-600 hover:bg-blue-500 text-white font-semibold px-8 py-4 rounded-full text-lg transition-colors">Get Started</Link>
            <Link href="/services" className="border border-white/30 hover:border-white/60 text-white/80 hover:text-white font-semibold px-8 py-4 rounded-full text-lg transition-colors">Our Services</Link>
          </div>
        </div>
      </section>

      {/* Services Overview */}
      <section className="py-24 px-6 bg-gray-50">
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-5xl font-bold mb-4">What We Do</h2>
            <p className="text-gray-500 text-lg max-w-xl mx-auto">Everything your business needs to succeed online — all in one place.</p>
          </div>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
            {services.map(({ Icon, title, description }) => (
              <div key={title} className="bg-white border border-gray-200 rounded-2xl p-6 hover:border-blue-500/40 hover:bg-blue-50 transition-all group">
                <div className="w-11 h-11 bg-gray-50 border border-gray-200 rounded-xl flex items-center justify-center mb-5 group-hover:bg-blue-50 group-hover:border-blue-200 transition-all">
                  <Icon className="w-5 h-5 text-blue-600" />
                </div>
                <h3 className="text-lg font-semibold mb-2">{title}</h3>
                <p className="text-gray-500 text-sm leading-relaxed">{description}</p>
              </div>
            ))}
          </div>
          <div className="text-center mt-12">
            <Link href="/services" className="text-blue-600 hover:text-blue-500 font-medium transition-colors">See all services →</Link>
          </div>
        </div>
      </section>

      {/* How It Works */}
      <section className="py-24 px-6">
        <div className="max-w-4xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-5xl font-bold mb-4">How It Works</h2>
            <p className="text-gray-500 text-lg max-w-xl mx-auto">From first call to live site in as little as a week.</p>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {[
              { step: "01", title: "Get in Touch", desc: "Fill out our contact form or give us a call. We'll learn about your business and what you need." },
              { step: "02", title: "We Build It", desc: "We design and build your site. You'll get a preview link to review before anything goes live." },
              { step: "03", title: "You Launch", desc: "Once you're happy, we go live on your domain. We handle everything — no technical knowledge needed." },
            ].map((item) => (
              <div key={item.step} className="flex flex-col items-center text-center">
                <div className="text-5xl font-extrabold text-gray-200 mb-4">{item.step}</div>
                <h3 className="text-lg font-bold mb-2">{item.title}</h3>
                <p className="text-gray-500 text-sm leading-relaxed">{item.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Testimonials */}
      <section className="py-24 px-6 bg-gray-50 border-y border-gray-200">
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-5xl font-bold mb-4">What Clients Say</h2>
            <p className="text-gray-500 text-lg max-w-xl mx-auto">Real results for real businesses.</p>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {[
              { quote: "Apex built our site in under a week and we started getting calls from Google within the first month. Best investment we've made.", name: "James R.", business: "JR Plumbing Co." },
              { quote: "I had no idea how bad our old website was until I saw the new one. Clean, fast, and our booking requests doubled.", name: "Maria S.", business: "Sunshine Cleaning Services" },
              { quote: "They handle everything — updates, SEO, hosting. I don't have to think about it. That alone is worth the monthly fee.", name: "David K.", business: "K&D Electrical" },
            ].map((t) => (
              <div key={t.name} className="bg-white border border-gray-200 rounded-2xl p-6">
                <p className="text-gray-600 text-sm leading-relaxed mb-6">&ldquo;{t.quote}&rdquo;</p>
                <div>
                  <div className="font-semibold text-sm">{t.name}</div>
                  <div className="text-gray-400 text-xs">{t.business}</div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="relative py-32 px-6 overflow-hidden">
        <Image src="https://images.unsplash.com/photo-1497366216548-37526070297c?w=1920&q=80&fit=crop" alt="Modern office" fill className="object-cover" />
        <div className="absolute inset-0 bg-black/80" />
        <div className="relative z-10 max-w-3xl mx-auto text-center text-white">
          <h2 className="text-3xl md:text-5xl font-bold mb-6">
            Ready to grow your<br />
            <span className="text-blue-400">online presence?</span>
          </h2>
          <p className="text-white/60 text-lg mb-10">Let&apos;s build something great together. Contact us today for a free consultation.</p>
          <Link href="/contact" className="bg-blue-600 hover:bg-blue-500 text-white font-semibold px-10 py-4 rounded-full text-lg transition-colors">Contact Us</Link>
        </div>
      </section>

      <footer className="bg-gray-900 py-8 px-6 text-center text-white/30 text-sm">
        © {new Date().getFullYear()} Apex Growth Management. All rights reserved.
      </footer>
    </main>
  );
}
'''

services_page = r'''import Link from "next/link";
import { Monitor, Zap, Wrench, TrendingUp } from "lucide-react";

const services = [
  { Icon: Monitor, title: "Website Design", description: "We design custom, mobile-friendly websites tailored to your brand. From layout to color scheme to copywriting guidance — we handle it all. Your site will look great on every device and be built to convert visitors into leads.", features: ["Custom design", "Mobile responsive", "Fast load times", "Modern tech stack"] },
  { Icon: Zap, title: "Hosting & Performance", description: "Your website needs a reliable home. We provide fast, secure hosting with 99.9% uptime. No more worrying about downtime, slow load speeds, or expired SSL certificates.", features: ["99.9% uptime guarantee", "SSL certificate included", "Daily backups", "24/7 monitoring"] },
  { Icon: Wrench, title: "Minor Updates", description: "Business changes, and your website should too. Whether you need new photos, updated pricing, a new page, or a small design tweak — we take care of it quickly so you don't have to learn code.", features: ["Text & image updates", "New pages or sections", "Layout adjustments", "Quick turnaround"] },
  { Icon: TrendingUp, title: "SEO Optimization", description: "Ranking on Google is how customers find you. We optimize your site's content, structure, and technical setup to improve your visibility in search results and drive real organic traffic.", features: ["Keyword research", "On-page SEO", "Technical SEO audit", "Monthly reporting"] },
];

export default function ServicesPage() {
  return (
    <main className="bg-white text-gray-900 pt-24 min-h-screen">
      <section className="py-20 px-6">
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-20">
            <h1 className="text-4xl md:text-6xl font-extrabold mb-4">Our Services</h1>
            <p className="text-gray-500 text-lg max-w-xl mx-auto">Everything you need to build, grow, and maintain your online presence.</p>
          </div>

          <div className="flex flex-col gap-8">
            {services.map(({ Icon, title, description, features }, i) => (
              <div key={title} className={`flex flex-col md:flex-row gap-8 items-start p-8 rounded-2xl border border-gray-200 bg-gray-50 ${i % 2 === 1 ? "md:flex-row-reverse" : ""}`}>
                <div className="shrink-0">
                  <div className="w-16 h-16 bg-white border border-gray-200 rounded-2xl flex items-center justify-center">
                    <Icon className="w-7 h-7 text-blue-600" />
                  </div>
                </div>
                <div>
                  <h2 className="text-2xl font-bold mb-3">{title}</h2>
                  <p className="text-gray-600 leading-relaxed mb-6">{description}</p>
                  <ul className="flex flex-wrap gap-2">
                    {features.map((f) => (
                      <li key={f} className="bg-blue-50 border border-blue-200 text-blue-700 text-sm px-3 py-1 rounded-full">{f}</li>
                    ))}
                  </ul>
                </div>
              </div>
            ))}
          </div>

          <div className="text-center mt-20">
            <h3 className="text-2xl font-bold mb-4">Ready to get started?</h3>
            <Link href="/contact" className="bg-blue-600 hover:bg-blue-500 text-white font-semibold px-8 py-4 rounded-full text-lg transition-colors">Contact Us</Link>
          </div>
        </div>
      </section>

      <footer className="bg-gray-900 py-8 px-6 text-center text-white/30 text-sm">
        © {new Date().getFullYear()} Apex Growth Management. All rights reserved.
      </footer>
    </main>
  );
}
'''

about_page = r'''import Link from "next/link";
import Image from "next/image";

const values = [
  { title: "Results First", description: "We measure success by what your business achieves — leads, sales, and growth." },
  { title: "Clear Communication", description: "No jargon. We explain everything in plain English and keep you in the loop." },
  { title: "Built to Last", description: "We build websites with clean code and modern practices that stand the test of time." },
  { title: "Always Available", description: "When you need updates or have questions, we're quick to respond and easy to reach." },
];

export default function AboutPage() {
  return (
    <main className="bg-white text-gray-900 pt-24 min-h-screen">
      {/* Hero */}
      <section className="relative py-32 px-6 overflow-hidden">
        <Image src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=1920&q=80&fit=crop" alt="Laptop and workspace" fill className="object-cover" />
        <div className="absolute inset-0 bg-black/78" />
        <div className="relative z-10 max-w-4xl mx-auto text-center text-white">
          <h1 className="text-4xl md:text-6xl font-extrabold mb-6">
            About <span className="text-blue-400">Apex Growth</span>
          </h1>
          <p className="text-white/75 text-lg md:text-xl leading-relaxed max-w-2xl mx-auto">
            Apex Growth Management was built with one goal: help small and medium businesses compete online. We handle the technical side so you can focus on what you do best.
          </p>
        </div>
      </section>

      {/* Story */}
      <section className="py-20 px-6">
        <div className="max-w-5xl mx-auto grid md:grid-cols-2 gap-16 items-center">
          <div>
            <h2 className="text-2xl md:text-3xl font-bold mb-6 text-blue-600">Our Story</h2>
            <div className="text-gray-600 leading-relaxed space-y-4 text-lg">
              <p>We started Apex Growth Management because we kept seeing the same problem: great local businesses with no online presence, or worse — a website that was doing them more harm than good.</p>
              <p>We built this company to fix that. We offer professional-grade web services at a price that makes sense for real businesses — not just enterprise clients with big budgets.</p>
              <p>Whether you&apos;re launching a new business or refreshing an existing one, we&apos;ll build you something you&apos;re proud of and keep it running smoothly.</p>
            </div>
          </div>
          <div className="relative rounded-2xl overflow-hidden h-80">
            <Image src="https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&q=80&fit=crop" alt="Code on screen" fill className="object-cover" />
          </div>
        </div>
      </section>

      {/* Values */}
      <section className="py-20 px-6 bg-gray-50 border-y border-gray-200">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-2xl md:text-3xl font-bold mb-12 text-center">What We Stand For</h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
            {values.map((v) => (
              <div key={v.title} className="border border-gray-200 bg-white rounded-2xl p-6 hover:border-blue-300 transition-colors">
                <h3 className="text-lg font-semibold text-blue-600 mb-2">{v.title}</h3>
                <p className="text-gray-500 leading-relaxed">{v.description}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Photo quote banner */}
      <section className="relative h-64 overflow-hidden">
        <Image src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1920&q=80&fit=crop" alt="Working on laptop" fill className="object-cover" />
        <div className="absolute inset-0 bg-black/75 flex items-center justify-center">
          <p className="text-2xl md:text-4xl font-extrabold text-center text-white max-w-xl px-6">
            &ldquo;Your website should work as hard as <span className="text-blue-400">you do.</span>&rdquo;
          </p>
        </div>
      </section>

      {/* CTA */}
      <section className="py-20 px-6 text-center">
        <h3 className="text-2xl font-bold mb-4">Let&apos;s work together</h3>
        <p className="text-gray-500 mb-8">Reach out and let&apos;s talk about what your business needs.</p>
        <Link href="/contact" className="bg-blue-600 hover:bg-blue-500 text-white font-semibold px-8 py-4 rounded-full text-lg transition-colors">Get in Touch</Link>
      </section>

      <footer className="bg-gray-900 py-8 px-6 text-center text-white/30 text-sm">
        © {new Date().getFullYear()} Apex Growth Management. All rights reserved.
      </footer>
    </main>
  );
}
'''

pricing_page = r'''import Link from "next/link";
import { Check } from "lucide-react";

const setupFees = [
  { name: "Standard", price: "$1,000", description: "Perfect for small businesses getting started online.", features: ["4-page website","Mobile responsive","Contact form","Basic SEO setup","2 rounds of revisions"] },
  { name: "Pro", price: "$1,500", description: "For businesses that need more pages and custom features.", features: ["Up to 8 pages","Mobile responsive","Contact form","Advanced SEO setup","Custom design elements","3 rounds of revisions"], popular: true },
  { name: "Premium", price: "$2,000", description: "Fully custom site with everything you need to stand out.", features: ["Unlimited pages","Mobile responsive","Contact form","Full SEO setup","Custom design","Priority build time","Unlimited revisions"] },
];

const retainers = [
  { name: "Basic", price: "$249", description: "Keep your site live and up to date.", features: ["Website hosting","Monthly minor updates","Uptime monitoring","SSL certificate"] },
  { name: "Growth", price: "$349", description: "Grow your online presence month over month.", features: ["Everything in Basic","SEO optimization","Monthly performance report","Google Business management"], popular: true },
  { name: "Premium", price: "$499", description: "Full-service management for serious businesses.", features: ["Everything in Growth","Priority support","Content updates","Competitor analysis","Quarterly strategy call"] },
];

export default function PricingPage() {
  return (
    <main className="bg-white text-gray-900 pt-24 min-h-screen">
      <section className="py-20 px-6">
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-20">
            <h1 className="text-4xl md:text-6xl font-extrabold mb-4">Simple Pricing</h1>
            <p className="text-gray-500 text-lg max-w-xl mx-auto">Transparent pricing with no hidden fees. Pay once to build, then a monthly retainer to grow.</p>
          </div>

          {/* Setup Fees */}
          <div className="mb-20">
            <h2 className="text-2xl font-bold text-center mb-2">Website Build</h2>
            <p className="text-gray-400 text-center text-sm mb-10">One-time fee to design and launch your site</p>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              {setupFees.map((plan) => (
                <div key={plan.name} className={`relative rounded-2xl p-8 border flex flex-col ${plan.popular ? "border-blue-500 bg-blue-50" : "border-gray-200 bg-gray-50"}`}>
                  {plan.popular && (
                    <div className="absolute -top-3 left-1/2 -translate-x-1/2 bg-blue-600 text-white text-xs font-semibold px-4 py-1 rounded-full">Most Popular</div>
                  )}
                  <div className="mb-6">
                    <h3 className="text-lg font-bold mb-1">{plan.name}</h3>
                    <div className="text-4xl font-extrabold text-gray-900 mb-2">{plan.price}</div>
                    <p className="text-gray-400 text-sm">{plan.description}</p>
                  </div>
                  <ul className="flex flex-col gap-3 mb-8 flex-1">
                    {plan.features.map((f) => (
                      <li key={f} className="flex items-center gap-2 text-sm text-gray-600">
                        <Check className="w-4 h-4 text-blue-600 shrink-0" /> {f}
                      </li>
                    ))}
                  </ul>
                  <Link href="/contact" className={`text-center font-semibold py-3 rounded-full transition-colors ${plan.popular ? "bg-blue-600 hover:bg-blue-500 text-white" : "border border-gray-300 hover:border-gray-500 text-gray-700 hover:text-gray-900"}`}>Get Started</Link>
                </div>
              ))}
            </div>
          </div>

          {/* Monthly Retainers */}
          <div className="mb-20">
            <h2 className="text-2xl font-bold text-center mb-2">Monthly Retainer</h2>
            <p className="text-gray-400 text-center text-sm mb-10">Ongoing hosting, updates, and SEO — billed monthly</p>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              {retainers.map((plan) => (
                <div key={plan.name} className={`relative rounded-2xl p-8 border flex flex-col ${plan.popular ? "border-blue-500 bg-blue-50" : "border-gray-200 bg-gray-50"}`}>
                  {plan.popular && (
                    <div className="absolute -top-3 left-1/2 -translate-x-1/2 bg-blue-600 text-white text-xs font-semibold px-4 py-1 rounded-full">Most Popular</div>
                  )}
                  <div className="mb-6">
                    <h3 className="text-lg font-bold mb-1">{plan.name}</h3>
                    <div className="text-4xl font-extrabold text-gray-900 mb-1">{plan.price}<span className="text-lg text-gray-400 font-normal">/mo</span></div>
                    <p className="text-gray-400 text-sm">{plan.description}</p>
                  </div>
                  <ul className="flex flex-col gap-3 mb-8 flex-1">
                    {plan.features.map((f) => (
                      <li key={f} className="flex items-center gap-2 text-sm text-gray-600">
                        <Check className="w-4 h-4 text-blue-600 shrink-0" /> {f}
                      </li>
                    ))}
                  </ul>
                  <Link href="/contact" className={`text-center font-semibold py-3 rounded-full transition-colors ${plan.popular ? "bg-blue-600 hover:bg-blue-500 text-white" : "border border-gray-300 hover:border-gray-500 text-gray-700 hover:text-gray-900"}`}>Get Started</Link>
                </div>
              ))}
            </div>
          </div>

          {/* FAQ */}
          <div className="max-w-3xl mx-auto">
            <h2 className="text-2xl font-bold text-center mb-10">Common Questions</h2>
            <div className="flex flex-col gap-4">
              {[
                { q: "Do I have to pay the setup fee and retainer?", a: "The setup fee is a one-time charge to build your site. The retainer is optional but recommended — it covers hosting, updates, and SEO so your site stays live and keeps growing." },
                { q: "Can I cancel the monthly retainer?", a: "Yes, you can cancel anytime. If you cancel, you keep your domain and we can transfer your site files to you." },
                { q: "How long does it take to build my site?", a: "Most sites are ready for review within 5-7 business days after we receive your content and onboarding form." },
                { q: "What counts as a minor update?", a: "Text changes, image swaps, adding a new section, updating hours or pricing — anything that takes under an hour. Larger changes are quoted separately." },
              ].map((item) => (
                <div key={item.q} className="border border-gray-200 rounded-2xl p-6 bg-gray-50">
                  <h3 className="font-semibold mb-2">{item.q}</h3>
                  <p className="text-gray-500 text-sm leading-relaxed">{item.a}</p>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      <footer className="bg-gray-900 py-8 px-6 text-center text-white/30 text-sm">
        © {new Date().getFullYear()} Apex Growth Management. All rights reserved.
      </footer>
    </main>
  );
}
'''

contact_page = r'''"use client";

import { useState } from "react";
import { CalendarDays } from "lucide-react";

export default function ContactPage() {
  const [form, setForm] = useState({ firstName: "", lastName: "", email: "", business: "", service: "", message: "" });
  const [status, setStatus] = useState<"idle" | "sending" | "success" | "error">("idle");

  function handleChange(e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>) {
    setForm({ ...form, [e.target.name]: e.target.value });
  }

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setStatus("sending");
    const res = await fetch("/api/contact", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(form) });
    setStatus(res.ok ? "success" : "error");
  }

  return (
    <main className="bg-white text-gray-900 pt-24 min-h-screen">
      <section className="py-20 px-6">
        <div className="max-w-2xl mx-auto">
          <div className="text-center mb-12">
            <h1 className="text-4xl md:text-6xl font-extrabold mb-4">Get in Touch</h1>
            <p className="text-gray-500 text-lg mb-6">Tell us about your project and we'll get back to you within 24 hours.</p>
            <a href="https://calendly.com/admin-apexgrowthmanagement/30min" target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-2 bg-gray-900 hover:bg-gray-800 text-white font-semibold px-6 py-3 rounded-full transition-colors text-sm">
              <CalendarDays className="w-4 h-4" /> Prefer to talk? Book a free 30-min call
            </a>
          </div>

          {status === "success" ? (
            <div className="text-center py-16">
              <div className="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-4">
                <svg className="w-8 h-8 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" /></svg>
              </div>
              <h2 className="text-2xl font-bold mb-2">Message Sent!</h2>
              <p className="text-gray-500">We'll get back to you within 24 hours.</p>
            </div>
          ) : (
            <form onSubmit={handleSubmit} className="flex flex-col gap-5">
              <div className="flex flex-col sm:flex-row gap-5">
                <div className="flex-1 flex flex-col gap-2">
                  <label className="text-sm text-gray-500 font-medium">First Name</label>
                  <input name="firstName" value={form.firstName} onChange={handleChange} required type="text" placeholder="John" className="bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 text-gray-900 placeholder-gray-400 focus:outline-none focus:border-blue-500 transition-colors" />
                </div>
                <div className="flex-1 flex flex-col gap-2">
                  <label className="text-sm text-gray-500 font-medium">Last Name</label>
                  <input name="lastName" value={form.lastName} onChange={handleChange} required type="text" placeholder="Smith" className="bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 text-gray-900 placeholder-gray-400 focus:outline-none focus:border-blue-500 transition-colors" />
                </div>
              </div>
              <div className="flex flex-col gap-2">
                <label className="text-sm text-gray-500 font-medium">Email</label>
                <input name="email" value={form.email} onChange={handleChange} required type="email" placeholder="john@example.com" className="bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 text-gray-900 placeholder-gray-400 focus:outline-none focus:border-blue-500 transition-colors" />
              </div>
              <div className="flex flex-col gap-2">
                <label className="text-sm text-gray-500 font-medium">Business Name (optional)</label>
                <input name="business" value={form.business} onChange={handleChange} type="text" placeholder="Your Business" className="bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 text-gray-900 placeholder-gray-400 focus:outline-none focus:border-blue-500 transition-colors" />
              </div>
              <div className="flex flex-col gap-2">
                <label className="text-sm text-gray-500 font-medium">What do you need?</label>
                <select name="service" value={form.service} onChange={handleChange} className="bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 text-gray-900 focus:outline-none focus:border-blue-500 transition-colors">
                  <option value="">Select a service</option>
                  <option value="Website Design">Website Design</option>
                  <option value="Hosting">Hosting</option>
                  <option value="Minor Updates">Minor Updates</option>
                  <option value="SEO Optimization">SEO Optimization</option>
                  <option value="Full Package">Full Package</option>
                </select>
              </div>
              <div className="flex flex-col gap-2">
                <label className="text-sm text-gray-500 font-medium">Message</label>
                <textarea name="message" value={form.message} onChange={handleChange} required rows={5} placeholder="Tell us about your business and what you're looking for..." className="bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 text-gray-900 placeholder-gray-400 focus:outline-none focus:border-blue-500 transition-colors resize-none" />
              </div>
              {status === "error" && <p className="text-red-500 text-sm text-center">Something went wrong. Please try again.</p>}
              <button type="submit" disabled={status === "sending"} className="bg-blue-600 hover:bg-blue-500 disabled:opacity-50 text-white font-semibold py-4 rounded-full text-lg transition-colors mt-2">
                {status === "sending" ? "Sending..." : "Send Message"}
              </button>
            </form>
          )}

          <div className="flex flex-col items-center gap-2 mt-8 text-sm text-gray-400">
            <p>Call or text us: <a href="tel:9197440504" className="text-blue-600 hover:text-blue-500 transition-colors">(919) 744-0504</a></p>
            <p>Or email: <a href="mailto:admin@apexgrowthmanagement.com" className="text-blue-600 hover:text-blue-500 transition-colors">admin@apexgrowthmanagement.com</a></p>
          </div>
        </div>
      </section>

      <footer className="bg-gray-900 py-8 px-6 text-center text-white/30 text-sm">
        © {new Date().getFullYear()} Apex Growth Management. All rights reserved.
      </footer>
    </main>
  );
}
'''

portfolio_page = r'''import Link from "next/link";

const templates = [
  { name: "Arctic Air HVAC", industry: "HVAC / Home Services", colors: "Black & Red", description: "A bold, conversion-focused template for heating and cooling companies. Includes emergency service CTA, service pages, and a contact form.", features: ["24/7 Emergency Banner","Service Pages","Contact Form","Mobile Responsive"], demo: "https://hvac-template-taupe.vercel.app", accent: "red" },
  { name: "Ember & Oak Kitchen", industry: "Restaurant / Dining", colors: "Black & Amber", description: "An upscale restaurant template with a warm, inviting feel. Includes a full menu page, about section, and reservation contact form.", features: ["Menu Page","Reservation Form","About / Story","Mobile Responsive"], demo: "https://restaurant-template-plum-sigma.vercel.app", accent: "amber" },
];

export default function PortfolioPage() {
  return (
    <main className="bg-white text-gray-900 pt-24 min-h-screen">
      <section className="py-20 px-6">
        <div className="max-w-5xl mx-auto">
          <div className="text-center mb-16">
            <p className="text-blue-600 text-sm font-semibold uppercase tracking-widest mb-3">Our Work</p>
            <h1 className="text-4xl md:text-6xl font-extrabold mb-4">Client Templates</h1>
            <p className="text-gray-500 text-lg max-w-2xl mx-auto">Every site we build is custom-designed for your industry. Here are a few examples of what your new website could look like.</p>
          </div>

          <div className="grid md:grid-cols-2 gap-8">
            {templates.map((t) => (
              <div key={t.name} className="bg-gray-50 border border-gray-200 rounded-2xl overflow-hidden hover:border-gray-300 transition-colors">
                <div className={`h-2 w-full ${t.accent === "red" ? "bg-red-600" : "bg-amber-500"}`} />
                <div className="p-8">
                  <div className="flex items-start justify-between mb-4">
                    <div>
                      <h2 className="text-xl font-bold">{t.name}</h2>
                      <p className="text-gray-400 text-sm mt-1">{t.industry}</p>
                    </div>
                    <span className={`text-xs font-semibold px-3 py-1 rounded-full border ${t.accent === "red" ? "border-red-300 text-red-600 bg-red-50" : "border-amber-300 text-amber-600 bg-amber-50"}`}>{t.colors}</span>
                  </div>
                  <p className="text-gray-600 text-sm leading-relaxed mb-6">{t.description}</p>
                  <ul className="flex flex-wrap gap-2 mb-8">
                    {t.features.map((f) => (
                      <li key={f} className="text-xs bg-white border border-gray-200 rounded-full px-3 py-1 text-gray-500">{f}</li>
                    ))}
                  </ul>
                  <a href={t.demo} target="_blank" rel="noopener noreferrer" className={`inline-block font-semibold px-6 py-3 rounded-full text-sm transition-colors text-white ${t.accent === "red" ? "bg-red-600 hover:bg-red-500" : "bg-amber-500 hover:bg-amber-400"}`}>View Live Demo →</a>
                </div>
              </div>
            ))}
          </div>

          <div className="mt-20 text-center bg-gray-900 rounded-2xl p-12">
            <h2 className="text-3xl font-extrabold mb-4 text-white">Want a site like this?</h2>
            <p className="text-white/50 mb-8 max-w-xl mx-auto">We build custom websites tailored to your business. Starting at $1,000 with no monthly contracts on setup.</p>
            <Link href="/contact" className="bg-blue-600 hover:bg-blue-500 text-white font-semibold px-8 py-4 rounded-full text-lg transition-colors">Get Started</Link>
          </div>
        </div>
      </section>

      <footer className="bg-gray-900 py-8 px-6 text-center text-white/30 text-sm">
        © {new Date().getFullYear()} Apex Growth Management. All rights reserved.
      </footer>
    </main>
  );
}
'''

blog_page = r'''import Link from "next/link";
import { client } from "@/sanity/lib/client";

interface Post {
  _id: string;
  title: string;
  slug: { current: string };
  publishedAt: string;
  excerpt: string;
}

async function getPosts(): Promise<Post[]> {
  return client.fetch(
    `*[_type == "post"] | order(publishedAt desc) { _id, title, slug, publishedAt, excerpt }`
  );
}

export default async function BlogPage() {
  const posts = await getPosts();

  return (
    <main className="bg-white text-gray-900 pt-24 min-h-screen">
      <section className="py-20 px-6">
        <div className="max-w-4xl mx-auto">
          <div className="text-center mb-16">
            <h1 className="text-4xl md:text-6xl font-extrabold mb-4">Blog</h1>
            <p className="text-gray-500 text-lg max-w-xl mx-auto">Tips and insights to help your business grow online.</p>
          </div>

          {posts.length === 0 ? (
            <p className="text-center text-gray-400">No posts yet — check back soon.</p>
          ) : (
            <div className="flex flex-col gap-6">
              {posts.map((post) => (
                <Link key={post._id} href={`/blog/${post.slug.current}`} className="border border-gray-200 bg-gray-50 rounded-2xl p-8 hover:border-blue-300 hover:bg-blue-50 transition-all">
                  <div className="text-gray-400 text-sm mb-2">
                    {new Date(post.publishedAt).toLocaleDateString("en-US", { year: "numeric", month: "long", day: "numeric" })}
                  </div>
                  <h2 className="text-xl font-bold mb-3">{post.title}</h2>
                  <p className="text-gray-500 leading-relaxed">{post.excerpt}</p>
                  <div className="text-blue-600 text-sm font-medium mt-4">Read more →</div>
                </Link>
              ))}
            </div>
          )}
        </div>
      </section>

      <footer className="bg-gray-900 py-8 px-6 text-center text-white/30 text-sm">
        © {new Date().getFullYear()} Apex Growth Management. All rights reserved.
      </footer>
    </main>
  );
}
'''

files = {
    f"{base}/app/globals.css": globals_css,
    f"{base}/components/Navbar.tsx": navbar,
    f"{base}/app/page.tsx": home,
    f"{base}/app/services/page.tsx": services_page,
    f"{base}/app/about/page.tsx": about_page,
    f"{base}/app/pricing/page.tsx": pricing_page,
    f"{base}/app/contact/page.tsx": contact_page,
    f"{base}/app/portfolio/page.tsx": portfolio_page,
    f"{base}/app/blog/page.tsx": blog_page,
}

for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written: {path}")

print("All done!")
