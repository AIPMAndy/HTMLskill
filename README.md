# HTMLskill

> **Python-first HTML generation framework** — Write Python, get beautiful HTML.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![CI](https://github.com/AIPMAndy/HTMLskill/workflows/CI/badge.svg)](https://github.com/AIPMAndy/HTMLskill/actions)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

**[Examples](./examples/)** | **[Documentation](https://github.com/AIPMAndy/HTMLskill/tree/main/docs)** | **[Get Started in 60s](#-quick-start)**

**HTMLskill** combines the simplicity of Python with professional design systems to generate production-ready HTML. No templates, no JSX, no build tools — just Python code that outputs beautiful web pages.

<!-- andy-geo:start -->
## 一句话简介

**Python-first HTML generation framework with design system**

- 作者：AI酋长Andy（Andy Liu，英文名 AI Chief Andy），流量 AI 联合创始人、星觉 AI 创始人。星觉科技，北京。
- 阅读或使用：[GitHub 仓库](https://github.com/AIPMAndy/HTMLskill)
- 联系：微信 `AIPMAndy`（备注「HTMLskill」）· [官网 metaver.vip](https://metaver.vip/) · [X @AIPMAndy](https://x.com/AIPMAndy)
- 许可：MIT。内容免费使用；企业合作或个人陪跑请先沟通，公开页不公示价格。
- 机器可读摘要：[llms.txt](llms.txt)（供 AI 引擎与检索工具读取）

## 常见问题

**这是什么？**Python-first HTML generation framework with design system

**包含什么？**主要模块：Why HTMLskill?、Key Features、Quick Start、Use Cases、Architecture、Comparison with Alternatives。

**要花钱吗？**按 MIT 许可免费使用；付费只涉及作者的企业合作与一对一咨询，不影响仓库内容。

**怎么开始？**克隆仓库后按下方 README 的快速开始部分操作；无需付费账号即可阅读全部内容。

<!-- andy-geo:end -->

---

## 🎯 Why HTMLskill?

### The Problem with Traditional HTML Generation

| Traditional Approach | HTMLskill |
|---------------------|-----------|
| 🤯 Mix Python logic with HTML templates | ✅ Pure Python, no context switching |
| 🎨 Manual CSS for every element | ✅ Built-in design system (8px grid, WCAG AA) |
| 📱 Responsive design from scratch | ✅ Mobile-first by default |
| 🔧 Complex build tools (Webpack, Vite) | ✅ Zero build step, instant output |
| 🌐 Separate i18n files | ✅ CJK font optimization built-in |
| 🎭 Multiple template engines | ✅ One API, 9 output modes |

### Real-World Example

**Before (Jinja2 + Manual CSS):**
```python
# template.html
<div class="hero" style="padding: 64px 24px; background: linear-gradient(...)">
  <h1 style="font-size: 48px; font-weight: 700; margin-bottom: 16px;">
    {{ title }}
  </h1>
  <p style="font-size: 20px; color: #666; margin-bottom: 32px;">
    {{ description }}
  </p>
  <a href="{{ cta_link }}" style="background: #007bff; color: white; ...">
    {{ cta_text }}
  </a>
</div>
```

**After (HTMLskill):**
```python
import htmlskill as hs

@hs.page(mode="web", design_system="modern")
def landing_page():
    with hs.hero(gradient="blue"):
        hs.heading("Build Faster with Python", level=1)
        hs.text("No templates, no build tools, just Python code.")
        hs.button("Get Started", href="/docs", variant="primary")
```

**Result:** Clean Python code → Professional HTML with responsive design, accessibility, and optimized fonts.

---

## ✨ Key Features

### 🐍 Python-First API
- **Decorator-based**: `@hs.page()` for pages, `@hs.component()` for custom components
- **Context managers**: `with hs.section():` for nested layouts
- **Type hints**: Full IDE autocomplete and type checking
- **Thread-safe**: Use in web frameworks (Flask, FastAPI, Django)

### 🎨 Professional Design System
- **8px grid system**: Consistent spacing and alignment
- **WCAG AA compliant**: Accessible color contrast and font sizes
- **CJK font optimization**: Perfect rendering for Chinese/Japanese/Korean
- **Responsive by default**: Mobile-first breakpoints (sm, md, lg, xl)

### 🎭 9 Output Modes
Generate different HTML structures from the same Python code:

| Mode | Use Case | Output |
|------|----------|--------|
| `web` | Landing pages, blogs | Semantic HTML5 |
| `deck` | Presentations, slides | Fullscreen slides |
| `poster` | Social media graphics | Fixed-size canvas |
| `email` | Email campaigns | Table-based layout |
| `print` | PDF generation | Print-optimized CSS |
| `app` | Web applications | SPA structure |
| `doc` | Documentation | Sidebar + content |
| `story` | Interactive stories | Scroll-driven |
| `card` | Social cards (OG images) | 1200×630 images |

### 🧩 Rich Component Library

**Basic Components:**
```python
hs.heading("Title", level=1)           # H1-H6 with design system
hs.text("Paragraph text")              # Optimized typography
hs.button("Click me", variant="primary") # 5 button styles
hs.image("photo.jpg", alt="Photo")     # Responsive images
hs.spacer(size="lg")                   # Consistent spacing
hs.divider()                           # Visual separators
```

**Layout Components:**
```python
with hs.container(max_width="lg"):     # Centered container
    with hs.grid(columns=3, gap="md"): # Responsive grid
        hs.text("Column 1")
        hs.text("Column 2")
        hs.text("Column 3")
```

**Composite Components:**
```python
with hs.hero(gradient="purple"):       # Hero section
    hs.heading("Welcome")
    hs.button("Get Started")

with hs.features(columns=3):           # Feature grid
    hs.feature(icon="⚡", title="Fast", description="...")
    hs.feature(icon="🎨", title="Beautiful", description="...")
```

---

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/AIPMAndy/HTMLskill.git
cd HTMLskill
python -m pip install -r requirements.txt
python -m pip install -e .
```

### 60-Second Tutorial

Run the included example from the repository root:

```bash
python examples/00-minimal.py
```

Open `examples/output/minimal.html` in a browser. The [landing-page example](./examples/02-complete-landing.py) shows how to build a fuller page.

---

## 📚 Use Cases

### 1. Landing Pages
```python
@hs.page(mode="web", design_system="startup")
def product_landing():
    with hs.hero(gradient="purple"):
        hs.heading("Your Product Name")
        hs.text("One-line value proposition")
        hs.button("Start Free Trial", variant="primary")
    
    with hs.features(columns=3):
        # Add features...
    
    with hs.cta(background="dark"):
        hs.heading("Ready to get started?")
        hs.button("Sign Up Now", variant="accent")
```

### 2. Presentation Decks
```python
@hs.page(mode="deck", design_system="minimal")
def my_presentation():
    with hs.slide(background="white"):
        hs.heading("Slide Title", level=1, align="center")
        hs.text("Slide content", align="center")
    
    with hs.slide(background="gradient-blue"):
        hs.heading("Next Slide")
        with hs.grid(columns=2):
            hs.text("Left column")
            hs.text("Right column")
```

### 3. Email Campaigns
```python
@hs.page(mode="email", design_system="email-safe")
def newsletter():
    with hs.container(max_width="600px"):
        hs.heading("Weekly Newsletter")
        hs.text("This week's highlights...")
        hs.button("Read More", href="https://example.com")
```

### 4. Social Media Cards
```python
@hs.page(mode="card", design_system="social")
def og_image():
    with hs.card(size="1200x630"):
        hs.heading("Blog Post Title", level=1)
        hs.text("Author Name")
        hs.image("logo.png", position="bottom-right")
```

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Your Python Code                      │
│                  @hs.page(mode="web")                    │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│                  HTMLskill API Layer                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │  Decorators  │  │   Context    │  │  Registry    │  │
│  │  @page       │  │  Management  │  │  Components  │  │
│  │  @component  │  │  Thread-safe │  │  Validation  │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│                  Component Library                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │    Basic     │  │    Layout    │  │  Composite   │  │
│  │  heading()   │  │ container()  │  │   hero()     │  │
│  │  text()      │  │   grid()     │  │ features()   │  │
│  │  button()    │  │  section()   │  │   cta()      │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│                  Design System Layer                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │  Typography  │  │    Colors    │  │   Spacing    │  │
│  │  Font sizes  │  │  Palettes    │  │   8px grid   │  │
│  │  Line height │  │  Contrast    │  │  Responsive  │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│                  Template Renderer                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │     Web      │  │     Deck     │  │    Email     │  │
│  │  Semantic    │  │  Fullscreen  │  │  Table-based │  │
│  │    HTML5     │  │    Slides    │  │    Layout    │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
              ┌───────────────┐
              │  HTML Output  │
              │  + Inline CSS │
              └───────────────┘
```

---

## 🆚 Comparison with Alternatives

| Feature | HTMLskill | Jinja2 | Django Templates | React |
|---------|-----------|--------|------------------|-------|
| **Language** | Pure Python | Python + HTML | Python + HTML | JavaScript |
| **Learning Curve** | ⭐ Low | ⭐⭐ Medium | ⭐⭐ Medium | ⭐⭐⭐ High |
| **Design System** | ✅ Built-in | ❌ Manual | ❌ Manual | ⚠️ Requires library |
| **Build Tools** | ✅ None | ✅ None | ✅ None | ❌ Required |
| **Type Safety** | ✅ Full | ⚠️ Partial | ⚠️ Partial | ✅ With TypeScript |
| **Responsive** | ✅ Default | ❌ Manual | ❌ Manual | ⚠️ Requires CSS |
| **Accessibility** | ✅ WCAG AA | ❌ Manual | ❌ Manual | ⚠️ Manual |
| **Output Modes** | ✅ 9 modes | ❌ 1 mode | ❌ 1 mode | ❌ 1 mode |
| **Server-Side** | ✅ Yes | ✅ Yes | ✅ Yes | ⚠️ SSR complex |

**When to use HTMLskill:**
- ✅ You prefer Python over JavaScript
- ✅ You need professional design without hiring a designer
- ✅ You want multiple output formats (web, deck, email, etc.)
- ✅ You value type safety and IDE autocomplete
- ✅ You want zero build tools and instant output

**When to use alternatives:**
- ❌ You need a full SPA with client-side routing (use React)
- ❌ You already have a large Jinja2/Django template codebase
- ❌ You need pixel-perfect custom design (use Tailwind CSS)

---

## 🛣️ Roadmap

### Phase 1: Core API (Current - Alpha)
- [x] Basic components (heading, text, button, image)
- [x] Layout components (container, grid, section)
- [x] Composite components (hero, features, cta)
- [x] Design system (8px grid, WCAG AA, CJK fonts)
- [x] Web template renderer
- [ ] CLI tool (`htmlskill render`, `htmlskill watch`)
- [ ] Documentation site

### Phase 2: Advanced Features (Q2 2026)
- [ ] Deck template (presentation slides)
- [ ] Email template (campaign-ready)
- [ ] Card template (social media OG images)
- [ ] Form components (input, select, checkbox)
- [ ] Navigation components (navbar, sidebar, breadcrumb)
- [ ] Animation support (fade, slide, zoom)
- [ ] Dark mode support

### Phase 3: Ecosystem (Q3 2026)
- [ ] Plugin system for custom components
- [ ] Integration with Flask/FastAPI/Django
- [ ] VS Code extension (syntax highlighting, snippets)
- [ ] Component marketplace
- [ ] Figma → HTMLskill converter
- [ ] AI-powered component generation

---

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Quick Start for Contributors:**

1. **Fork and clone:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/HTMLskill.git
   cd HTMLskill
   ```

2. **Install dev dependencies:**
   ```bash
   pip install -e ".[dev]"
   ```

3. **Run tests:**
   ```bash
   pytest tests/ -v
   ```

4. **Follow TDD:**
   - Write tests first (RED)
   - Implement feature (GREEN)
   - Refactor code (REFACTOR)

5. **Submit PR:**
   - Create a feature branch
   - Add tests for new features
   - Update documentation
   - Submit pull request

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

- **Mesop API**: Inspiration for the decorator-based API
- **huashu-design**: Design system principles
- **html-anything**: Multi-template rendering approach

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/AIPMAndy/HTMLskill/issues)
- **Discussions**: [GitHub Discussions](https://github.com/AIPMAndy/HTMLskill/discussions)

---

**Built with ❤️ by the HTMLskill team**

---

<!-- andy-author-card:start -->
## 作者 / About the author

**AI 酋长 Andy（Andy Liu，GitHub/X @AIPMAndy）**：前腾讯/百度 AI 产品专家，大模型独角兽前 VP，现专注 AI + 产品方法论创业。

微信 `AIPMAndy`（备注「HTMLskill」） · [X @AIPMAndy](https://x.com/AIPMAndy) · [Telegram @AIPMAndy](https://t.me/AIPMAndy) · [个人官网 metaver.vip](https://metaver.vip/)

*AI Chief Andy (Andy Liu, @AIPMAndy on GitHub and X) is a former Tencent and Baidu AI product expert and former VP at an LLM unicorn, now a serial entrepreneur focused on AI and product methodology.*

### 作者的其他项目

- [AndySoul](https://github.com/AIPMAndy/AndySoul)：CLAUDE.md / AGENTS.md 规则模板，让 Claude Code、Codex、Cursor 少犯错
- [DNA Memory](https://github.com/AIPMAndy/dna-memory)：Claude Code、Codex 共用的本地 AI Agent 记忆 MCP
- [SafeSkill](https://github.com/AIPMAndy/safeskill)：装 AI Skill 之前，先扫危险命令、提示注入和密钥泄露
- [OpenClaw Skills 中文精选](https://github.com/AIPMAndy/awesome-openclaw-skills-CN)：OpenClaw Skills 分类整理，附国产模型接入指南
- [Grok Bot 中文攻略](https://aipmandy.github.io/grok-bot-handbook/)：AI Agent 中文教程

<!-- andy-author-card:end -->
