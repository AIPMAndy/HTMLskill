# HTMLSkill - Python-first HTML Generation Framework

> **Status**: 🚧 Alpha - Phase 1 MVP in development

A Python-first HTML generation framework that combines:
- **Mesop-style API** - Declarative Python decorators and components
- **huashu-design system** - Professional design constraints (8px grid, WCAG AA contrast, CJK fonts)
- **html-anything templates** - 9 output modes (web, deck, poster, social cards, etc.)

## Quick Start

```python
import htmlskill as hs

@hs.page(mode="web-prototype", design_system="huashu")
def landing_page():
    hs.heading("Welcome to HTMLSkill", level=1)
    hs.text("Build professional HTML with Python", size="large")
    hs.button("Get Started", style="primary")

# Generate single-file HTML
ctx = landing_page()
# (Rendering engine coming in next commits)
```

## Features (Phase 1 MVP)

- ✅ **Python API** - `@page` and `@component` decorators
- ✅ **Basic Components** - heading, text, button, image, spacer, divider
- 🚧 **Layout Components** - container, grid, section (in progress)
- 🚧 **Composite Components** - hero, features, cta, navbar, footer (in progress)
- 🚧 **3 Output Modes** - web-prototype, deck, infographic (in progress)
- 🚧 **Design Constraints** - 8px grid, contrast checking (in progress)
- 🚧 **HTML Export** - Single-file with inlined assets (in progress)

## Installation

```bash
# Clone the repository
git clone https://github.com/AIPMAndy/python-html-designer.git
cd python-html-designer

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

## Roadmap

### Phase 1: MVP (Current - 2-3 weeks)
- Core Python API ✅
- Basic components ✅
- 3 output modes 🚧
- HTML rendering 🚧

### Phase 2: Design System (1-2 weeks)
- huashu-design asset protocol
- 5-dimension expert review
- Anti AI-slop rules

### Phase 3: Templates & Export (2-3 weeks)
- 9 output modes
- 75+ templates
- Multi-format export (PDF/PNG/MP4/GIF/PPTX)

## Architecture

```
User Python Code
    ↓
@page decorator → RenderContext
    ↓
Components → Add to context
    ↓
Renderer → Jinja2 templates
    ↓
Single-file HTML output
```

## Tech Stack

- Python 3.10+
- Jinja2 (templates)
- Tailwind CSS (styling)
- Playwright (validation)
- Click (CLI)

## Development

```bash
# Run tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=htmlskill --cov-report=html

# Format code
black htmlskill/ tests/

# Lint
flake8 htmlskill/ tests/
```

## License

MIT License - see [LICENSE](LICENSE) for details

## Author

**Andy** - [@AIPMAndy](https://github.com/AIPMAndy)

Inspired by:
- [Mesop](https://github.com/google/mesop) - Python UI framework
- [huashu-design](https://github.com/alchaincyf/huashu-design) - Design system
- [html-anything](https://github.com/nexu-io/html-anything) - Multi-template HTML generator

---

**Note**: This project is in active development. APIs may change before v1.0.0 release.
