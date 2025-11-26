"""QSS snippet for docked sidebars (settings, notebooks, etc.)."""

from __future__ import annotations

from textwrap import dedent

from theme import Theme, ThemeMode, get_theme

SIDEBAR_DOCK_SELECTOR = "QDockWidget#NotebooksDock, QDockWidget#SettingsDock"
SIDEBAR_ACTION_ROW_SELECTOR = 'QWidget[sidebarRole="action-row"]'


def get_qss(
    mode: ThemeMode = ThemeMode.DARK,
    theme: Theme | None = None,
) -> str:
    """Return QSS that styles all dock-based sidebars consistently."""

    theme = theme or get_theme(mode)
    metrics = theme.metrics
    bg = theme.bg
    border = theme.border
    text = theme.text

    dock_block = dedent(
        f"""
        {SIDEBAR_DOCK_SELECTOR} {{
            background-color: {bg.sidebar_content};
            color: {text.primary};
            border-left: {metrics.border_width}px solid {border.strong};
        }}

        QDockWidget#NotebooksDock::title,
        QDockWidget#SettingsDock::title {{
            background-color: {bg.sidebar_header};
            color: {text.primary};
            text-align: left;
            padding: {metrics.padding_small}px;
        }}

        {SIDEBAR_DOCK_SELECTOR} > QWidget {{
            background-color: {bg.sidebar_content};
        }}

        QDockWidget#NotebooksDock QWidget#NotebookSidebarPanel,
        QDockWidget#SettingsDock QWidget#SettingsSidebarPanel {{
            background-color: {bg.sidebar_content};
        }}
        """
    ).strip()

    toolbar_block = dedent(
        f"""
        QWidget[sidebarRole="toolbar"] {{
            background-color: {bg.sidebar_toolbar};
            color: {text.primary};
            padding: {metrics.padding_small}px;
            border-bottom: {metrics.border_width}px solid {border.strong};
        }}

        QWidget[sidebarRole="toolbar"] QLabel {{
            color: {text.primary};
        }}

        {SIDEBAR_ACTION_ROW_SELECTOR} {{
            background-color: {bg.sidebar_toolbar};
            border-radius: {metrics.radius_small}px;
            padding: {metrics.padding_extra_small}px {metrics.padding_small}px;
        }}
        """
    ).strip()

    # Style child widgets inside sidebars to match the sidebar background
    child_widgets_block = dedent(
        f"""
        QDockWidget#NotebooksDock QListWidget,
        QDockWidget#SettingsDock QListWidget {{
            background-color: transparent;
            border: none;
            color: {text.primary};
        }}

        QDockWidget#NotebooksDock QListWidget::item,
        QDockWidget#SettingsDock QListWidget::item {{
            background-color: transparent;
            color: {text.primary};
        }}

        QDockWidget#NotebooksDock QListWidget::item:selected,
        QDockWidget#SettingsDock QListWidget::item:selected {{
            background-color: {bg.sidebar_toolbar};
            color: {text.primary};
        }}

        QDockWidget#NotebooksDock QComboBox,
        QDockWidget#SettingsDock QComboBox,
        QDockWidget#NotebooksDock QSpinBox,
        QDockWidget#SettingsDock QSpinBox {{
            background-color: {bg.sidebar_content};
            border: {metrics.border_width}px solid {border.subtle};
            padding: {metrics.padding_small}px;
        }}

        QDockWidget#NotebooksDock QComboBox:hover,
        QDockWidget#SettingsDock QComboBox:hover,
        QDockWidget#NotebooksDock QSpinBox:hover,
        QDockWidget#SettingsDock QSpinBox:hover {{
            border-color: {border.strong};
        }}

        QDockWidget#NotebooksDock QLabel,
        QDockWidget#SettingsDock QLabel {{
            background-color: transparent;
        }}
        """
    ).strip()

    return f"{dock_block}\n\n{toolbar_block}\n\n{child_widgets_block}"


__all__ = ["get_qss"]
