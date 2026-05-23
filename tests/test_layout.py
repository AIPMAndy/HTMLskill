"""Tests for layout components."""
import pytest
from htmlskill.api.decorators import page
from htmlskill.components.layout import container, grid, section


def test_container_context_manager():
    @page()
    def test_page():
        with container(max_width="1200px"):
            pass

    ctx = test_page()
    assert len(ctx.components) == 2  # container_start + container_end
    assert ctx.components[0]["type"] == "container_start"
    assert ctx.components[0]["props"]["max_width"] == "1200px"
    assert ctx.components[1]["type"] == "container_end"


def test_grid_context_manager():
    @page()
    def test_page():
        with grid(columns=3, gap="32px"):
            pass

    ctx = test_page()
    assert len(ctx.components) == 2
    assert ctx.components[0]["type"] == "grid_start"
    assert ctx.components[0]["props"]["columns"] == 3
    assert ctx.components[0]["props"]["gap"] == "32px"


def test_section_context_manager():
    @page()
    def test_page():
        with section(padding="80px"):
            pass

    ctx = test_page()
    assert len(ctx.components) == 2
    assert ctx.components[0]["type"] == "section_start"
    assert ctx.components[0]["props"]["padding"] == "80px"


def test_nested_layout_components():
    @page()
    def test_page():
        with container():
            with section():
                with grid(columns=2):
                    pass

    ctx = test_page()
    # Should have: container_start, section_start, grid_start, grid_end, section_end, container_end
    assert len(ctx.components) == 6
    assert ctx.components[0]["type"] == "container_start"
    assert ctx.components[1]["type"] == "section_start"
    assert ctx.components[2]["type"] == "grid_start"
    assert ctx.components[3]["type"] == "grid_end"
    assert ctx.components[4]["type"] == "section_end"
    assert ctx.components[5]["type"] == "container_end"
