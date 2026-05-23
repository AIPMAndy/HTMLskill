"""Composite components."""
from typing import List, Optional
from htmlskill.api.decorators import get_current_context


def hero(background: str = "gradient", **kwargs):
    """Hero context manager - placeholder."""
    pass


def features(**kwargs):
    """Features - placeholder."""
    pass


def cta(text: str, **kwargs):
    """Call to action - placeholder."""
    pass


def navbar(logo: Optional[str] = None, links: Optional[List[str]] = None, **kwargs):
    """Navbar - placeholder."""
    pass


def footer(copyright: Optional[str] = None, **kwargs):
    """Footer - placeholder."""
    pass


def card(**kwargs):
    """Card - placeholder."""
    pass
