# HTMLskill Documentation

Welcome to HTMLskill documentation!

## Quick Links

- [Getting Started](getting-started.md)
- [API Reference](api-reference.md)
- [Examples](../examples/README.md)
- [Contributing](../CONTRIBUTING.md)

## Overview

HTMLskill is a Python-first HTML generation framework that combines the simplicity of Python with professional design systems.

## Key Concepts

### 1. Decorators

Use `@hs.page()` to define pages and `@hs.component()` for custom components.

```python
import htmlskill as hs

@hs.page(mode="web-prototype", design_system="huashu")
def my_page():
    hs.heading("Hello World")
```

### 2. Context Managers

Use `with` statements for nested layouts:

```python
with hs.hero(gradient="blue"):
    hs.heading("Title")
    hs.text("Description")
```

### 3. Design System

Built-in design constraints ensure professional output:
- 8px baseline grid for consistent spacing
- WCAG AA compliant colors for accessibility
- CJK font optimization for Chinese/Japanese/Korean
- Mobile-first responsive breakpoints

### 4. Output Modes

Generate different HTML structures from the same code:
- `web-prototype`: Landing pages and blogs
- `deck`: Presentation slides
- `email`: Email campaigns
- More coming soon!

## Architecture

```
Your Python Code
       ↓
HTMLskill API (@page, components)
       ↓
Design System (8px grid, WCAG AA)
       ↓
Template Renderer (Jinja2)
       ↓
HTML Output
```

## Learning Path

1. **Start Simple**: Run `examples/00-minimal.py`
2. **Explore Components**: Check `examples/04-complete-with-output.py`
3. **Build Real Pages**: Study `examples/05-product-landing.py`
4. **Read API Docs**: Understand all available components
5. **Create Your Own**: Start building!

## Next Steps

- [Getting Started Guide](getting-started.md)
- [Component Library](api-reference.md)
- [Best Practices](best-practices.md)
- [FAQ](faq.md)
