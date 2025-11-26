"""
Color Theme Module
Provides color palette management and theme definitions for the Qt application.
"""

from dataclasses import dataclass
from typing import Dict


@dataclass
class ColorPalette:
    """Defines a color palette with primary, secondary, and accent colors."""

    primary: str
    primary_light: str
    primary_dark: str
    secondary: str
    secondary_light: str
    secondary_dark: str
    accent: str
    background: str
    surface: str
    text_primary: str
    text_secondary: str
    text_on_primary: str  # Text color for use on primary-colored backgrounds
    error: str
    success: str
    warning: str


# Pre-defined color themes
THEMES: Dict[str, ColorPalette] = {
    "dark": ColorPalette(
        primary="#6366F1",
        primary_light="#818CF8",
        primary_dark="#4F46E5",
        secondary="#10B981",
        secondary_light="#34D399",
        secondary_dark="#059669",
        accent="#F59E0B",
        background="#1E1E2E",
        surface="#2D2D3D",
        text_primary="#FFFFFF",
        text_secondary="#A1A1AA",
        text_on_primary="#FFFFFF",
        error="#EF4444",
        success="#22C55E",
        warning="#F59E0B",
    ),
    "light": ColorPalette(
        primary="#4F46E5",
        primary_light="#6366F1",
        primary_dark="#4338CA",
        secondary="#059669",
        secondary_light="#10B981",
        secondary_dark="#047857",
        accent="#D97706",
        background="#F8FAFC",
        surface="#FFFFFF",
        text_primary="#1E293B",
        text_secondary="#64748B",
        text_on_primary="#FFFFFF",
        error="#DC2626",
        success="#16A34A",
        warning="#D97706",
    ),
    "ocean": ColorPalette(
        primary="#0EA5E9",
        primary_light="#38BDF8",
        primary_dark="#0284C7",
        secondary="#06B6D4",
        secondary_light="#22D3EE",
        secondary_dark="#0891B2",
        accent="#8B5CF6",
        background="#0F172A",
        surface="#1E293B",
        text_primary="#F1F5F9",
        text_secondary="#94A3B8",
        text_on_primary="#FFFFFF",
        error="#F43F5E",
        success="#10B981",
        warning="#FBBF24",
    ),
    "forest": ColorPalette(
        primary="#22C55E",
        primary_light="#4ADE80",
        primary_dark="#16A34A",
        secondary="#84CC16",
        secondary_light="#A3E635",
        secondary_dark="#65A30D",
        accent="#F97316",
        background="#14532D",
        surface="#166534",
        text_primary="#ECFDF5",
        text_secondary="#BBF7D0",
        text_on_primary="#FFFFFF",
        error="#EF4444",
        success="#22C55E",
        warning="#EAB308",
    ),
}


def get_theme(name: str) -> ColorPalette:
    """Get a color palette by theme name.
    
    Args:
        name: Theme name (dark, light, ocean, forest)
        
    Returns:
        ColorPalette for the specified theme
    """
    return THEMES.get(name, THEMES["dark"])


def get_available_themes() -> list:
    """Get a list of available theme names."""
    return list(THEMES.keys())
