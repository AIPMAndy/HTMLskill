# Getting Started with HTMLskill

## Installation

### Using pip (Recommended)

```bash
pip install htmlskill
```

### From source

```bash
git clone https://github.com/AIPMAndy/HTMLskill.git
cd HTMLskill
pip install -e .
```

### With optional dependencies

```bash
# For CLI tools
pip install htmlskill[cli]

# For image processing
pip install htmlskill[image]

# Everything
pip install htmlskill[full]

# Development
pip install htmlskill[dev]
```

## Your First Page (60 seconds)

### 1. Create a Python file

Create `my_first_page.py`:

```python
import htmlskill as hs

@hs.page(mode="web-prototype", design_system="huashu")
def my_landing_page():
    hs.heading("Welcome to My Site", level=1)
    hs.text("This page was generated with Python!")
    hs.button("Get Started", style="primary", size="large")
```

### 2. Generate HTML

Add this to the bottom of your file:

```python
if __name__ == "__main__":
    from htmlskill.renderers.web import WebPrototypeRenderer
    from pathlib import Path

    ctx = my_landing_page()
    renderer = WebPrototypeRenderer()
    html = renderer.render(ctx)

    Path("output.html").write_text(html)
    print("✅ Generated output.html")
```

### 3. Run it

```bash
python3 my_first_page.py
```

### 4. Open the result

```bash
open output.html
```

That's it! You've generated your first HTML page with HTMLskill.

## Understanding the Basics

### Page Decorator

The `@hs.page()` decorator tells HTMLskill this function defines a page:

```python
@hs.page(
    mode="web-prototype",      # Output format
    design_system="huashu",    # Design constraints
    brand="My Brand"           # Optional branding
)
def my_page():
    # Your components here
    pass
```

### Components

HTMLskill provides three types of components:

#### Basic Components

Simple, single-purpose elements:

```python
hs.heading("Title", level=1)
hs.text("Paragraph text", size="large")
hs.button("Click me", style="primary")
hs.image("photo.jpg", alt="Photo")
hs.spacer(height="32px")
hs.divider()
```

#### Layout Components

Structural containers using context managers:

```python
with hs.container(max_width="1200px"):
    with hs.grid(columns=3, gap="32px"):
        hs.text("Column 1")
        hs.text("Column 2")
        hs.text("Column 3")
```

#### Composite Components

Pre-built sections:

```python
with hs.hero(background="gradient"):
    hs.heading("Welcome")
    hs.text("Description")
    hs.button("Call to Action")
```

### Rendering

To convert your page to HTML:

```python
from htmlskill.renderers.web import WebPrototypeRenderer

ctx = my_page()              # Execute page function
renderer = WebPrototypeRenderer()
html = renderer.render(ctx)  # Generate HTML string
```

## Next Steps

### Try More Examples

```bash
cd examples
python3 00-minimal.py
python3 04-complete-with-output.py
python3 05-product-landing.py
```

### Learn the API

Read the [API Reference](api-reference.md) to see all available components.

### Build Something Real

Start with a template:
- Landing page → `examples/05-product-landing.py`
- Simple page → `examples/00-minimal.py`
- Complete site → `examples/04-complete-with-output.py`

### Join the Community

- [GitHub Discussions](https://github.com/AIPMAndy/HTMLskill/discussions)
- [Report Issues](https://github.com/AIPMAndy/HTMLskill/issues)
- [Contribute](../CONTRIBUTING.md)

## Common Patterns

### Full Landing Page

```python
@hs.page(mode="web-prototype", design_system="huashu")
def landing():
    # Navigation
    hs.navbar(logo="logo.png", links=["Home", "About", "Contact"])

    # Hero section
    with hs.hero(background="gradient"):
        hs.heading("Your Product Name")
        hs.text("Value proposition")
        hs.button("Get Started", style="primary")

    # Features
    with hs.section(padding="80px 0"):
        hs.heading("Features", level=2, align="center")
        hs.features(items=[
            {"icon": "⚡", "title": "Fast", "description": "Lightning fast"},
            {"icon": "🎨", "title": "Beautiful", "description": "Great design"},
        ])

    # Footer
    hs.footer(copyright="© 2026 Your Company")
```

### Responsive Grid

```python
with hs.grid(columns=3, gap="24px"):
    for i in range(6):
        with hs.card(title=f"Item {i+1}"):
            hs.text("Card content here")
```

## Troubleshooting

### Import Error

```bash
ModuleNotFoundError: No module named 'htmlskill'
```

Solution: Make sure htmlskill is installed:
```bash
pip install htmlskill
```

### Template Not Found

```bash
jinja2.exceptions.TemplateNotFound
```

Solution: Install htmlskill properly with package data:
```bash
pip install -e .
```

### No HTML Output

Make sure you're calling the renderer:
```python
ctx = my_page()  # This returns a context, not HTML
renderer = WebPrototypeRenderer()
html = renderer.render(ctx)  # This generates HTML
```

## Getting Help

- Check [FAQ](faq.md)
- Search [GitHub Issues](https://github.com/AIPMAndy/HTMLskill/issues)
- Ask in [Discussions](https://github.com/AIPMAndy/HTMLskill/discussions)
- Read [examples](../examples/)
