"""Example 3: Render to HTML file."""
import htmlskill as hs
from htmlskill.renderers.web import WebPrototypeRenderer


@hs.page(mode="web-prototype", design_system="huashu", brand="MyCompany")
def demo_page():
    """Create a demo page and render to HTML."""

    # Navigation
    hs.navbar(logo="./logo.svg", links=["Features", "Pricing", "About"])

    # Hero section
    with hs.hero(background="gradient"):
        hs.heading("Welcome to HTMLSkill", level=1)
        hs.text("Build professional HTML with Python code", size="large")
        hs.spacer(height="32px")
        hs.cta("Get Started", url="https://github.com/AIPMAndy/HTMLskill")

    hs.spacer(height="80px")

    # Features section
    with hs.container():
        hs.heading("Core Features", level=2, align="center")
        hs.spacer(height="48px")

        hs.features([
            {
                "icon": "🎨",
                "title": "Design System",
                "description": "Built-in huashu-design constraints"
            },
            {
                "icon": "🚀",
                "title": "Fast Development",
                "description": "Write HTML with Python decorators"
            },
            {
                "icon": "✅",
                "title": "Type Safe",
                "description": "Full type hints and IDE support"
            },
        ])

    hs.spacer(height="80px")

    # Footer
    hs.footer(
        copyright="© 2026 HTMLSkill. MIT License.",
        links=["GitHub", "Documentation", "Examples"]
    )


if __name__ == "__main__":
    # Execute the page function
    ctx = demo_page()

    # Render to HTML
    renderer = WebPrototypeRenderer()
    html = renderer.render(ctx)

    # Save to file
    output_file = "demo-output.html"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ HTML generated successfully!")
    print(f"   Output: {output_file}")
    print(f"   Components: {len(ctx.components)}")
    print(f"   Size: {len(html)} bytes")
    print(f"\n🌐 Open {output_file} in your browser to view the result!")
