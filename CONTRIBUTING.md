# Contributing to HTMLskill

Thank you for your interest in contributing to HTMLskill! This guide will help you get started.

## 🎯 Development Philosophy

HTMLskill follows **Test-Driven Development (TDD)**:

1. **RED**: Write a failing test first
2. **GREEN**: Write minimal code to make it pass
3. **REFACTOR**: Improve code quality without changing behavior

## 🚀 Quick Start

### 1. Fork and Clone

```bash
git clone https://github.com/YOUR_USERNAME/HTMLskill.git
cd HTMLskill
```

### 2. Set Up Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in editable mode with dev dependencies
pip install -e ".[dev]"
```

### 3. Run Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=htmlskill --cov-report=html

# Run specific test file
pytest tests/test_components.py -v
```

## 📝 Contribution Workflow

### Adding a New Component

**Example: Adding a `card()` component**

#### Step 1: Write the Test (RED)

Create `tests/test_card_component.py`:

```python
import htmlskill as hs

def test_card_basic():
    """Test basic card component"""
    @hs.page(mode="web")
    def page():
        with hs.card():
            hs.heading("Card Title")
            hs.text("Card content")
    
    html = page()
    assert '<div class="card">' in html
    assert '<h2>Card Title</h2>' in html
    assert '<p>Card content</p>' in html

def test_card_with_image():
    """Test card with image"""
    @hs.page(mode="web")
    def page():
        with hs.card(image="photo.jpg"):
            hs.heading("Card Title")
    
    html = page()
    assert '<img src="photo.jpg"' in html
```

Run the test (it should fail):
```bash
pytest tests/test_card_component.py -v
```

#### Step 2: Implement the Feature (GREEN)

Add to `htmlskill/components/composite.py`:

```python
@contextmanager
def card(image: Optional[str] = None, padding: str = "md"):
    """
    Card component with optional image.
    
    Args:
        image: Optional image URL
        padding: Padding size (sm, md, lg)
    """
    ctx = get_render_context()
    
    # Start card container
    ctx.append('<div class="card">')
    
    # Add image if provided
    if image:
        ctx.append(f'<img src="{image}" alt="" class="card-image">')
    
    # Card content wrapper
    ctx.append(f'<div class="card-content padding-{padding}">')
    
    yield
    
    # Close wrappers
    ctx.append('</div>')  # card-content
    ctx.append('</div>')  # card
```

Run the test again (it should pass):
```bash
pytest tests/test_card_component.py -v
```

#### Step 3: Refactor (REFACTOR)

Improve code quality:
- Add type hints
- Add docstrings
- Extract magic strings to constants
- Optimize performance

#### Step 4: Update Documentation

Add to `README.md`:

```markdown
### Card Component

\`\`\`python
with hs.card(image="photo.jpg", padding="lg"):
    hs.heading("Card Title")
    hs.text("Card description")
    hs.button("Learn More")
\`\`\`
```

### Adding a New Design System

**Example: Adding a "cyberpunk" design system**

#### Step 1: Write the Test

Create `tests/test_cyberpunk_design.py`:

```python
def test_cyberpunk_colors():
    """Test cyberpunk color palette"""
    @hs.page(mode="web", design_system="cyberpunk")
    def page():
        hs.heading("Neon Title")
    
    html = page()
    assert 'color: #00ff00' in html  # Neon green
```

#### Step 2: Implement

Add to `htmlskill/design/systems.py`:

```python
DESIGN_SYSTEMS = {
    "cyberpunk": {
        "colors": {
            "primary": "#00ff00",    # Neon green
            "secondary": "#ff00ff",  # Neon pink
            "background": "#0a0a0a", # Dark background
            "text": "#ffffff",       # White text
        },
        "fonts": {
            "heading": "Orbitron, sans-serif",
            "body": "Roboto Mono, monospace",
        },
        "spacing": {
            "unit": 8,  # 8px grid
        }
    }
}
```

## 🧪 Testing Guidelines

### Test Structure

```python
def test_feature_name():
    """Clear description of what is being tested"""
    # Arrange: Set up test data
    @hs.page(mode="web")
    def page():
        hs.heading("Test")
    
    # Act: Execute the code
    html = page()
    
    # Assert: Verify the result
    assert '<h1>Test</h1>' in html
```

### Test Coverage

- **Unit tests**: Test individual components in isolation
- **Integration tests**: Test component interactions
- **Regression tests**: Prevent bugs from reappearing

Aim for **>90% code coverage**.

## 📋 Code Style

### Python Style

Follow **PEP 8** with these additions:

```python
# Good: Clear function names
def render_hero_section():
    pass

# Bad: Unclear abbreviations
def rhs():
    pass

# Good: Type hints
def heading(text: str, level: int = 1) -> None:
    pass

# Bad: No type hints
def heading(text, level=1):
    pass

# Good: Docstrings
def button(text: str, href: str = "#") -> None:
    """
    Render a button element.
    
    Args:
        text: Button text
        href: Link URL (default: "#")
    """
    pass
```

### Commit Messages

Follow **Conventional Commits**:

```
feat: add card component
fix: correct hero gradient rendering
docs: update README with new examples
test: add tests for grid layout
refactor: simplify context management
```

## 🐛 Reporting Bugs

Use the [Bug Report template](.github/ISSUE_TEMPLATE/bug_report.md):

1. **Describe the bug**: Clear and concise description
2. **Reproduction steps**: Minimal code to reproduce
3. **Expected behavior**: What should happen
4. **Actual behavior**: What actually happens
5. **Environment**: Python version, OS, HTMLskill version

## 💡 Requesting Features

Use the [Feature Request template](.github/ISSUE_TEMPLATE/feature_request.md):

1. **Problem statement**: What problem does this solve?
2. **Proposed solution**: How should it work?
3. **Alternatives**: Other approaches considered
4. **Use cases**: Real-world examples

## 🔍 Code Review Process

All contributions go through code review:

1. **Automated checks**: Tests, linting, coverage
2. **Manual review**: Code quality, design, documentation
3. **Feedback**: Constructive suggestions for improvement
4. **Approval**: At least one maintainer approval required

### Review Checklist

- [ ] Tests pass (`pytest tests/ -v`)
- [ ] Code coverage >90% (`pytest --cov`)
- [ ] Type hints added (`mypy htmlskill/`)
- [ ] Docstrings added
- [ ] README updated (if needed)
- [ ] CHANGELOG updated
- [ ] No breaking changes (or documented)

## 📦 Release Process

Maintainers only:

1. Update version in `setup.py`
2. Update `CHANGELOG.md`
3. Create git tag: `git tag v0.2.0`
4. Push tag: `git push origin v0.2.0`
5. GitHub Actions will build and publish to PyPI

## 🙏 Recognition

Contributors are recognized in:
- `CONTRIBUTORS.md` file
- GitHub Contributors page
- Release notes

## 📞 Questions?

- **GitHub Discussions**: For general questions
- **GitHub Issues**: For bug reports and feature requests
- **Email**: For private inquiries

---

**Thank you for contributing to HTMLskill!** 🎉
