"""Complete working example with HTML output generation."""
import htmlskill as hs
from pathlib import Path


@hs.page(mode="web-prototype", design_system="huashu")
def complete_landing_page():
    """Create a complete landing page with all sections."""

    # Navbar
    hs.navbar(
        logo="https://via.placeholder.com/120x40/667eea/ffffff?text=HTMLskill",
        links=["Features", "Docs", "Examples", "GitHub"]
    )

    # Hero section
    with hs.hero(background="gradient"):
        hs.heading("Build Beautiful HTML with Python", level=1)
        hs.text(
            "No templates, no build tools, just Python code that generates professional web pages.",
            size="large"
        )
        hs.spacer(height="32px")
        hs.button("Get Started", style="primary", size="large")
        hs.spacer(height="16px")
        hs.button("View Examples", style="secondary", size="large")

    # Features section
    with hs.section(padding="80px 0"):
        with hs.container(max_width="1200px"):
            hs.heading("Why HTMLskill?", level=2, align="center")
            hs.spacer(height="48px")

            hs.features(items=[
                {
                    "icon": "🐍",
                    "title": "Python-First API",
                    "description": "Write pure Python code with decorators and context managers. No HTML templates needed."
                },
                {
                    "icon": "🎨",
                    "title": "Design System Built-in",
                    "description": "8px grid, WCAG AA colors, CJK fonts. Professional design out of the box."
                },
                {
                    "icon": "⚡",
                    "title": "Zero Build Tools",
                    "description": "No Webpack, no Vite, no configuration. Just run your Python script."
                },
            ])

    # Code example section
    with hs.section(padding="80px 0"):
        with hs.container(max_width="800px"):
            hs.heading("Dead Simple API", level=2, align="center")
            hs.spacer(height="32px")

            with hs.card(title="Example Code"):
                hs.text(
                    "Just three lines to create a professional page:",
                    size="medium"
                )
                hs.spacer(height="16px")
                hs.text(
                    "@hs.page(mode='web')\ndef my_page():\n    hs.heading('Hello World')",
                    color="#333"
                )

    # CTA section
    with hs.cta(background="linear-gradient(135deg, #667eea 0%, #764ba2 100%)"):
        hs.heading("Ready to Get Started?", level=2)
        hs.spacer(height="24px")
        hs.text("Install with pip and start building in 60 seconds.", size="large")
        hs.spacer(height="32px")
        hs.button("pip install htmlskill", style="primary", size="large")

    # Footer
    hs.footer(
        copyright="© 2026 HTMLskill. MIT License.",
        links=["GitHub", "Documentation", "Examples", "Community"]
    )


def generate_html_file():
    """Generate and save HTML file."""
    from htmlskill.renderers.web import WebPrototypeRenderer

    # Execute page function to get context
    ctx = complete_landing_page()

    # Render to HTML
    renderer = WebPrototypeRenderer()
    html = renderer.render(ctx)

    # Save to file
    output_dir = Path(__file__).parent / "output"
    output_dir.mkdir(exist_ok=True)

    output_file = output_dir / "complete-landing.html"
    output_file.write_text(html, encoding="utf-8")

    print(f"✅ Generated: {output_file}")
    print(f"📊 Components: {len(ctx.components)}")
    print(f"🎨 Design System: {ctx.design_system}")
    print(f"\n🌐 Open in browser:")
    print(f"   file://{output_file.absolute()}")

    return output_file


if __name__ == "__main__":
    generate_html_file()
