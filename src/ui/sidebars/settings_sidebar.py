"""Placeholder settings sidebar used by the demo UI."""

from __future__ import annotations

try:  # pragma: no cover - only imported when Qt is available
    from PySide6.QtGui import QPalette, QColor
    from PySide6.QtWidgets import (
        QComboBox,
        QFormLayout,
        QLabel,
        QSpinBox,
        QVBoxLayout,
        QWidget,
    )
except ModuleNotFoundError as exc:  # pragma: no cover - runtime guard
    raise SystemExit("PySide6 must be installed to use the sidebar widgets.") from exc

class SettingsSidebarWidget(QWidget):
    """Lightweight form with font/precision controls."""

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setObjectName("SettingsSidebarPanel")
        self.setAutoFillBackground(True)
        
        from PySide6.QtWidgets import QHBoxLayout
        
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Add sidebar toolbar
        sidebar_toolbar = QWidget(self)
        sidebar_toolbar.setProperty("sidebarRole", "toolbar")
        sidebar_toolbar.setAutoFillBackground(True)
        toolbar_layout = QHBoxLayout(sidebar_toolbar)
        toolbar_layout.setContentsMargins(8, 8, 8, 8)
        toolbar_label = QLabel("Toolbar", sidebar_toolbar)
        toolbar_layout.addWidget(toolbar_label)
        toolbar_layout.addStretch()
        main_layout.addWidget(sidebar_toolbar)

        # Content area container
        content_container = QWidget(self)
        content_container.setProperty("sidebarRole", "content")
        content_container.setAutoFillBackground(True)
        content_layout = QVBoxLayout(content_container)
        content_layout.setContentsMargins(8, 8, 8, 8)
        
        content_label = QLabel("Content Area", content_container)
        content_layout.addWidget(content_label)
        content_layout.addStretch()
        
        main_layout.addWidget(content_container)


__all__ = ["SettingsSidebarWidget"]
