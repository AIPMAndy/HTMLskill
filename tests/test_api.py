"""Tests for API decorators."""
import pytest
from htmlskill.api.decorators import page, component, get_current_context
from htmlskill.api.context import RenderContext


def test_page_decorator_basic():
    @page(mode="web-prototype")
    def my_page():
        pass

    assert hasattr(my_page, "_htmlskill_page")
    assert my_page._htmlskill_mode == "web-prototype"


def test_page_decorator_with_brand():
    @page(mode="deck", brand="Stripe")
    def my_deck():
        pass

    assert my_deck._htmlskill_mode == "deck"
    assert my_deck._htmlskill_brand == "Stripe"


def test_page_decorator_execution():
    @page(mode="web-prototype")
    def my_page():
        ctx = get_current_context()
        assert ctx is not None
        assert ctx.mode == "web-prototype"

    ctx = my_page()
    assert isinstance(ctx, RenderContext)
    assert ctx.mode == "web-prototype"
