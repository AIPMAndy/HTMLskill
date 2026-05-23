"""Decorators for pages and components."""
from functools import wraps
from typing import Callable, Literal, Optional
import threading
from htmlskill.api.context import RenderContext
from htmlskill.api.registry import get_registry


# Thread-local storage for current context
_current_context = threading.local()


def get_current_context() -> Optional[RenderContext]:
    """Get the current render context."""
    return getattr(_current_context, "value", None)


def set_current_context(ctx: Optional[RenderContext]) -> None:
    """Set the current render context."""
    _current_context.value = ctx


def page(
    path: str = "/",
    mode: Literal["web-prototype", "deck", "infographic"] = "web-prototype",
    design_system: Literal["huashu", "minimal", "custom"] = "huashu",
    brand: Optional[str] = None,
    template: Optional[str] = None,
    template_config: Optional[dict] = None,
):
    """Decorator to mark a function as a page."""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            ctx = RenderContext(
                mode=mode,
                design_system=design_system,
                brand=brand,
                path=path,
            )

            set_current_context(ctx)

            try:
                result = func(*args, **kwargs)
                return ctx
            finally:
                set_current_context(None)

        wrapper._htmlskill_page = True
        wrapper._htmlskill_mode = mode
        wrapper._htmlskill_design_system = design_system
        wrapper._htmlskill_brand = brand
        wrapper._htmlskill_path = path
        wrapper._htmlskill_template = template
        wrapper._htmlskill_template_config = template_config or {}

        return wrapper

    return decorator


def component(name: str):
    """Decorator to register a custom component."""

    def decorator(func: Callable) -> Callable:
        registry = get_registry()
        registry.register(name, func)

        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        wrapper._htmlskill_component = True
        wrapper._htmlskill_name = name

        return wrapper

    return decorator
