"""Base renderer for all output modes."""
from abc import ABC, abstractmethod
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape
from htmlskill.api.context import RenderContext


class BaseRenderer(ABC):
    """Base class for all renderers."""

    def __init__(self):
        """Initialize renderer with Jinja2 environment."""
        template_dir = Path(__file__).parent.parent / "templates"
        self.env = Environment(
            loader=FileSystemLoader(str(template_dir)),
            autoescape=select_autoescape(["html", "xml"]),
            trim_blocks=True,
            lstrip_blocks=True,
        )

    @abstractmethod
    def get_template_name(self) -> str:
        """Get the template file name for this renderer."""
        pass

    def render(self, context: RenderContext) -> str:
        """
        Render the context to HTML.

        Args:
            context: RenderContext with components

        Returns:
            HTML string
        """
        template = self.env.get_template(self.get_template_name())
        return template.render(
            mode=context.mode,
            design_system=context.design_system,
            brand=context.brand,
            components=context.components,
            config=context.config,
        )
