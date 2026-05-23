"""Example 1: Simple landing page."""
import htmlskill as hs


@hs.page(mode="web-prototype", design_system="huashu")
def landing_page():
    """Create a simple landing page."""
    hs.heading("Welcome to HTMLSkill", level=1)
    hs.text("Build professional HTML with Python code", size="large")
    hs.spacer(height="32px")
    hs.button("Get Started", style="primary", size="large")
    hs.spacer(height="16px")
    hs.button("Learn More", style="secondary", size="large")
    hs.spacer(height="64px")
    hs.divider()
    hs.spacer(height="32px")
    hs.heading("Features", level=2)
    hs.text("Python-first API with professional design constraints")


if __name__ == "__main__":
    # Execute the page function
    ctx = landing_page()

    # Print the collected components
    print(f"Mode: {ctx.mode}")
    print(f"Design System: {ctx.design_system}")
    print(f"Components collected: {len(ctx.components)}")
    print("\nComponents:")
    for i, comp in enumerate(ctx.components, 1):
        print(f"  {i}. {comp['type']}: {comp['props']}")
