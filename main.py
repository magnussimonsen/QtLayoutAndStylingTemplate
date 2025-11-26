"""
Qt Layout and Styling Template
Main application entry point demonstrating Qt layouts, styling, and color themes.
"""

import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QTabWidget,
    QLabel,
    QComboBox,
    QStatusBar,
    QFrame,
)
from PyQt6.QtCore import Qt

from src.colors import get_theme, get_available_themes, ColorPalette
from src.stylesheet import generate_stylesheet
from src.layouts import LayoutExamplesWidget, WidgetShowcaseWidget


class MainWindow(QMainWindow):
    """Main application window with theme switching and layout examples."""

    def __init__(self):
        super().__init__()
        self.current_theme = "dark"
        self._setup_ui()
        self._apply_theme(self.current_theme)

    def _setup_ui(self):
        """Set up the main window UI."""
        self.setWindowTitle("Qt Layout & Styling Template")
        self.setMinimumSize(1000, 700)

        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Header with theme selector
        header = self._create_header()
        main_layout.addWidget(header)

        # Tab widget for different sections
        self.tab_widget = QTabWidget()
        self.tab_widget.addTab(LayoutExamplesWidget(), "Layout Examples")
        self.tab_widget.addTab(WidgetShowcaseWidget(), "Widget Showcase")
        self.tab_widget.addTab(self._create_color_palette_tab(), "Color Palette")
        main_layout.addWidget(self.tab_widget)

        # Status bar
        status_bar = QStatusBar()
        status_bar.showMessage("Ready - Select a theme from the dropdown above")
        self.setStatusBar(status_bar)

    def _create_header(self) -> QFrame:
        """Create the header with theme selector."""
        header = QFrame()
        header.setFrameShape(QFrame.Shape.StyledPanel)
        layout = QHBoxLayout(header)
        layout.setContentsMargins(20, 15, 20, 15)

        # App title
        title = QLabel("Qt Layout & Styling Template")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)

        layout.addStretch()

        # Theme selector
        theme_label = QLabel("Theme:")
        layout.addWidget(theme_label)

        self.theme_combo = QComboBox()
        self.theme_combo.addItems([t.capitalize() for t in get_available_themes()])
        self.theme_combo.setCurrentText(self.current_theme.capitalize())
        self.theme_combo.currentTextChanged.connect(self._on_theme_changed)
        layout.addWidget(self.theme_combo)

        return header

    def _create_color_palette_tab(self) -> QWidget:
        """Create the color palette visualization tab."""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(20)
        layout.setContentsMargins(20, 20, 20, 20)

        # Title
        title = QLabel("Color Palette Visualization")
        title.setProperty("class", "title")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        subtitle = QLabel("Current theme colors displayed below")
        subtitle.setProperty("class", "subtitle")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(subtitle)

        # Color swatches container
        self.color_container = QWidget()
        self.color_layout = QHBoxLayout(self.color_container)
        self.color_layout.setSpacing(15)
        layout.addWidget(self.color_container)

        # We'll populate this when theme changes
        self._update_color_swatches()

        layout.addStretch()
        return widget

    def _update_color_swatches(self):
        """Update the color swatches display."""
        # Clear existing swatches
        while self.color_layout.count():
            child = self.color_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        palette = get_theme(self.current_theme)
        colors = [
            ("Primary", palette.primary),
            ("Primary Light", palette.primary_light),
            ("Primary Dark", palette.primary_dark),
            ("Secondary", palette.secondary),
            ("Accent", palette.accent),
            ("Background", palette.background),
            ("Surface", palette.surface),
            ("Success", palette.success),
            ("Warning", palette.warning),
            ("Error", palette.error),
        ]

        for name, color in colors:
            swatch = self._create_color_swatch(name, color)
            self.color_layout.addWidget(swatch)

    def _create_color_swatch(self, name: str, color: str) -> QFrame:
        """Create a color swatch widget."""
        frame = QFrame()
        frame.setMinimumSize(80, 100)
        frame.setStyleSheet(f"""
            QFrame {{
                background-color: {color};
                border-radius: 8px;
                border: 2px solid white;
            }}
        """)

        layout = QVBoxLayout(frame)
        layout.setAlignment(Qt.AlignmentFlag.AlignBottom)

        label = QLabel(name)
        label.setStyleSheet("""
            color: white;
            font-size: 10px;
            font-weight: bold;
            background-color: rgba(0, 0, 0, 0.5);
            padding: 4px;
            border-radius: 4px;
        """)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        color_code = QLabel(color)
        color_code.setStyleSheet("""
            color: white;
            font-size: 9px;
            background-color: rgba(0, 0, 0, 0.5);
            padding: 2px;
            border-radius: 2px;
        """)
        color_code.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(color_code)

        return frame

    def _on_theme_changed(self, theme_name: str):
        """Handle theme selection change."""
        self.current_theme = theme_name.lower()
        self._apply_theme(self.current_theme)
        self._update_color_swatches()
        self.statusBar().showMessage(f"Theme changed to: {theme_name}")

    def _apply_theme(self, theme_name: str):
        """Apply the selected theme to the application."""
        palette = get_theme(theme_name)
        stylesheet = generate_stylesheet(palette)
        self.setStyleSheet(stylesheet)


def main():
    """Main entry point for the application."""
    app = QApplication(sys.argv)
    app.setStyle("Fusion")  # Use Fusion style as base for better cross-platform consistency

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
