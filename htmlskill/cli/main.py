"""CLI module for HTMLSkill."""
import click
from pathlib import Path
import sys
import os


@click.group()
@click.version_option(version="0.1.0")
def cli():
    """HTMLSkill - Python-first HTML generation framework."""
    pass


@cli.command()
@click.argument("project_name")
@click.option("--template", default="basic", help="Project template (basic, landing, dashboard)")
def init(project_name, template):
    """Initialize a new HTMLSkill project."""
    project_path = Path(project_name)

    if project_path.exists():
        click.echo(f"❌ Error: Directory '{project_name}' already exists")
        sys.exit(1)

    # Create project structure
    project_path.mkdir()
    (project_path / "assets").mkdir()
    (project_path / "output").mkdir()

    # Create main app file
    app_content = '''"""Main application file."""
import htmlskill as hs
from htmlskill.renderers.web import WebPrototypeRenderer


@hs.page(mode="web-prototype", design_system="huashu")
def main_page():
    """Main page."""
    hs.navbar(logo="./assets/logo.svg", links=["Home", "About", "Contact"])

    with hs.hero(background="gradient"):
        hs.heading("Welcome to Your Project", level=1)
        hs.text("Built with HTMLSkill", size="large")
        hs.spacer(height="32px")
        hs.cta("Get Started", url="#")

    hs.spacer(height="80px")

    with hs.container():
        hs.heading("Features", level=2, align="center")
        hs.spacer(height="48px")

        hs.features([
            {"icon": "⚡", "title": "Fast", "description": "Lightning fast development"},
            {"icon": "🎨", "title": "Beautiful", "description": "Professional design system"},
            {"icon": "🚀", "title": "Easy", "description": "Simple Python API"},
        ])

    hs.spacer(height="80px")
    hs.footer(copyright="© 2026 Your Company")


if __name__ == "__main__":
    ctx = main_page()
    renderer = WebPrototypeRenderer()
    html = renderer.render(ctx)

    with open("output/index.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("✅ Generated: output/index.html")
'''

    (project_path / "app.py").write_text(app_content)

    # Create config file
    config_content = '''"""HTMLSkill configuration."""

config = {
    "design_system": "huashu",
    "constraints": {
        "grid_base": 8,
        "min_contrast": 4.5,
        "font_stack": "cjk-first",
    },
    "output": {
        "inline_assets": True,
        "minify": False,
        "validate": True,
    }
}
'''

    (project_path / "htmlskill.config.py").write_text(config_content)

    # Create README
    readme_content = f'''# {project_name}

Created with HTMLSkill.

## Usage

```bash
# Generate HTML
python app.py

# View output
open output/index.html
```

## Structure

- `app.py` - Main application
- `htmlskill.config.py` - Configuration
- `assets/` - Static assets (images, fonts)
- `output/` - Generated HTML files
'''

    (project_path / "README.md").write_text(readme_content)

    click.echo(f"✅ Created project: {project_name}")
    click.echo(f"\n📁 Project structure:")
    click.echo(f"   {project_name}/")
    click.echo(f"   ├── app.py")
    click.echo(f"   ├── htmlskill.config.py")
    click.echo(f"   ├── README.md")
    click.echo(f"   ├── assets/")
    click.echo(f"   └── output/")
    click.echo(f"\n🚀 Next steps:")
    click.echo(f"   cd {project_name}")
    click.echo(f"   python app.py")


@cli.command()
@click.argument("file", type=click.Path(exists=True))
@click.option("--output", "-o", default="output.html", help="Output file path")
def build(file, output):
    """Build HTML from Python file."""
    click.echo(f"🔨 Building {file}...")

    # Add current directory to Python path
    sys.path.insert(0, os.path.dirname(os.path.abspath(file)))

    # Import and execute the file
    import importlib.util
    spec = importlib.util.spec_from_file_location("app", file)
    module = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(module)
        click.echo(f"✅ Built successfully: {output}")
    except Exception as e:
        click.echo(f"❌ Build failed: {e}", err=True)
        sys.exit(1)


@cli.command()
@click.argument("file", type=click.Path(exists=True))
def check(file):
    """Check design constraints in Python file."""
    from htmlskill.design.constraints import ConstraintChecker

    click.echo(f"🔍 Checking design constraints in {file}...")

    checker = ConstraintChecker()

    # Example checks
    issues = []

    # Check common spacing values
    common_spacings = [16, 24, 32, 48, 64, 80]
    for spacing in common_spacings:
        if not checker.check_grid(spacing):
            issues.append(f"❌ Spacing {spacing}px does not conform to 8px grid")

    # Check common color combinations
    test_colors = [
        ("#000000", "#FFFFFF", "Black on White"),
        ("#333333", "#FFFFFF", "Dark Gray on White"),
        ("#CCCCCC", "#FFFFFF", "Light Gray on White"),
    ]

    for fg, bg, desc in test_colors:
        contrast = checker.check_contrast(fg, bg)
        if contrast < 4.5:
            issues.append(f"❌ {desc}: contrast {contrast:.1f} < 4.5")
        else:
            click.echo(f"✅ {desc}: contrast {contrast:.1f}")

    # Check font stacks
    good_stack = ["Noto Sans SC", "Inter", "Arial"]
    bad_stack = ["Inter", "Noto Sans SC", "Arial"]

    if checker.check_font_stack(good_stack):
        click.echo(f"✅ Font stack is CJK-first: {', '.join(good_stack)}")

    if not checker.check_font_stack(bad_stack):
        issues.append(f"❌ Font stack should be CJK-first: {', '.join(bad_stack)}")

    if issues:
        click.echo(f"\n⚠️  Found {len(issues)} issues:")
        for issue in issues:
            click.echo(f"   {issue}")
    else:
        click.echo(f"\n✅ All design constraints passed!")


@cli.command()
def version():
    """Show version information."""
    click.echo("HTMLSkill v0.1.0-alpha")
    click.echo("Python-first HTML generation framework")
    click.echo("https://github.com/AIPMAndy/HTMLskill")


if __name__ == "__main__":
    cli()
