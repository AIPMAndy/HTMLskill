"""Tests for composite components."""
import pytest
from htmlskill.api.decorators import page
from htmlskill.components.composite import hero, features, cta, navbar, footer, card


def test_hero_context_manager():
    @page()
    def test_page():
        with hero(background="gradient"):
            pass

    ctx = test_page()
    assert len(ctx.components) == 2
    assert ctx.components[0]["type"] == "hero_start"
    assert ctx.components[0]["props"]["background"] == "gradient"


def test_features_function():
    @page()
    def test_page():
        features([
            {"icon": "⚡", "title": "Fast", "description": "Lightning fast"},
            {"icon": "🔒", "title": "Secure", "description": "Bank-grade security"},
        ])

    ctx = test_page()
    assert len(ctx.components) == 1
    assert ctx.components[0]["type"] == "features"
    assert len(ctx.components[0]["props"]["items"]) == 2


def test_cta_component():
    @page()
    def test_page():
        cta("Get Started", url="https://example.com")

    ctx = test_page()
    assert len(ctx.components) == 1
    assert ctx.components[0]["type"] == "cta"
    assert ctx.components[0]["props"]["text"] == "Get Started"


def test_navbar_component():
    @page()
    def test_page():
        navbar(logo="./logo.svg", links=["Home", "About", "Contact"])

    ctx = test_page()
    assert len(ctx.components) == 1
    assert ctx.components[0]["type"] == "navbar"
    assert ctx.components[0]["props"]["logo"] == "./logo.svg"
    assert len(ctx.components[0]["props"]["links"]) == 3


def test_footer_component():
    @page()
    def test_page():
        footer(copyright="© 2026 Company")

    ctx = test_page()
    assert len(ctx.components) == 1
    assert ctx.components[0]["type"] == "footer"
    assert ctx.components[0]["props"]["copyright"] == "© 2026 Company"


def test_card_context_manager():
    @page()
    def test_page():
        with card(title="Card Title"):
            pass

    ctx = test_page()
    assert len(ctx.components) == 2
    assert ctx.components[0]["type"] == "card_start"
    assert ctx.components[0]["props"]["title"] == "Card Title"
