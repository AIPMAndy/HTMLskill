"""Context for rendering pages."""
from typing import Any, Dict, List, Literal, Optional
from dataclasses import dataclass, field


@dataclass
class RenderContext:
    """Context for rendering a page."""

    mode: Literal["web-prototype", "deck", "infographic"] = "web-prototype"
    design_system: Literal["huashu", "minimal", "custom"] = "huashu"
    brand: Optional[str] = None
    path: str = "/"
    components: List[Dict[str, Any]] = field(default_factory=list)
    config: Dict[str, Any] = field(default_factory=dict)

    def add_component(self, component_type: str, props: Dict[str, Any]) -> None:
        """Add a component to the render queue."""
        self.components.append({
            "type": component_type,
            "props": props
        })

    def clear(self) -> None:
        """Clear all components."""
        self.components.clear()
