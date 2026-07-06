"""Product landing page example - SaaS style."""
import htmlskill as hs
from pathlib import Path


@hs.page(mode="web-prototype", design_system="huashu", brand="MyProduct")
def product_landing():
    """Create a SaaS product landing page."""

    # Navigation
    hs.navbar(
        logo="https://via.placeholder.com/140x40/667eea/ffffff?text=MyProduct",
        links=["Features", "Pricing", "Docs", "Login"]
    )

    # Hero with value proposition
    with hs.hero(background="gradient"):
        hs.heading("Ship Faster with AI-Powered Tools", level=1)
        hs.text(
            "Build, deploy, and scale your applications 10x faster with our intelligent platform.",
            size="large"
        )
        hs.spacer(height="32px")
        hs.button("Start Free Trial", style="primary", size="large")
        hs.spacer(height="16px")
        hs.text("No credit card required • 14-day trial", size="medium")

    # Social proof
    with hs.section(padding="48px 0"):
        with hs.container(max_width="1200px"):
            hs.text("Trusted by 10,000+ developers at", size="medium", align="center")
            hs.spacer(height="24px")
            # Placeholder for company logos

    # Key features
    with hs.section(padding="80px 0"):
        with hs.container(max_width="1200px"):
            hs.heading("Everything You Need to Build Great Products", level=2, align="center")
            hs.spacer(height="48px")

            hs.features(items=[
                {
                    "icon": "⚡",
                    "title": "Lightning Fast",
                    "description": "Deploy in seconds with our optimized infrastructure. 99.99% uptime guaranteed."
                },
                {
                    "icon": "🔒",
                    "title": "Enterprise Security",
                    "description": "SOC 2 compliant. Your data is encrypted at rest and in transit."
                },
                {
                    "icon": "🌍",
                    "title": "Global CDN",
                    "description": "Serve users worldwide with sub-100ms latency from 200+ edge locations."
                },
                {
                    "icon": "📊",
                    "title": "Real-time Analytics",
                    "description": "Understand your users with built-in analytics and monitoring dashboards."
                },
                {
                    "icon": "🔌",
                    "title": "API-First",
                    "description": "Integrate with anything. Comprehensive REST and GraphQL APIs included."
                },
                {
                    "icon": "💬",
                    "title": "24/7 Support",
                    "description": "Our expert team is always here to help. Average response time: 2 minutes."
                },
            ])

    # Pricing teaser
    with hs.section(padding="80px 0"):
        with hs.container(max_width="800px"):
            hs.heading("Simple, Transparent Pricing", level=2, align="center")
            hs.spacer(height="24px")
            hs.text(
                "Start free, scale as you grow. No hidden fees, no surprises.",
                size="large",
                align="center"
            )
            hs.spacer(height="32px")
            hs.button("View Pricing Plans", style="primary", size="large")

    # Final CTA
    with hs.cta(background="linear-gradient(135deg, #667eea 0%, #764ba2 100%)"):
        hs.heading("Ready to Transform Your Workflow?", level=2)
        hs.spacer(height="24px")
        hs.text("Join thousands of developers already building with MyProduct.", size="large")
        hs.spacer(height="32px")
        hs.button("Get Started Free", style="primary", size="large")
        hs.spacer(height="16px")
        hs.text("Free 14-day trial • No credit card required", size="medium")

    # Footer
    hs.footer(
        copyright="© 2026 MyProduct Inc. All rights reserved.",
        links=["Terms", "Privacy", "Security", "Status", "Contact"]
    )


if __name__ == "__main__":
    from htmlskill.renderers.web import WebPrototypeRenderer

    ctx = product_landing()
    renderer = WebPrototypeRenderer()
    html = renderer.render(ctx)

    output_dir = Path(__file__).parent / "output"
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / "product-landing.html"
    output_file.write_text(html, encoding="utf-8")

    print(f"✅ Generated: {output_file}")
    print(f"🌐 Open: file://{output_file.absolute()}")
