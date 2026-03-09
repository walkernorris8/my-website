/**
 * LocalBusinessSchema — Reusable JSON-LD schema component
 *
 * Drop into any client site's layout.tsx (server component).
 * Change `type` to the most specific Schema.org type for the business:
 *   "HVACBusiness" | "Plumber" | "Restaurant" | "Electrician" |
 *   "RoofingContractor" | "LandscapingBusiness" | "Dentist" | "AutoRepair" etc.
 * Full list: https://schema.org/LocalBusiness
 */

interface LocalBusinessSchemaProps {
  type?: string;
  name: string;
  description: string;
  url: string;
  telephone: string;
  email?: string;
  addressLocality: string;
  addressRegion: string;
  addressPostalCode?: string;
  addressCountry?: string;
  latitude?: number;
  longitude?: number;
  areaServed?: string | string[];
  serviceType?: string[];
  priceRange?: string;
  hours?: string | string[]; // e.g. "Mo-Fr 08:00-18:00" or array for multiple ranges
  sameAs?: string[];
}

export default function LocalBusinessSchema({
  type = "LocalBusiness",
  name,
  description,
  url,
  telephone,
  email,
  addressLocality,
  addressRegion,
  addressPostalCode,
  addressCountry = "US",
  latitude,
  longitude,
  areaServed,
  serviceType,
  priceRange = "$$",
  hours,
  sameAs,
}: LocalBusinessSchemaProps) {
  const schema: Record<string, unknown> = {
    "@context": "https://schema.org",
    "@type": type,
    name,
    description,
    url,
    telephone,
    address: {
      "@type": "PostalAddress",
      addressLocality,
      addressRegion,
      ...(addressPostalCode && { postalCode: addressPostalCode }),
      addressCountry,
    },
    priceRange,
  };

  if (email) schema.email = email;

  if (latitude && longitude) {
    schema.geo = {
      "@type": "GeoCoordinates",
      latitude,
      longitude,
    };
  }

  if (areaServed) {
    if (Array.isArray(areaServed)) {
      schema.areaServed = areaServed.map((city) => ({ "@type": "City", name: city }));
    } else {
      schema.areaServed = { "@type": "State", name: areaServed };
    }
  }

  if (serviceType && serviceType.length > 0) schema.serviceType = serviceType;

  if (hours) {
    schema.openingHours = hours;
  }

  if (sameAs && sameAs.length > 0) schema.sameAs = sameAs;

  return (
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{ __html: JSON.stringify(schema) }}
    />
  );
}
