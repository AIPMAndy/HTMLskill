"""Design constraint checker for huashu-design system."""
import re
from typing import List, Tuple


class ConstraintChecker:
    """Check design constraints (8px grid, contrast, fonts)."""

    # CJK font names
    CJK_FONTS = {
        "noto sans sc", "noto sans tc", "noto sans jp", "noto sans kr",
        "noto serif sc", "noto serif tc", "noto serif jp", "noto serif kr",
        "source han sans", "source han serif",
        "microsoft yahei", "simsun", "simhei",
        "pingfang sc", "hiragino sans",
    }

    def check_grid(self, value: int) -> bool:
        """Check if value conforms to 8px grid."""
        return value % 8 == 0

    def check_contrast(self, fg: str, bg: str) -> float:
        """
        Check color contrast ratio (WCAG AA requires ≥4.5).

        Args:
            fg: Foreground color (hex)
            bg: Background color (hex)

        Returns:
            Contrast ratio (1-21)
        """
        fg_luminance = self._get_relative_luminance(fg)
        bg_luminance = self._get_relative_luminance(bg)

        lighter = max(fg_luminance, bg_luminance)
        darker = min(fg_luminance, bg_luminance)

        return (lighter + 0.05) / (darker + 0.05)

    def check_font_stack(self, fonts: List[str]) -> bool:
        """
        Check if font stack is CJK-first.

        Args:
            fonts: List of font names

        Returns:
            True if first font is CJK
        """
        if not fonts:
            return False

        first_font = fonts[0].lower().strip()
        return first_font in self.CJK_FONTS

    def _get_relative_luminance(self, color: str) -> float:
        """
        Calculate relative luminance of a color.

        Args:
            color: Hex color string (e.g., "#FFFFFF")

        Returns:
            Relative luminance (0-1)
        """
        # Remove # if present
        color = color.lstrip("#")

        # Convert to RGB
        r, g, b = int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16)

        # Normalize to 0-1
        r, g, b = r / 255.0, g / 255.0, b / 255.0

        # Apply gamma correction
        r = self._gamma_correct(r)
        g = self._gamma_correct(g)
        b = self._gamma_correct(b)

        # Calculate luminance
        return 0.2126 * r + 0.7152 * g + 0.0722 * b

    def _gamma_correct(self, channel: float) -> float:
        """Apply gamma correction to a color channel."""
        if channel <= 0.03928:
            return channel / 12.92
        else:
            return ((channel + 0.055) / 1.055) ** 2.4
