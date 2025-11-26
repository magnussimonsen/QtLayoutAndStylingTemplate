"""Placeholder settings sidebar used by the demo UI."""

from __future__ import annotations

try:  # pragma: no cover - only imported when Qt is available
    from PySide6.QtGui import QPalette, QColor
    from PySide6.QtWidgets import (
        QComboBox,
        QFormLayout,
        QLabel,
        QSpinBox,
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
        
        # Use VBoxLayout instead of QFormLayout to add toolbar
        from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Add toolbar placeholder
        toolbar = QWidget(self)
        toolbar.setProperty("sidebarRole", "toolbar")
        toolbar.setAutoFillBackground(True)
        toolbar_label = QLabel("Toolbar Area", toolbar)
        toolbar_layout = QHBoxLayout(toolbar)
        toolbar_layout.setContentsMargins(8, 8, 8, 8)
        toolbar_layout.addWidget(toolbar_label)
        main_layout.addWidget(toolbar)

        # Add a simple label to test if content shows with sidebar_content background
        test_label = QLabel("Settings Panel Content")
        test_label.setStyleSheet("background-color: #F5FF66; color: #111111; padding: 20px;")
        main_layout.addWidget(test_label)
        main_layout.addStretch()

        layout = QFormLayout()

        # Temporarily removed all other content for debugging
        # self.ui_font_combo = self._build_combo(["Inter", "Figtree", "JetBrains Mono"])
        # layout.addRow("UI Font", self.ui_font_combo)

        # self.ui_font_size = self._build_spinbox(8, 24, 14)
        # layout.addRow("UI Size", self.ui_font_size)

        # self.code_font_combo = self._build_combo(["Fira Code", "JetBrains Mono"])
        # layout.addRow("Code Font", self.code_font_combo)

        # self.code_font_size = self._build_spinbox(8, 24, 13)
        # layout.addRow("Code Size", self.code_font_size)

        # self.precision_spin = self._build_spinbox(0, 10, 4)
        # layout.addRow("Precision", self.precision_spin)

        # layout.addRow("", self._build_hint())

    @staticmethod
    def _build_combo(values: list[str]) -> QComboBox:
        combo = QComboBox()
        combo.addItems(values)
        combo.setEditable(False)
        return combo

    @staticmethod
    def _build_spinbox(min_value: int, max_value: int, current: int) -> QSpinBox:
        spin = QSpinBox()
        spin.setRange(min_value, max_value)
        spin.setValue(current)
        return spin

    @staticmethod
    def _build_hint() -> QLabel:
        label = QLabel("Settings wiring will land in a future pass.")
        label.setWordWrap(True)
        label.setProperty("statusRole", "info")
        return label


__all__ = ["SettingsSidebarWidget"]
