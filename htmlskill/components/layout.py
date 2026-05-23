"""Layout components with context manager support."""
from typing import Optional
from contextlib import contextmanager
from htmlskill.api.decorators import get_current_context


@contextmanager
def container(max_width: str = "1200px", **kwargs):
    """Container context manager."""
    ctx = get_current_context()
    if ctx:
        ctx.add_component("container_start", {
            "max_width": max_width,
            **kwargs
        })

    try:
        yield
    finally:
        if ctx:
            ctx.add_component("container_end", {})


@contextmanager
def grid(columns: int = 3, gap: str = "32px", **kwargs):
    """Grid context manager."""
    ctx = get_current_context()
    if ctx:
        ctx.add_component("grid_start", {
            "columns": columns,
            "gap": gap,
            **kwargs
        })

    try:
        yield
    finally:
        if ctx:
            ctx.add_component("grid_end", {})


@contextmanager
def section(padding: str = "80px", **kwargs):
    """Section context manager."""
    ctx = get_current_context()
    if ctx:
        ctx.add_component("section_start", {
            "padding": padding,
            **kwargs
        })

    try:
        yield
    finally:
        if ctx:
            ctx.add_component("section_end", {})
