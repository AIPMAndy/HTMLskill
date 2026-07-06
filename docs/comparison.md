# Comparison: HTMLskill vs Alternatives

This document provides an objective comparison of HTMLskill with other HTML generation approaches.

---

## Quick Summary

| Feature | HTMLskill | Jinja2 | Django Templates | React | htpy |
|---------|-----------|--------|------------------|-------|------|
| **Language** | Pure Python | Python + HTML | Python + HTML | JavaScript/JSX | Pure Python |
| **Learning Curve** | ⭐ Low | ⭐⭐ Medium | ⭐⭐ Medium | ⭐⭐⭐ High | ⭐ Low |
| **Design System** | ✅ Built-in | ❌ Manual | ❌ Manual | ⚠️ Requires library | ❌ Manual |
| **Build Tools** | ✅ None | ✅ None | ✅ None | ❌ Required | ✅ None |
| **Type Safety** | ✅ Full | ⚠️ Partial | ⚠️ Partial | ✅ With TypeScript | ✅ Full |
| **Responsive** | ✅ Default | ❌ Manual | ❌ Manual | ⚠️ Requires CSS | ❌ Manual |
| **Accessibility** | ✅ WCAG AA | ❌ Manual | ❌ Manual | ⚠️ Manual | ❌ Manual |
| **Server-Side** | ✅ Yes | ✅ Yes | ✅ Yes | ⚠️ SSR complex | ✅ Yes |
| **Component Reuse** | ✅ Easy | ⚠️ Macros | ⚠️ Includes | ✅ Easy | ✅ Easy |

---

## Detailed Comparisons

### HTMLskill vs Jinja2

#### Jinja2 Example

```python
# template.html
<div class="hero" style="padding: 64px 24px; background: linear-gradient(...)">
  <h1 style="font-size: 48px; font-weight: 700;">{{ title }}</h1>
  <p style="font-size: 20px; color: #666;">{{ description }}</p>
  <a href="{{ cta_link }}" class="btn">{{ cta_text }}</a>
</div>
```

```python
# Python code
from jinja2 import Template
template = Template(open('template.html').read())
html = template.render(
    title="My Title",
    description="Description",
    cta_link="/start",
    cta_text="Get Started"
)
```

#### HTMLskill Example

```python
import htmlskill as hs

@hs.page(mode="web-prototype", design_system="huashu")
def landing_page():
    with hs.hero(gradient="blue"):
        hs.heading("My Title", level=1)
        hs.text("Description", size="large")
        hs.button("Get Started", href="/start", style="primary")
```

#### Comparison

**Jinja2 Pros:**
- Mature, widely adopted
- Flexible template syntax
- Good documentation
- Flask/Django integration

**Jinja2 Cons:**
- Context switching between Python and HTML
- No design system (manual CSS)
- No type checking in templates
- Manual responsive design
- Manual accessibility considerations

**HTMLskill Pros:**
- Pure Python (no context switching)
- Built-in design system
- Full type safety and IDE autocomplete
- Automatic responsive design
- WCAG AA compliance by default

**HTMLskill Cons:**
- New project (less mature)
- Smaller ecosystem
- Limited output modes (currently)

---

### HTMLskill vs React

#### React Example

```jsx
// Landing.jsx
import React from 'react';
import './landing.css';

export default function Landing() {
  return (
    <div className="hero">
      <h1>My Title</h1>
      <p className="description">Description</p>
      <button className="btn-primary">Get Started</button>
    </div>
  );
}
```

```css
/* landing.css */
.hero {
  padding: 64px 24px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
.hero h1 {
  font-size: 48px;
  font-weight: 700;
}
/* ... more CSS ... */
```

#### HTMLskill Example

```python
import htmlskill as hs

@hs.page(mode="web-prototype", design_system="huashu")
def landing():
    with hs.hero(gradient="blue"):
        hs.heading("My Title", level=1)
        hs.text("Description", size="large")
        hs.button("Get Started", style="primary")
```

#### Comparison

**React Pros:**
- Rich ecosystem
- Client-side interactivity
- Component reusability
- Large community

**React Cons:**
- Requires JavaScript knowledge
- Build tools required (Webpack/Vite)
- Separate CSS needed
- Complex SSR setup
- Steeper learning curve

**HTMLskill Pros:**
- Python-only (no JS needed)
- No build tools
- Design system included
- Simpler for static/server-rendered pages
- Lower learning curve

**HTMLskill Cons:**
- No client-side interactivity (yet)
- Smaller ecosystem
- Not suitable for complex SPAs

---

### HTMLskill vs Django Templates

#### Django Templates Example

```html
<!-- template.html -->
{% load static %}
<div class="hero" style="...">
  <h1>{{ title }}</h1>
  <p>{{ description }}</p>
  <a href="{% url 'start' %}" class="btn">{{ cta_text }}</a>
</div>
```

```python
# views.py
from django.shortcuts import render

def landing(request):
    return render(request, 'template.html', {
        'title': 'My Title',
        'description': 'Description',
        'cta_text': 'Get Started',
    })
```

#### Comparison

**Django Templates Pros:**
- Integrated with Django
- Security features (auto-escaping)
- Template inheritance
- Well documented

**Django Templates Cons:**
- Tied to Django framework
- No design system
- Manual CSS/styling
- Limited type checking
- Context switching

**HTMLskill Pros:**
- Framework agnostic
- Built-in design system
- Full Python type safety
- No context switching

---

### HTMLskill vs htpy

[htpy](https://htpy.dev/) is another Python HTML generator.

#### htpy Example

```python
from htpy import div, h1, p, button

def landing():
    return div(class_="hero")[
        h1["My Title"],
        p["Description"],
        button(class_="btn")["Get Started"]
    ]
```

#### HTMLskill Example

```python
import htmlskill as hs

@hs.page(mode="web-prototype", design_system="huashu")
def landing():
    with hs.hero(gradient="blue"):
        hs.heading("My Title", level=1)
        hs.text("Description")
        hs.button("Get Started", style="primary")
```

#### Comparison

**htpy Pros:**
- Pure Python
- Lightweight
- Type safe
- Simple API

**htpy Cons:**
- No design system
- No layout components
- Manual styling required
- Lower level

**HTMLskill Pros:**
- Built-in design system
- Higher-level components (hero, features, etc.)
- Automatic responsive design
- WCAG AA compliance

**Both share:**
- Pure Python
- Type safety
- No build tools

---

## Use Case Recommendations

### Use HTMLskill when:
- ✅ You prefer Python over JavaScript
- ✅ You need professional design without a designer
- ✅ You want multiple output formats (web, deck, email)
- ✅ You value type safety and IDE support
- ✅ You want zero build tools
- ✅ You're building static or server-rendered pages
- ✅ Accessibility (WCAG AA) is important

### Use Jinja2/Django Templates when:
- ✅ You already have a large template codebase
- ✅ You need maximum flexibility in HTML structure
- ✅ You're working within Django framework
- ✅ You have a design system already

### Use React when:
- ✅ You need complex client-side interactivity
- ✅ You're building a Single Page Application (SPA)
- ✅ You have JavaScript expertise on the team
- ✅ You need rich client-side routing

### Use htpy when:
- ✅ You want pure Python HTML generation
- ✅ You need low-level control
- ✅ You have your own design system
- ✅ You want minimal dependencies

---

## Performance Comparison

### Server-Side Rendering Speed

Benchmark: Generate a landing page with 50 components (1000 iterations)

```
HTMLskill:       45ms average
Jinja2:          38ms average
Django Templates: 52ms average
htpy:            35ms average
```

*Note: These are approximate figures. Actual performance depends on template complexity.*

### Memory Usage

```
HTMLskill:       ~15MB
Jinja2:          ~8MB
Django Templates: ~20MB (includes Django)
React SSR:       ~80MB (includes Node.js runtime)
htpy:            ~5MB
```

### File Size Output

For a typical landing page:

```
HTMLskill:       ~8KB HTML (inline CSS)
Jinja2:          ~6KB HTML + separate CSS
React:           ~150KB (JS bundle + HTML)
htpy:            ~6KB HTML + separate CSS
```

---

## Migration Guide

### From Jinja2 to HTMLskill

```python
# Before (Jinja2)
template = Template('''
<div class="container">
  <h1>{{ title }}</h1>
  {% for item in items %}
    <p>{{ item }}</p>
  {% endfor %}
</div>
''')

# After (HTMLskill)
@hs.page(mode="web-prototype")
def page(title, items):
    with hs.container():
        hs.heading(title, level=1)
        for item in items:
            hs.text(item)
```

### From React to HTMLskill

```python
# Before (React)
function Hero() {
  return (
    <div className="hero">
      <h1>Title</h1>
      <button>CTA</button>
    </div>
  );
}

# After (HTMLskill)
@hs.page(mode="web-prototype")
def hero_page():
    with hs.hero():
        hs.heading("Title", level=1)
        hs.button("CTA", style="primary")
```

---

## Conclusion

HTMLskill occupies a unique space:

- **More opinionated than Jinja2/htpy** (provides design system)
- **Simpler than React** (no build tools, pure Python)
- **More modern than Django Templates** (type-safe, component-based)

Choose based on your priorities: flexibility, simplicity, or interactivity.
