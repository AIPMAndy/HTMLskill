"""API module for decorators and context management."""
from htmlskill.api.decorators import page, component, get_current_context
from htmlskill.api.context import RenderContext
from htmlskill.api.registry import ComponentRegistry, get_registry

__all__ = [
    "page",
    "component",
    "get_current_context",
    "RenderContext",
    "ComponentRegistry",
    "get_registry",
]
