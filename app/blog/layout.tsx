import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Blog",
  description:
    "Web design tips, SEO insights, and growth strategies for local businesses. Written by the team at Apex Growth Management in Raleigh, NC.",
  openGraph: {
    title: "Blog | Web Design Tips — Apex Growth Management",
    description:
      "Web design tips, SEO insights, and growth strategies for local businesses. Written by the team at Apex Growth Management in Raleigh, NC.",
    url: "https://apexgrowthmanagement.com/blog",
  },
  alternates: {
    canonical: "https://apexgrowthmanagement.com/blog",
  },
};

export default function BlogLayout({ children }: { children: React.ReactNode }) {
  return <>{children}</>;
}
