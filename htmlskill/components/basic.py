"""Basic components."""
from typing import Literal, Optional
from htmlskill.api.decorators import get_current_context


def heading(
    text: str,
    level: Literal[1, 2, 3, 4, 5, 6] = 1,
    align: Literal["left", "center", "right"] = "left",
    **kwargs
) -> None:
    """Render a heading."""
    ctx = get_current_context()
    if ctx:
        ctx.add_component("heading", {
            "text": text,
            "level": level,
            "align": align,
            **kwargs
        })


def text(
    content: str,
    size: Literal["small", "medium", "large"] = "medium",
    color: Optional[str] = None,
    **kwargs
) -> None:
    """Render text content."""
    ctx = get_current_context()
    if ctx:
        ctx.add_component("text", {
            "content": content,
            "size": size,
            "color": color,
            **kwargs
        })


def button(
    text: str,
    style: Literal["primary", "secondary", "outline"] = "primary",
    size: Literal["small", "medium", "large"] = "medium",
    on_click: Optional[str] = None,
    **kwargs
) -> None:
    """Render a button."""
    ctx = get_current_context()
    if ctx:
        ctx.add_component("button", {
            "text": text,
            "style": style,
            "size": size,
            "on_click": on_click,
            **kwargs
        })


def image(
    src: str,
    alt: str = "",
    width: Optional[str] = None,
    height: Optional[str] = None,
    **kwargs
) -> None:
    """Render an image."""
    ctx = get_current_context()
    if ctx:
        ctx.add_component("image", {
            "src": src,
            "alt": alt,
            "width": width,
            "height": height,
            **kwargs
        })


def spacer(height: str = "32px", **kwargs) -> None:
    """Render vertical spacing."""
    ctx = get_current_context()
    if ctx:
        ctx.add_component("spacer", {
            "height": height,
            **kwargs
        })


def divider(
    color: str = "#E5E7EB",
    thickness: str = "1px",
    **kwargs
) -> None:
    """Render a horizontal divider."""
    ctx = get_current_context()
    if ctx:
        ctx.add_component("divider", {
            "color": color,
            "thickness": thickness,
            **kwargs
        })
