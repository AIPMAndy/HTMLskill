"""Minimal working example - 10 lines to a beautiful page."""
import htmlskill as hs


@hs.page(mode="web-prototype", design_system="huashu")
def minimal_example():
    """Absolute minimal example."""
    hs.heading("Hello, HTMLskill! 👋", level=1)
    hs.text("This page was generated with 3 lines of Python code.")
    hs.button("Learn More", style="primary", size="large")


if __name__ == "__main__":
    from htmlskill.renderers.web import WebPrototypeRenderer
    from pathlib import Path

    ctx = minimal_example()
    renderer = WebPrototypeRenderer()
    html = renderer.render(ctx)

    output_dir = Path(__file__).parent / "output"
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / "minimal.html"
    output_file.write_text(html, encoding="utf-8")

    print(f"✅ Generated: {output_file}")
    print(f"🌐 Open: file://{output_file.absolute()}")
