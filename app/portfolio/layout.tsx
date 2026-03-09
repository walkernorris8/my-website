import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Portfolio",
  description:
    "See real website examples built by Apex Growth Management — HVAC, restaurant, and plumbing industry templates ready to customize for your business.",
  openGraph: {
    title: "Portfolio | Website Examples — Apex Growth Management",
    description:
      "See real website examples built by Apex Growth Management — HVAC, restaurant, and plumbing industry templates ready to customize for your business.",
    url: "https://apexgrowthmanagement.com/portfolio",
  },
  alternates: {
    canonical: "https://apexgrowthmanagement.com/portfolio",
  },
};

export default function PortfolioLayout({ children }: { children: React.ReactNode }) {
  return <>{children}</>;
}
