import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Services",
  description:
    "Web design, hosting, SEO, and ongoing maintenance for local businesses in Raleigh, NC. Everything you need to succeed online — in one place.",
  openGraph: {
    title: "Web Design & SEO Services | Apex Growth Management",
    description:
      "Web design, hosting, SEO, and ongoing maintenance for local businesses in Raleigh, NC. Everything you need to succeed online — in one place.",
    url: "https://apexgrowthmanagement.com/services",
  },
  alternates: {
    canonical: "https://apexgrowthmanagement.com/services",
  },
};

export default function ServicesLayout({ children }: { children: React.ReactNode }) {
  return <>{children}</>;
}
