import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Pricing",
  description:
    "Transparent pricing for web design and monthly SEO retainers. Sites starting at $1,000 with no long-term contracts. Raleigh, NC.",
  openGraph: {
    title: "Pricing | Apex Growth Management",
    description:
      "Transparent pricing for web design and monthly SEO retainers. Sites starting at $1,000 with no long-term contracts. Raleigh, NC.",
    url: "https://apexgrowthmanagement.com/pricing",
  },
  alternates: {
    canonical: "https://apexgrowthmanagement.com/pricing",
  },
};

export default function PricingLayout({ children }: { children: React.ReactNode }) {
  return <>{children}</>;
}
