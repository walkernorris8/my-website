import os, re

NEW_FOOTER = '''      <footer className="bg-gray-900 py-10 px-6 text-center text-sm">
        <div className="flex justify-center mb-4">
          <img src="/logo.png" alt="Apex Growth Management" className="h-12 brightness-0 invert" style={{ objectFit: "contain" }} />
        </div>
        <div className="flex flex-col sm:flex-row items-center justify-center gap-3 mt-2 text-white/50">
          <a href="tel:9197440504" className="hover:text-white transition-colors">(919) 744-0504</a>
          <span className="hidden sm:inline text-white/20">·</span>
          <a href="mailto:admin@apexgrowthmanagement.com" className="hover:text-white transition-colors">admin@apexgrowthmanagement.com</a>
        </div>
        <p className="text-white/30 mt-4">© {new Date().getFullYear()} Apex Growth Management. All rights reserved.</p>
      </footer>'''

pages = [
    "app/page.tsx",
    "app/services/page.tsx",
    "app/about/page.tsx",
    "app/pricing/page.tsx",
    "app/contact/page.tsx",
    "app/portfolio/page.tsx",
    "app/blog/page.tsx",
    "app/blog/[slug]/page.tsx",
]

base = "C:/Users/walke/Desktop/my-website"
FOOTER_PATTERN = re.compile(r'\s*<footer[^>]*>.*?</footer>', re.DOTALL)

for rel in pages:
    path = os.path.join(base, rel)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    new_content = FOOTER_PATTERN.sub("\n" + NEW_FOOTER, content)
    if new_content != content:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated: {rel}")
    else:
        print(f"No footer found: {rel}")

print("Done!")
