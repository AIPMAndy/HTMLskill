"""Example 2: Complete landing page with all components."""
import htmlskill as hs


@hs.page(mode="web-prototype", design_system="huashu", brand="MyStartup")
def complete_landing_page():
    """Create a complete landing page with all available components."""

    # Navigation bar
    hs.navbar(logo="./logo.svg", links=["Features", "Pricing", "About", "Contact"])

    # Hero section
    with hs.hero(background="gradient"):
        hs.heading("Build Amazing Products", level=1)
        hs.text("The fastest way to ship your ideas", size="large")
        hs.spacer(height="32px")
        hs.cta("Get Started Free", url="https://example.com/signup")
        hs.spacer(height="16px")
        hs.button("Watch Demo", style="secondary", size="large")

    hs.spacer(height="80px")

    # Features section
    with hs.container(max_width="1200px"):
        with hs.section(padding="80px"):
            hs.heading("Why Choose Us", level=2, align="center")
            hs.spacer(height="48px")

            hs.features([
                {
                    "icon": "⚡",
                    "title": "Lightning Fast",
                    "description": "Optimized for speed and performance"
                },
                {
                    "icon": "🔒",
                    "title": "Secure by Default",
                    "description": "Bank-grade security built-in"
                },
                {
                    "icon": "🌍",
                    "title": "Global Scale",
                    "description": "Deploy to 135+ countries instantly"
                },
            ])

    hs.spacer(height="80px")
    hs.divider()
    hs.spacer(height="80px")

    # Testimonials section
    with hs.container(max_width="1200px"):
        hs.heading("What Our Customers Say", level=2, align="center")
        hs.spacer(height="48px")

        with hs.grid(columns=3, gap="32px"):
            with hs.card(title="Amazing Product"):
                hs.text("This tool has transformed how we work. Highly recommended!")
                hs.spacer(height="16px")
                hs.text("- Sarah Chen, CEO", size="small")

            with hs.card(title="Game Changer"):
                hs.text("The best investment we made this year. ROI in 2 weeks.")
                hs.spacer(height="16px")
                hs.text("- Mike Johnson, CTO", size="small")

            with hs.card(title="Simply Perfect"):
                hs.text("Intuitive, powerful, and reliable. Everything we needed.")
                hs.spacer(height="16px")
                hs.text("- Lisa Wang, Designer", size="small")

    hs.spacer(height="80px")

    # CTA section
    with hs.section(padding="80px"):
        hs.heading("Ready to Get Started?", level=2, align="center")
        hs.spacer(height="24px")
        hs.text("Join thousands of happy customers today", size="large")
        hs.spacer(height="32px")
        hs.cta("Start Your Free Trial", url="https://example.com/trial")

    hs.spacer(height="80px")

    # Footer
    hs.footer(
        copyright="© 2026 MyStartup. All rights reserved.",
        links=["Privacy", "Terms", "Contact"]
    )


if __name__ == "__main__":
    # Execute the page function
    ctx = complete_landing_page()

    # Print summary
    print(f"✅ Page generated successfully!")
    print(f"   Mode: {ctx.mode}")
    print(f"   Design System: {ctx.design_system}")
    print(f"   Brand: {ctx.brand}")
    print(f"   Components: {len(ctx.components)}")
    print(f"\n📋 Component breakdown:")

    component_counts = {}
    for comp in ctx.components:
        comp_type = comp["type"]
        component_counts[comp_type] = component_counts.get(comp_type, 0) + 1

    for comp_type, count in sorted(component_counts.items()):
        print(f"   - {comp_type}: {count}")
