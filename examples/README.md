# HTMLskill Examples

All example scripts with generated HTML outputs.

## Quick Start

Run any example:

```bash
python3 00-minimal.py
```

Or generate all examples at once:

```bash
python3 generate_all.py
```

## Examples List

### 00-minimal.py
**The simplest possible HTMLskill page**

Just 3 lines of code to generate a beautiful page.

```bash
python3 00-minimal.py
open output/minimal.html
```

### 01-landing-page.py
**Simple landing page**

Basic landing page demonstrating core components.

### 02-complete-landing.py
**Complete landing page with sections**

More comprehensive example with multiple sections.

### 03-render-to-html.py
**Rendering demonstration**

Shows how to convert context to HTML.

### 04-complete-with-output.py
**Full landing page with HTML generation**

Complete example that generates actual HTML file.

Features:
- Navigation bar
- Hero section with gradient
- Features grid
- Code example section
- CTA section
- Footer

```bash
python3 04-complete-with-output.py
open output/complete-landing.html
```

### 05-product-landing.py
**Professional SaaS landing page**

Real-world SaaS product landing page example.

Features:
- Professional navigation
- Value proposition hero
- Social proof section
- 6-item features grid
- Pricing teaser
- Final CTA
- Comprehensive footer

```bash
python3 05-product-landing.py
open output/product-landing.html
```

### 06-blog-post.py
**Blog article layout**

Article page with rich content structure.

Features:
- Blog navigation
- Article header with metadata
- Featured image
- Article content with headings
- Related articles grid
- Newsletter subscription CTA

```bash
python3 06-blog-post.py
open output/blog-post.html
```

### 07-portfolio.py
**Personal portfolio page**

Developer portfolio showcasing projects and skills.

Features:
- Personal hero section
- About section
- Featured projects grid
- Skills showcase (6 categories)
- Testimonials
- Contact CTA

```bash
python3 07-portfolio.py
open output/portfolio.html
```

## Generating All Examples

Use the provided script to generate all examples:

```bash
python3 generate_all.py
```

This will:
- Find all example files (00-*.py, 01-*.py, etc.)
- Execute each one
- Generate HTML files in `output/`
- Show summary with file:// links

## Output Directory

All generated HTML files are saved to:

```
examples/output/
├── minimal.html
├── complete-landing.html
├── product-landing.html
├── blog-post.html
├── portfolio.html
└── ... (more examples)
```

## Live Preview

After generating, open in your browser:

```bash
# macOS
open output/product-landing.html

# Linux
xdg-open output/product-landing.html

# Windows
start output/product-landing.html
```

Or use a local server:

```bash
cd output
python3 -m http.server 8000
# Visit http://localhost:8000
```

## Customizing Examples

All examples are fully customizable Python scripts. Modify them to:

- Change text and content
- Adjust colors and styles
- Add or remove sections
- Experiment with layouts

Example modification:

```python
# In any example file, change:
hs.heading("Original Title", level=1)

# To:
hs.heading("My Custom Title", level=1)

# Then re-run the script to see changes
```

## Using Examples as Templates

Copy any example as a starting point:

```bash
cp 05-product-landing.py my-landing-page.py
```

Then customize it for your needs.

## Learning Path

Recommended order for learning:

1. **00-minimal.py** - Understand the basics
2. **04-complete-with-output.py** - See full page structure
3. **05-product-landing.py** - Study real-world patterns
4. **06-blog-post.py** - Learn content layout
5. **07-portfolio.py** - Explore complex grids

## Common Patterns

### Hero Section
```python
with hs.hero(gradient="blue"):
    hs.heading("Main Title", level=1)
    hs.text("Subtitle or description")
    hs.button("Call to Action", style="primary")
```

### Features Grid
```python
hs.features(items=[
    {
        "icon": "⚡",
        "title": "Feature Name",
        "description": "Feature description"
    },
    # ... more features
])
```

### Card Grid
```python
with hs.grid(columns=3, gap="32px"):
    with hs.card(title="Card 1"):
        hs.text("Content")
    with hs.card(title="Card 2"):
        hs.text("Content")
    with hs.card(title="Card 3"):
        hs.text("Content")
```

## Troubleshooting

### Module not found
```
ModuleNotFoundError: No module named 'htmlskill'
```

**Solution**: Install htmlskill first
```bash
pip install htmlskill
# OR for development
pip install -e ..
```

### Output directory doesn't exist

The scripts automatically create the `output/` directory, but you can create it manually:

```bash
mkdir -p output
```

### Generated HTML doesn't look right

Make sure you're viewing the complete rendered HTML, not the source. Open in a web browser, not a text editor.

## Contributing Examples

Have a great example? Contribute it!

1. Create a new file: `08-your-example.py`
2. Follow the existing pattern
3. Include generation code at the bottom
4. Add documentation to this README
5. Submit a PR

See [CONTRIBUTING.md](../CONTRIBUTING.md) for details.

## Need Help?

- Check the [main documentation](../docs/)
- Ask in [GitHub Discussions](https://github.com/AIPMAndy/HTMLskill/discussions)
- Review the [FAQ](../docs/faq.md)

## Live Demos

View live demos of all examples:
👉 https://aipmandty.github.io/HTMLskill/

---

**Tip**: Start with the simplest examples and progressively explore more complex ones. Each example builds on concepts from the previous ones.
