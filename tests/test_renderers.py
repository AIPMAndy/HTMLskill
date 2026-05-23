"""Tests for renderers."""
import pytest
from htmlskill.api.decorators import page
from htmlskill.components.basic import heading, text, button
from htmlskill.components.composite import navbar, footer
from htmlskill.renderers.web import WebPrototypeRenderer


def test_web_prototype_renderer_basic():
    @page(mode="web-prototype")
    def test_page():
        heading("Hello World", level=1)
        text("Welcome to HTMLSkill")
        button("Get Started", style="primary")

    ctx = test_page()
    renderer = WebPrototypeRenderer()
    html = renderer.render(ctx)

    assert "<!DOCTYPE html>" in html
    assert "Hello World" in html
    assert "Welcome to HTMLSkill" in html
    assert "Get Started" in html


def test_web_prototype_renderer_with_navbar():
    @page(mode="web-prototype")
    def test_page():
        navbar(logo="./logo.svg", links=["Home", "About"])
        heading("Test Page", level=1)

    ctx = test_page()
    renderer = WebPrototypeRenderer()
    html = renderer.render(ctx)

    assert "navbar" in html
    assert "logo.svg" in html
    assert "Home" in html
    assert "About" in html


def test_web_prototype_renderer_with_footer():
    @page(mode="web-prototype")
    def test_page():
        heading("Content", level=1)
        footer(copyright="© 2026 Test")

    ctx = test_page()
    renderer = WebPrototypeRenderer()
    html = renderer.render(ctx)

    assert "footer" in html
    assert "© 2026 Test" in html
