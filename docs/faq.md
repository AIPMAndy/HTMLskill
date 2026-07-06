# Frequently Asked Questions (FAQ)

## General Questions

### What is HTMLskill?

HTMLskill is a Python-first HTML generation framework that lets you write pure Python code to generate professional, accessible HTML pages. No templates, no build tools, no JavaScript required.

### Why use HTMLskill instead of templates?

HTMLskill offers several advantages:
- **Type Safety**: Full IDE autocomplete and type checking
- **No Context Switching**: Pure Python, no HTML/template syntax to learn
- **Built-in Design System**: Professional design without manual CSS
- **Component Reusability**: Python functions for reusable components
- **WCAG AA Compliance**: Accessibility built-in by default

### Is HTMLskill production-ready?

HTMLskill is currently in **alpha** (v0.1.x). It's suitable for:
- ✅ Side projects and prototypes
- ✅ Internal tools and dashboards
- ✅ Static site generation
- ⚠️ Production use with caution (API may change)

For production use, we recommend:
- Pin the exact version in requirements.txt
- Extensive testing of your use case
- Be prepared for API changes in minor versions

### How does HTMLskill compare to React/Vue?

HTMLskill is designed for **server-side HTML generation**, not client-side SPAs:

**Use HTMLskill for:**
- Landing pages, blogs, documentation sites
- Server-rendered web pages
- Email templates, PDFs, presentations
- Prototypes and MVPs

**Use React/Vue for:**
- Complex single-page applications
- Rich client-side interactivity
- Real-time collaborative tools
- Complex client-side state management

See [Comparison Guide](comparison.md) for detailed comparison.

---

## Installation & Setup

### How do I install HTMLskill?

```bash
pip install htmlskill
```

For development:
```bash
pip install htmlskill[dev]
```

### What are the minimum requirements?

- Python 3.8 or higher
- pip (Python package manager)

Dependencies:
- `jinja2>=3.1.0` (only required dependency)

### Can I use HTMLskill with Flask/Django/FastAPI?

Yes! HTMLskill is framework-agnostic. Example with Flask:

```python
from flask import Flask
import htmlskill as hs
from htmlskill.renderers.web import WebPrototypeRenderer

app = Flask(__name__)
renderer = WebPrototypeRenderer()

@app.route("/")
def index():
    @hs.page(mode="web-prototype")
    def page():
        hs.heading("Hello from Flask!")
    
    ctx = page()
    html = renderer.render(ctx)
    return html
```

---

## Usage Questions

### How do I save generated HTML to a file?

```python
from pathlib import Path

@hs.page(mode="web-prototype")
def my_page():
    hs.heading("Hello")

ctx = my_page()
renderer = WebPrototypeRenderer()
html = renderer.render(ctx)

# Save to file
Path("output.html").write_text(html, encoding="utf-8")
```

### Can I pass data to pages?

Yes, pages are just Python functions:

```python
@hs.page(mode="web-prototype")
def product_page(product_name, price, features):
    hs.heading(product_name, level=1)
    hs.text(f"Price: ${price}")
    
    for feature in features:
        hs.text(f"• {feature}")

# Call with data
ctx = product_page("Widget Pro", 99.99, ["Fast", "Reliable", "Easy"])
```

### How do I add custom CSS?

Currently, HTMLskill uses inline CSS and design system constraints. For custom styling:

**Option 1**: Use the design system parameters
```python
hs.text("Custom colored text", color="#ff6600")
```

**Option 2**: Post-process the HTML (add `<style>` tag)
```python
html = renderer.render(ctx)
custom_css = "<style>.my-class { color: red; }</style>"
html = html.replace("</head>", f"{custom_css}</head>")
```

**Option 3**: Wait for v0.2.0 which will support custom CSS injection

### Can I create custom components?

Yes, use the `@component` decorator:

```python
@hs.component("feature-card")
def feature_card(icon, title, description):
    with hs.card():
        hs.text(icon, size="large")
        hs.heading(title, level=3)
        hs.text(description)

# Use it
feature_card("⚡", "Fast", "Lightning fast performance")
```

### How do I handle user-generated content safely?

Always sanitize user input:

```python
import html

user_input = html.escape(untrusted_data)
hs.text(user_input)
```

HTMLskill does not automatically sanitize input - you must do this yourself.

### Can I use HTMLskill for email templates?

Email mode is planned for v0.3.0. Currently, you can use `web-prototype` mode but you'll need to:
1. Use inline styles (already default)
2. Test in email clients
3. Avoid complex layouts (use tables)

---

## Design System Questions

### What is the "huashu" design system?

Huashu is the default design system with:
- 8px baseline grid for consistent spacing
- WCAG AA compliant color contrasts
- CJK (Chinese/Japanese/Korean) font optimization
- Mobile-first responsive breakpoints

### Can I customize the design system?

In v0.1.x, customization is limited. Use the `custom` design system:

```python
@hs.page(mode="web-prototype", design_system="custom")
def page():
    # More control, but manual CSS required
    pass
```

v0.4.0 will add theme customization (colors, fonts, spacing).

### How do I make pages responsive?

HTMLskill pages are responsive by default:
- Container has max-width and centers
- Grid adapts to screen size
- Font sizes scale appropriately
- Images are responsive (max-width: 100%)

### Does HTMLskill support dark mode?

Not yet. Dark mode support is planned for v0.4.0.

---

## Performance Questions

### Is HTMLskill fast?

Yes! Benchmarks show competitive performance:
- ~45ms to generate a landing page (50 components)
- Similar speed to Jinja2
- Much faster than React SSR

See [Comparison Guide](comparison.md#performance-comparison) for details.

### Can I cache rendered HTML?

Yes, render once and cache:

```python
from functools import lru_cache

@lru_cache(maxsize=100)
def render_product_page(product_id):
    @hs.page(mode="web-prototype")
    def page():
        # ... generate page ...
        pass
    
    ctx = page()
    return renderer.render(ctx)
```

### Does HTMLskill work with static site generators?

Yes! Generate HTML files and serve them statically:

```python
pages = ["home", "about", "contact"]

for page_name in pages:
    ctx = generate_page(page_name)
    html = renderer.render(ctx)
    Path(f"dist/{page_name}.html").write_text(html)
```

---

## Troubleshooting

### I get "ModuleNotFoundError: No module named 'htmlskill'"

Make sure htmlskill is installed:
```bash
pip install htmlskill
```

If using a virtual environment, ensure it's activated:
```bash
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### My page is empty / no HTML output

Ensure you're calling the renderer:

```python
# ❌ Wrong - returns context, not HTML
ctx = my_page()
print(ctx)  # This won't be HTML

# ✅ Correct - render context to HTML
from htmlskill.renderers.web import WebPrototypeRenderer
ctx = my_page()
renderer = WebPrototypeRenderer()
html = renderer.render(ctx)
print(html)
```

### Components don't appear in output

Make sure you're inside the page function:

```python
# ❌ Wrong - outside page function
@hs.page(mode="web-prototype")
def page():
    pass

hs.heading("This won't work")

# ✅ Correct - inside page function
@hs.page(mode="web-prototype")
def page():
    hs.heading("This works!")
```

### Jinja2 TemplateNotFound error

This usually means htmlskill wasn't installed properly. Try:

```bash
pip uninstall htmlskill
pip install htmlskill
```

Or install in development mode:
```bash
git clone https://github.com/AIPMAndy/HTMLskill.git
cd HTMLskill
pip install -e .
```

### Type hints not working in IDE

Make sure your IDE's Python language server is configured:

**VS Code**: Install Python extension
**PyCharm**: Should work out of the box
**Other**: Ensure Python language server has access to htmlskill package

---

## Contribution Questions

### How can I contribute?

See [CONTRIBUTING.md](../CONTRIBUTING.md) for full guide. Quick ways to help:
- Report bugs
- Suggest features
- Improve documentation
- Submit PRs for open issues

### I found a bug, what should I do?

1. Check [existing issues](https://github.com/AIPMAndy/HTMLskill/issues)
2. If new, [open an issue](https://github.com/AIPMAndy/HTMLskill/issues/new/choose)
3. Include:
   - Python version
   - HTMLskill version
   - Minimal code to reproduce
   - Expected vs actual behavior

### I want feature X, will you add it?

1. Check [ROADMAP.md](../ROADMAP.md) - it might be planned
2. Search [discussions](https://github.com/AIPMAndy/HTMLskill/discussions)
3. Open a feature request with:
   - Use case description
   - Proposed API (example code)
   - Why existing features don't work

### Can I hire someone to build with HTMLskill?

The project doesn't offer commercial support yet. For now:
- Ask in [GitHub Discussions](https://github.com/AIPMAndy/HTMLskill/discussions)
- Check the [examples](../examples/) directory
- Read the [documentation](README.md)

Commercial support may be available post-v1.0.

---

## Future Plans

### When will v1.0 be released?

Target: Q3 2027. See [ROADMAP.md](../ROADMAP.md) for details.

v1.0 criteria:
- Stable API
- Comprehensive documentation
- 90%+ test coverage
- Production case studies
- Security audit

### Will there be a component marketplace?

Yes! Planned for post-v1.0. Users will be able to:
- Share custom components
- Download community components
- Rate and review components

### Will HTMLskill support client-side interactivity?

Limited interactivity is planned for v0.5.0:
- Simple animations
- Accordion, modals, tooltips
- Alpine.js or HTMX integration

For complex SPAs, use React/Vue instead.

### Can I use HTMLskill commercially?

Yes! HTMLskill is MIT licensed. You can:
- Use in commercial projects
- Modify the source
- Include in proprietary software

No attribution required (but appreciated!).

---

## Still have questions?

- 💬 [GitHub Discussions](https://github.com/AIPMAndy/HTMLskill/discussions)
- 🐛 [Report Issues](https://github.com/AIPMAndy/HTMLskill/issues)
- 📚 [Read Documentation](README.md)
- 💡 [Check Examples](../examples/)
