"""HTMLSkill - Python-first HTML generation framework."""

__version__ = "0.1.0"

from htmlskill.api.decorators import page, component
from htmlskill.components.basic import (
    heading,
    text,
    button,
    image,
    spacer,
    divider,
)
from htmlskill.components.layout import (
    container,
    grid,
    section,
)
from htmlskill.components.composite import (
    hero,
    features,
    cta,
    navbar,
    footer,
    card,
)

__all__ = [
    "page",
    "component",
    "heading",
    "text",
    "button",
    "image",
    "spacer",
    "divider",
    "container",
    "grid",
    "section",
    "hero",
    "features",
    "cta",
    "navbar",
    "footer",
    "card",
]
