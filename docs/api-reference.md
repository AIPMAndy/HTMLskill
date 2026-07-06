# API Reference

Complete reference for all HTMLskill components and APIs.

## Table of Contents

- [Decorators](#decorators)
- [Basic Components](#basic-components)
- [Layout Components](#layout-components)
- [Composite Components](#composite-components)
- [Renderers](#renderers)

## Decorators

### @page()

Marks a function as a page definition.

```python
@hs.page(
    path: str = "/",
    mode: Literal["web-prototype", "deck", "infographic"] = "web-prototype",
    design_system: Literal["huashu", "minimal", "custom"] = "huashu",
    brand: Optional[str] = None,
)
```

**Parameters:**
- `path`: URL path for the page (default: "/")
- `mode`: Output format (default: "web-prototype")
- `design_system`: Design constraints to apply (default: "huashu")
- `brand`: Optional brand name for the page

**Example:**
```python
@hs.page(mode="web-prototype", design_system="huashu", brand="MyApp")
def my_page():
    hs.heading("Hello")
```

### @component()

Registers a custom component.

```python
@hs.component(name: str)
```

**Parameters:**
- `name`: Unique name for the component

**Example:**
```python
@hs.component("custom-card")
def custom_card(title, content):
    with hs.card():
        hs.heading(title, level=3)
        hs.text(content)
```

## Basic Components

### heading()

Renders a heading element (H1-H6).

```python
hs.heading(
    text: str,
    level: int = 1,
    align: Literal["left", "center", "right"] = "left"
)
```

**Parameters:**
- `text`: Heading text content
- `level`: Heading level 1-6 (default: 1)
- `align`: Text alignment (default: "left")

**Example:**
```python
hs.heading("Welcome", level=1)
hs.heading("Section Title", level=2, align="center")
```

### text()

Renders a paragraph of text.

```python
hs.text(
    content: str,
    size: Literal["small", "medium", "large"] = "medium",
    color: Optional[str] = None,
    align: Literal["left", "center", "right"] = "left"
)
```

**Parameters:**
- `content`: Text content
- `size`: Font size preset (default: "medium")
- `color`: Text color (CSS color value)
- `align`: Text alignment (default: "left")

**Example:**
```python
hs.text("This is a paragraph.", size="large")
hs.text("Subtitle text", color="#666", align="center")
```

### button()

Renders a button element.

```python
hs.button(
    text: str,
    style: Literal["primary", "secondary", "outline"] = "primary",
    size: Literal["small", "medium", "large"] = "medium",
    href: Optional[str] = None
)
```

**Parameters:**
- `text`: Button label
- `style`: Button style variant (default: "primary")
- `size`: Button size (default: "medium")
- `href`: Optional link URL

**Example:**
```python
hs.button("Click me", style="primary", size="large")
hs.button("Learn More", style="secondary", href="/docs")
```

### image()

Renders an image element.

```python
hs.image(
    src: str,
    alt: str,
    width: Optional[str] = None,
    height: Optional[str] = None
)
```

**Parameters:**
- `src`: Image source URL or path
- `alt`: Alternative text for accessibility
- `width`: Optional width (CSS value)
- `height`: Optional height (CSS value)

**Example:**
```python
hs.image("photo.jpg", alt="Product photo")
hs.image("logo.png", alt="Logo", width="200px")
```

### spacer()

Adds vertical spacing.

```python
hs.spacer(height: str = "16px")
```

**Parameters:**
- `height`: Spacing height (CSS value, default: "16px")

**Example:**
```python
hs.spacer(height="32px")
hs.spacer(height="64px")
```

### divider()

Renders a horizontal divider line.

```python
hs.divider(
    thickness: str = "1px",
    color: str = "#e0e0e0"
)
```

**Parameters:**
- `thickness`: Line thickness (CSS value, default: "1px")
- `color`: Line color (CSS color, default: "#e0e0e0")

**Example:**
```python
hs.divider()
hs.divider(thickness="2px", color="#667eea")
```

## Layout Components

Layout components use context managers (`with` statements) for nested content.

### container()

Centers content with a maximum width.

```python
with hs.container(max_width: str = "1200px"):
    # Content here
```

**Parameters:**
- `max_width`: Maximum container width (CSS value, default: "1200px")

**Example:**
```python
with hs.container(max_width="800px"):
    hs.heading("Centered Content")
    hs.text("This content is centered with a max width.")
```

### grid()

Creates a responsive grid layout.

```python
with hs.grid(
    columns: int = 2,
    gap: str = "24px"
):
    # Grid items here
```

**Parameters:**
- `columns`: Number of columns (default: 2)
- `gap`: Gap between grid items (CSS value, default: "24px")

**Example:**
```python
with hs.grid(columns=3, gap="32px"):
    hs.text("Column 1")
    hs.text("Column 2")
    hs.text("Column 3")
```

### section()

Creates a section with padding.

```python
with hs.section(padding: str = "80px 0"):
    # Section content here
```

**Parameters:**
- `padding`: Section padding (CSS value, default: "80px 0")

**Example:**
```python
with hs.section(padding="120px 0"):
    hs.heading("Section Title", align="center")
    hs.text("Section content")
```

## Composite Components

### hero()

Creates a hero section (typically at the top of a page).

```python
with hs.hero(
    background: str = "gradient",
    gradient: Optional[str] = None
):
    # Hero content here
```

**Parameters:**
- `background`: Background style ("gradient", color value)
- `gradient`: Gradient preset ("blue", "purple", etc.)

**Example:**
```python
with hs.hero(gradient="blue"):
    hs.heading("Welcome to Our Site", level=1)
    hs.text("Build amazing things with Python")
    hs.button("Get Started", style="primary")
```

### features()

Renders a feature grid.

```python
hs.features(
    items: List[Dict[str, str]],
    columns: int = 3
)
```

**Parameters:**
- `items`: List of feature dictionaries with `icon`, `title`, `description`
- `columns`: Number of columns (default: 3)

**Example:**
```python
hs.features(items=[
    {
        "icon": "⚡",
        "title": "Fast",
        "description": "Lightning-fast performance"
    },
    {
        "icon": "🎨",
        "title": "Beautiful",
        "description": "Professional design out of the box"
    },
])
```

### cta()

Creates a call-to-action section.

```python
with hs.cta(background: str = "#667eea"):
    # CTA content here
```

**Parameters:**
- `background`: Background color or gradient (CSS value)

**Example:**
```python
with hs.cta(background="linear-gradient(135deg, #667eea 0%, #764ba2 100%)"):
    hs.heading("Ready to Start?", level=2)
    hs.button("Sign Up Now", style="primary")
```

### navbar()

Renders a navigation bar.

```python
hs.navbar(
    logo: Optional[str] = None,
    links: Optional[List[str]] = None
)
```

**Parameters:**
- `logo`: Logo image URL (optional)
- `links`: List of navigation link labels (optional)

**Example:**
```python
hs.navbar(
    logo="logo.png",
    links=["Home", "Features", "Pricing", "Contact"]
)
```

### footer()

Renders a footer section.

```python
hs.footer(
    copyright: Optional[str] = None,
    links: Optional[List[str]] = None
)
```

**Parameters:**
- `copyright`: Copyright text (optional)
- `links`: List of footer link labels (optional)

**Example:**
```python
hs.footer(
    copyright="© 2026 MyCompany. All rights reserved.",
    links=["Privacy", "Terms", "Contact"]
)
```

### card()

Creates a card container.

```python
with hs.card(title: Optional[str] = None):
    # Card content here
```

**Parameters:**
- `title`: Optional card title

**Example:**
```python
with hs.card(title="Feature Card"):
    hs.text("Card content goes here")
    hs.button("Learn More")
```

## Renderers

### WebPrototypeRenderer

Renders pages in web prototype mode.

```python
from htmlskill.renderers.web import WebPrototypeRenderer

renderer = WebPrototypeRenderer()
html = renderer.render(context)
```

**Methods:**
- `render(context: RenderContext) -> str`: Renders context to HTML string

**Example:**
```python
from htmlskill.renderers.web import WebPrototypeRenderer

@hs.page(mode="web-prototype")
def my_page():
    hs.heading("Hello")

ctx = my_page()
renderer = WebPrototypeRenderer()
html = renderer.render(ctx)
```

## Design Systems

### huashu (default)

Professional design system with:
- 8px baseline grid
- WCAG AA compliant colors
- CJK font optimization
- Mobile-first responsive design

### minimal

Simplified design system for clean, minimal pages.

### custom

Allows full control over styling.

## Type Hints

HTMLskill includes full type hints for IDE autocomplete:

```python
import htmlskill as hs

# Your IDE will provide autocomplete for all parameters
hs.heading("Title", level=1, align="center")
```

## Thread Safety

All HTMLskill APIs are thread-safe and can be used in web frameworks:

```python
from flask import Flask
import htmlskill as hs

app = Flask(__name__)

@app.route("/")
def index():
    @hs.page(mode="web-prototype")
    def page():
        hs.heading("Hello from Flask")

    ctx = page()
    # ... render context
```
