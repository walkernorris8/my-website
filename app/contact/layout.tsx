import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Contact Us",
  description:
    "Get in touch with Apex Growth Management. Book a free consultation or send us a message — we'll get back to you within one business day.",
  openGraph: {
    title: "Contact Us | Apex Growth Management",
    description:
      "Get in touch with Apex Growth Management. Book a free consultation or send us a message — we'll get back to you within one business day.",
    url: "https://apexgrowthmanagement.com/contact",
  },
  alternates: {
    canonical: "https://apexgrowthmanagement.com/contact",
  },
};

export default function ContactLayout({ children }: { children: React.ReactNode }) {
  return <>{children}</>;
}
