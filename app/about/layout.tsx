import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "About Us",
  description:
    "Meet Walker Norris and Jack Francis — two Raleigh, NC founders helping local businesses compete online with professional web design and SEO.",
  openGraph: {
    title: "About Us | Apex Growth Management",
    description:
      "Meet Walker Norris and Jack Francis — two Raleigh, NC founders helping local businesses compete online with professional web design and SEO.",
    url: "https://apexgrowthmanagement.com/about",
  },
  alternates: {
    canonical: "https://apexgrowthmanagement.com/about",
  },
};

export default function AboutLayout({ children }: { children: React.ReactNode }) {
  return <>{children}</>;
}
