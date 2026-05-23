"""Web prototype renderer."""
from htmlskill.renderers.base import BaseRenderer


class WebPrototypeRenderer(BaseRenderer):
    """Renderer for web prototype mode."""

    def get_template_name(self) -> str:
        """Get template name."""
        return "web-prototype.html"
