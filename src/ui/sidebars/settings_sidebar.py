"""Placeholder settings sidebar used by the demo UI."""

from __future__ import annotations

try:  # pragma: no cover - only imported when Qt is available
    from PySide6.QtCore import Signal
    from PySide6.QtWidgets import (
        QFormLayout,
        QHBoxLayout,
        QLabel,
        QSpinBox,
        QVBoxLayout,
        QWidget,
    )
except ModuleNotFoundError as exc:  # pragma: no cover - runtime guard
    raise SystemExit("PySide6 must be installed to use the sidebar widgets.") from exc

class SettingsSidebarWidget(QWidget):
    """Lightweight form with font/precision controls."""

    ui_font_size_changed = Signal(int)

    def __init__(
        self,
        parent: QWidget | None = None,
        *,
        ui_font_size: int,
        min_font_size: int,
        max_font_size: int,
        step: int = 1,
    ) -> None:
        super().__init__(parent)
        self.setObjectName("SettingsSidebarPanel")
        self.setAutoFillBackground(True)

        self._ui_font_spin = QSpinBox(self)
        self._configure_font_spin(ui_font_size, min_font_size, max_font_size, step)

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        main_layout.addWidget(self._build_toolbar())
        main_layout.addWidget(self._build_content_container())

    def _configure_font_spin(
        self,
        value: int,
        min_value: int,
        max_value: int,
        step: int,
    ) -> None:
        self._ui_font_spin.setRange(min_value, max_value)
        self._ui_font_spin.setSingleStep(max(1, step))
        self._ui_font_spin.setValue(value)
        self._ui_font_spin.valueChanged.connect(self.ui_font_size_changed)

    def _build_toolbar(self) -> QWidget:
        toolbar = QWidget(self)
        toolbar.setProperty("sidebarRole", "toolbar")
        toolbar.setAutoFillBackground(True)
        toolbar_layout = QHBoxLayout(toolbar)
        toolbar_layout.setContentsMargins(8, 8, 8, 8)
        toolbar_layout.setSpacing(8)
        toolbar_label = QLabel("Sidebar Settings", toolbar)
        toolbar_layout.addWidget(toolbar_label)
        toolbar_layout.addStretch()
        return toolbar

    def _build_content_container(self) -> QWidget:
        container = QWidget(self)
        container.setProperty("sidebarRole", "content")
        container.setAutoFillBackground(True)
        content_layout = QVBoxLayout(container)
        content_layout.setContentsMargins(8, 8, 8, 8)
        content_layout.setSpacing(12)

        typography_label = QLabel("Typography", container)
        typography_label.setProperty("sidebarSection", "typography")
        content_layout.addWidget(typography_label)

        form_layout = QFormLayout()
        form_layout.setContentsMargins(0, 0, 0, 0)
        form_layout.setSpacing(6)
        form_layout.addRow("UI font size", self._ui_font_spin)
        content_layout.addLayout(form_layout)
        content_layout.addStretch()
        return container


__all__ = ["SettingsSidebarWidget"]
