"""Tests for RenderContext and ComponentRegistry."""
import pytest
from htmlskill.api.context import RenderContext
from htmlskill.api.registry import ComponentRegistry


def test_render_context_initialization():
    ctx = RenderContext(mode="web-prototype", design_system="huashu")
    assert ctx.mode == "web-prototype"
    assert ctx.design_system == "huashu"
    assert ctx.components == []


def test_render_context_add_component():
    ctx = RenderContext(mode="web-prototype")
    ctx.add_component("heading", {"text": "Hello", "level": 1})
    assert len(ctx.components) == 1
    assert ctx.components[0]["type"] == "heading"
    assert ctx.components[0]["props"]["text"] == "Hello"


def test_component_registry_register():
    registry = ComponentRegistry()

    def my_component(**props):
        return {"type": "custom", "props": props}

    registry.register("my_component", my_component)
    assert "my_component" in registry.components
    assert registry.get("my_component") == my_component


def test_component_registry_get_nonexistent():
    registry = ComponentRegistry()
    assert registry.get("nonexistent") is None
