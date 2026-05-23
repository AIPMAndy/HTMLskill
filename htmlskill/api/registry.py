"""Component registry for custom components."""
from typing import Any, Callable, Dict, Optional


class ComponentRegistry:
    """Registry for custom components."""

    def __init__(self):
        self.components: Dict[str, Callable] = {}

    def register(self, name: str, func: Callable) -> None:
        """Register a component function."""
        self.components[name] = func

    def get(self, name: str) -> Optional[Callable]:
        """Get a registered component."""
        return self.components.get(name)

    def has(self, name: str) -> bool:
        """Check if a component is registered."""
        return name in self.components


# Global registry instance
_registry = ComponentRegistry()


def get_registry() -> ComponentRegistry:
    """Get the global component registry."""
    return _registry
