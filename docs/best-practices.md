# Best Practices

Guidelines for writing clean, maintainable HTMLskill code.

---

## Code Organization

### Structure Your Project

```
my_project/
├── pages/
│   ├── __init__.py
│   ├── home.py
│   ├── about.py
│   └── contact.py
├── components/
│   ├── __init__.py
│   ├── cards.py
│   └── forms.py
├── utils/
│   ├── __init__.py
│   └── renderer.py
├── output/
│   └── (generated HTML files)
└── main.py
```

### Separate Pages into Modules

```python
# pages/home.py
import htmlskill as hs

@hs.page(mode="web-prototype", design_system="huashu", brand="MyApp")
def home_page():
    """Home page with hero and features."""
    with hs.hero(gradient="blue"):
        hs.heading("Welcome to MyApp", level=1)
        hs.text("Build amazing things")
    
    with hs.section(padding="80px 0"):
        hs.features(items=[...])
```

```python
# main.py
from pages.home import home_page
from utils.renderer import save_page

if __name__ == "__main__":
    save_page(home_page(), "output/index.html")
```

---

## Component Design

### Create Reusable Components

```python
# components/cards.py
import htmlskill as hs

@hs.component("feature-card")
def feature_card(icon: str, title: str, description: str):
    """Reusable feature card component."""
    with hs.card():
        hs.text(icon, size="large")
        hs.heading(title, level=3)
        hs.text(description, color="#666")

@hs.component("pricing-card")
def pricing_card(plan: str, price: float, features: list[str], highlighted: bool = False):
    """Pricing card with optional highlight."""
    with hs.card():
        hs.heading(plan, level=3)
        hs.text(f"${price}/month", size="large")
        hs.spacer(height="16px")
        for feature in features:
            hs.text(f"✓ {feature}", size="small")
        hs.spacer(height="24px")
        hs.button(
            "Choose Plan",
            style="primary" if highlighted else "secondary"
        )
```

### Use Type Hints

```python
from typing import List, Optional
import htmlskill as hs

@hs.component("blog-post-card")
def blog_post_card(
    title: str,
    excerpt: str,
    author: str,
    date: str,
    image_url: Optional[str] = None,
    tags: Optional[List[str]] = None
) -> None:
    """Blog post card with optional image and tags."""
    with hs.card():
        if image_url:
            hs.image(image_url, alt=title)
            hs.spacer(height="16px")
        
        hs.heading(title, level=3)
        hs.text(excerpt, color="#666")
        hs.spacer(height="16px")
        hs.text(f"By {author} • {date}", size="small", color="#999")
        
        if tags:
            hs.spacer(height="8px")
            for tag in tags:
                hs.text(f"#{tag}", size="small", color="#667eea")
```

---

## Data Handling

### Pass Data as Parameters

```python
# ✅ Good - explicit data passing
@hs.page(mode="web-prototype")
def product_page(product: dict):
    hs.heading(product["name"], level=1)
    hs.text(product["description"])
    hs.text(f"${product['price']}", size="large")

# ❌ Bad - accessing global data
PRODUCT = {...}

@hs.page(mode="web-prototype")
def product_page():
    hs.heading(PRODUCT["name"], level=1)  # Harder to test and reuse
```

### Validate Input Data

```python
from dataclasses import dataclass
from typing import List

@dataclass
class Product:
    name: str
    description: str
    price: float
    features: List[str]
    
    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price must be positive")
        if not self.name:
            raise ValueError("Name is required")

@hs.page(mode="web-prototype")
def product_page(product: Product):
    """Type-safe product page."""
    hs.heading(product.name, level=1)
    hs.text(product.description)
    hs.text(f"${product.price:.2f}", size="large")
    
    for feature in product.features:
        hs.text(f"• {feature}")
```

### Sanitize User Input

```python
import html
from typing import Optional

def safe_text(content: str, allow_html: bool = False) -> None:
    """Safely render text content."""
    if not allow_html:
        content = html.escape(content)
    hs.text(content)

@hs.page(mode="web-prototype")
def user_profile(username: str, bio: Optional[str] = None):
    """User profile page with safe rendering."""
    safe_text(username)  # Escapes HTML
    
    if bio:
        safe_text(bio)
```

---

## Performance Optimization

### Cache Rendered Pages

```python
from functools import lru_cache
from htmlskill.renderers.web import WebPrototypeRenderer

renderer = WebPrototypeRenderer()

@lru_cache(maxsize=100)
def render_static_page(page_name: str) -> str:
    """Cache rendered static pages."""
    @hs.page(mode="web-prototype")
    def page():
        # ... page content ...
        pass
    
    ctx = page()
    return renderer.render(ctx)

# First call: renders and caches
html = render_static_page("about")

# Second call: returns cached version
html = render_static_page("about")  # Instant!
```

### Lazy Load Components

```python
@hs.page(mode="web-prototype")
def large_page(include_analytics: bool = False):
    """Only include analytics when needed."""
    hs.heading("Page Title")
    hs.text("Content")
    
    # Conditional expensive operations
    if include_analytics:
        generate_analytics_section()  # Only when needed

def generate_analytics_section():
    """Expensive component - only call when needed."""
    # Complex data processing
    data = process_analytics_data()
    
    with hs.section(padding="40px 0"):
        for item in data:
            hs.text(item)
```

### Batch Rendering

```python
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

def render_all_pages(pages: list[str], output_dir: Path):
    """Render multiple pages in parallel."""
    
    def render_page(page_name: str):
        ctx = generate_page(page_name)
        html = renderer.render(ctx)
        output_file = output_dir / f"{page_name}.html"
        output_file.write_text(html)
        return page_name
    
    with ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(render_page, pages))
    
    print(f"Rendered {len(results)} pages")
```

---

## Accessibility

### Use Semantic Headings

```python
# ✅ Good - proper heading hierarchy
@hs.page(mode="web-prototype")
def article():
    hs.heading("Article Title", level=1)  # Page title
    
    with hs.section():
        hs.heading("Introduction", level=2)  # Section title
        hs.text("...")
        
        hs.heading("Subsection", level=3)  # Subsection
        hs.text("...")

# ❌ Bad - skipping levels
@hs.page(mode="web-prototype")
def article():
    hs.heading("Article Title", level=1)
    hs.heading("Subsection", level=4)  # Skipped 2 and 3!
```

### Always Include Alt Text

```python
# ✅ Good - descriptive alt text
hs.image("product.jpg", alt="Red bicycle with basket")

# ❌ Bad - missing or generic alt text
hs.image("product.jpg", alt="")
hs.image("product.jpg", alt="image")
```

### Use Descriptive Link Text

```python
# ✅ Good - descriptive
hs.button("Read the full documentation", href="/docs")

# ❌ Bad - generic
hs.button("Click here", href="/docs")
```

---

## Testing

### Test Page Generation

```python
import pytest
from htmlskill.renderers.web import WebPrototypeRenderer

def test_home_page_renders():
    """Test that home page renders without errors."""
    ctx = home_page()
    renderer = WebPrototypeRenderer()
    html = renderer.render(ctx)
    
    assert html
    assert "<h1>" in html
    assert "Welcome" in html

def test_product_page_with_data():
    """Test product page with sample data."""
    product = Product(
        name="Widget",
        description="A great widget",
        price=29.99,
        features=["Fast", "Reliable"]
    )
    
    ctx = product_page(product)
    renderer = WebPrototypeRenderer()
    html = renderer.render(ctx)
    
    assert "Widget" in html
    assert "$29.99" in html
    assert "Fast" in html
```

### Test Components

```python
def test_feature_card():
    """Test feature card component."""
    @hs.page(mode="web-prototype")
    def test_page():
        feature_card("⚡", "Fast", "Very fast performance")
    
    ctx = test_page()
    assert len(ctx.components) > 0
    
    # Check card content
    renderer = WebPrototypeRenderer()
    html = renderer.render(ctx)
    assert "⚡" in html
    assert "Fast" in html
```

---

## Error Handling

### Graceful Fallbacks

```python
from typing import Optional

@hs.page(mode="web-prototype")
def safe_page(data: Optional[dict] = None):
    """Page with fallback for missing data."""
    if data is None:
        hs.heading("No Data Available", level=1)
        hs.text("Please try again later.")
        return
    
    hs.heading(data.get("title", "Untitled"), level=1)
    hs.text(data.get("content", "No content available"))
```

### Log Errors

```python
import logging

logger = logging.getLogger(__name__)

def render_page_safe(page_func, output_path: Path) -> bool:
    """Render page with error handling."""
    try:
        ctx = page_func()
        renderer = WebPrototypeRenderer()
        html = renderer.render(ctx)
        output_path.write_text(html)
        logger.info(f"Rendered: {output_path}")
        return True
    except Exception as e:
        logger.error(f"Failed to render {page_func.__name__}: {e}")
        return False
```

---

## Styling Conventions

### Consistent Spacing

```python
# ✅ Good - consistent spacing pattern
@hs.page(mode="web-prototype")
def page():
    hs.heading("Section 1", level=2)
    hs.spacer(height="24px")
    hs.text("Content")
    hs.spacer(height="48px")
    
    hs.heading("Section 2", level=2)
    hs.spacer(height="24px")
    hs.text("Content")

# ❌ Bad - inconsistent spacing
@hs.page(mode="web-prototype")
def page():
    hs.heading("Section 1", level=2)
    hs.spacer(height="17px")  # Random value
    hs.text("Content")
    hs.spacer(height="93px")  # Random value
```

### Use Design System Values

```python
# ✅ Good - multiples of 8px (design system grid)
hs.spacer(height="16px")  # 8px × 2
hs.spacer(height="32px")  # 8px × 4
hs.spacer(height="64px")  # 8px × 8

# ❌ Bad - arbitrary values
hs.spacer(height="17px")
hs.spacer(height="23px")
```

---

## Common Pitfalls

### Don't Call Components Outside Page

```python
# ❌ Wrong - components outside page function
hs.heading("This won't work")

@hs.page(mode="web-prototype")
def page():
    pass

# ✅ Correct - components inside page function
@hs.page(mode="web-prototype")
def page():
    hs.heading("This works!")
```

### Don't Forget to Render

```python
# ❌ Wrong - returns context, not HTML
def generate_page():
    @hs.page(mode="web-prototype")
    def page():
        hs.heading("Hello")
    return page()  # Returns context object

# ✅ Correct - render to HTML
def generate_page():
    @hs.page(mode="web-prototype")
    def page():
        hs.heading("Hello")
    
    ctx = page()
    renderer = WebPrototypeRenderer()
    return renderer.render(ctx)  # Returns HTML string
```

### Close Context Managers

```python
# ❌ Wrong - missing context manager
@hs.page(mode="web-prototype")
def page():
    hs.hero()  # Missing 'with'
    hs.heading("Title")

# ✅ Correct - use 'with' statement
@hs.page(mode="web-prototype")
def page():
    with hs.hero():
        hs.heading("Title")
```

---

## Documentation

### Document Your Components

```python
@hs.component("author-bio")
def author_bio(name: str, bio: str, avatar_url: str) -> None:
    """
    Author biography component.
    
    Args:
        name: Author's full name
        bio: Short biography (max 200 chars)
        avatar_url: URL to author's profile picture
    
    Example:
        >>> author_bio(
        ...     name="Jane Doe",
        ...     bio="Software engineer and writer",
        ...     avatar_url="https://example.com/jane.jpg"
        ... )
    """
    with hs.card():
        hs.image(avatar_url, alt=f"{name}'s avatar")
        hs.heading(name, level=3)
        hs.text(bio, size="small")
```

### Add Page Metadata

```python
@hs.page(
    mode="web-prototype",
    design_system="huashu",
    brand="MyApp"
)
def landing_page():
    """
    Main landing page for MyApp.
    
    Features:
    - Hero section with CTA
    - Feature showcase (3 columns)
    - Social proof section
    - Final CTA
    
    Last updated: 2026-07-06
    """
    # ... implementation ...
```

---

## Deployment

### Environment-Specific Configuration

```python
import os

def get_config():
    """Get environment-specific configuration."""
    env = os.getenv("ENV", "development")
    
    return {
        "development": {
            "brand": "MyApp (Dev)",
            "analytics": False,
        },
        "production": {
            "brand": "MyApp",
            "analytics": True,
        }
    }[env]

@hs.page(mode="web-prototype", **get_config())
def page():
    # ... page content ...
    pass
```

### Build Script

```python
#!/usr/bin/env python3
"""Build script for generating all HTML pages."""

from pathlib import Path
from pages import home, about, contact
from htmlskill.renderers.web import WebPrototypeRenderer

def build_site(output_dir: Path):
    """Generate all pages."""
    output_dir.mkdir(exist_ok=True)
    renderer = WebPrototypeRenderer()
    
    pages = [
        ("index.html", home.home_page),
        ("about.html", about.about_page),
        ("contact.html", contact.contact_page),
    ]
    
    for filename, page_func in pages:
        ctx = page_func()
        html = renderer.render(ctx)
        (output_dir / filename).write_text(html)
        print(f"✅ Generated {filename}")

if __name__ == "__main__":
    build_site(Path("dist"))
```

---

## Summary

**Key Principles:**
1. ✅ Organize code into modules
2. ✅ Use type hints for clarity
3. ✅ Sanitize user input
4. ✅ Cache for performance
5. ✅ Follow accessibility guidelines
6. ✅ Test your pages
7. ✅ Document components
8. ✅ Use consistent spacing

Following these practices will help you build maintainable, performant, and accessible HTMLskill applications.
