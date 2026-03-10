import { ImageResponse } from "next/og";

export const runtime = "edge";
export const alt = "Apex Growth Management Blog";
export const size = { width: 1200, height: 630 };
export const contentType = "image/png";

export default async function Image({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;

  const query = encodeURIComponent(
    `*[_type == "post" && slug.current == "${slug}"][0]{ title, excerpt }`
  );

  let title = "Web Design & SEO Blog";
  let excerpt = "Tips and insights for local businesses in Raleigh, NC";

  try {
    const res = await fetch(
      `https://g1hic8ei.apicdn.sanity.io/v2021-10-21/data/query/production?query=${query}`,
      { next: { revalidate: 3600 } }
    );
    const data = await res.json();
    if (data.result?.title) title = data.result.title;
    if (data.result?.excerpt) excerpt = data.result.excerpt;
  } catch {
    // fallback to defaults above
  }

  // Truncate excerpt to keep layout clean
  const shortExcerpt = excerpt && excerpt.length > 140 ? excerpt.slice(0, 137) + "…" : excerpt;

  return new ImageResponse(
    (
      <div
        style={{
          background: "#030712",
          width: "100%",
          height: "100%",
          display: "flex",
          flexDirection: "column",
          alignItems: "flex-start",
          justifyContent: "center",
          padding: "72px 80px",
          position: "relative",
        }}
      >
        {/* Grid overlay — inline SVG as background */}
        <div
          style={{
            position: "absolute",
            inset: 0,
            backgroundImage:
              "linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px)",
            backgroundSize: "60px 60px",
          }}
        />

        {/* Blue accent line top-left */}
        <div
          style={{
            position: "absolute",
            top: 0,
            left: 80,
            width: 80,
            height: 3,
            background: "#2563eb",
            borderRadius: 99,
          }}
        />

        {/* Brand label */}
        <div
          style={{
            display: "flex",
            alignItems: "center",
            gap: 10,
            marginBottom: 36,
          }}
        >
          <div
            style={{
              width: 8,
              height: 8,
              borderRadius: "50%",
              background: "#60a5fa",
            }}
          />
          <span
            style={{
              fontSize: 15,
              fontWeight: 600,
              color: "#60a5fa",
              letterSpacing: "0.18em",
              textTransform: "uppercase",
            }}
          >
            Apex Growth Management
          </span>
        </div>

        {/* Post title */}
        <div
          style={{
            fontSize: title.length > 60 ? 44 : 54,
            fontWeight: 800,
            color: "#ffffff",
            lineHeight: 1.18,
            marginBottom: 28,
            maxWidth: 960,
          }}
        >
          {title}
        </div>

        {/* Excerpt */}
        {shortExcerpt && (
          <div
            style={{
              fontSize: 22,
              color: "#9ca3af",
              lineHeight: 1.55,
              maxWidth: 880,
            }}
          >
            {shortExcerpt}
          </div>
        )}

        {/* Bottom bar */}
        <div
          style={{
            position: "absolute",
            bottom: 56,
            left: 80,
            right: 80,
            display: "flex",
            alignItems: "center",
            justifyContent: "space-between",
          }}
        >
          <span style={{ color: "#374151", fontSize: 16, fontWeight: 500 }}>
            apexgrowthmanagement.com/blog
          </span>
          <div
            style={{
              display: "flex",
              alignItems: "center",
              gap: 8,
              background: "#1e3a5f",
              border: "1px solid #2563eb44",
              borderRadius: 99,
              padding: "8px 18px",
            }}
          >
            <span style={{ color: "#93c5fd", fontSize: 14, fontWeight: 600 }}>
              Read Article →
            </span>
          </div>
        </div>
      </div>
    ),
    size
  );
}
