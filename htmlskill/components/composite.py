"""Composite components."""
from typing import List, Optional, Dict, Any
from contextlib import contextmanager
from htmlskill.api.decorators import get_current_context


@contextmanager
def hero(background: str = "gradient", **kwargs):
    """Hero section context manager."""
    ctx = get_current_context()
    if ctx:
        ctx.add_component("hero_start", {
            "background": background,
            **kwargs
        })

    try:
        yield
    finally:
        if ctx:
            ctx.add_component("hero_end", {})


def features(items: List[Dict[str, str]], **kwargs) -> None:
    """Render a features grid."""
    ctx = get_current_context()
    if ctx:
        ctx.add_component("features", {
            "items": items,
            **kwargs
        })


def cta(text: str, url: Optional[str] = None, style: str = "primary", **kwargs) -> None:
    """Render a call-to-action button."""
    ctx = get_current_context()
    if ctx:
        ctx.add_component("cta", {
            "text": text,
            "url": url,
            "style": style,
            **kwargs
        })


def navbar(logo: Optional[str] = None, links: Optional[List[str]] = None, **kwargs) -> None:
    """Render a navigation bar."""
    ctx = get_current_context()
    if ctx:
        ctx.add_component("navbar", {
            "logo": logo,
            "links": links or [],
            **kwargs
        })


def footer(copyright: Optional[str] = None, links: Optional[List[str]] = None, **kwargs) -> None:
    """Render a footer."""
    ctx = get_current_context()
    if ctx:
        ctx.add_component("footer", {
            "copyright": copyright,
            "links": links or [],
            **kwargs
        })


@contextmanager
def card(title: Optional[str] = None, **kwargs):
    """Card context manager."""
    ctx = get_current_context()
    if ctx:
        ctx.add_component("card_start", {
            "title": title,
            **kwargs
        })

    try:
        yield
    finally:
        if ctx:
            ctx.add_component("card_end", {})
