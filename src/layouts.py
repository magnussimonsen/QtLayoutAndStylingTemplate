"""
Layout Examples Module
Demonstrates different Qt layout managers and their usage.
"""

from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QFormLayout,
    QGroupBox,
    QPushButton,
    QLabel,
    QLineEdit,
    QCheckBox,
    QRadioButton,
    QSlider,
    QProgressBar,
    QComboBox,
    QSpinBox,
    QFrame,
)
from PyQt6.QtCore import Qt


class LayoutExamplesWidget(QWidget):
    """Widget demonstrating various Qt layout types."""

    def __init__(self):
        super().__init__()
        self._setup_ui()

    def _setup_ui(self):
        """Set up the main UI with examples of different layouts."""
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Title
        title = QLabel("Qt Layout Examples")
        title.setProperty("class", "title")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title)

        subtitle = QLabel("Demonstrating different layout managers")
        subtitle.setProperty("class", "subtitle")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(subtitle)

        # Create layout example sections
        layout_examples = QHBoxLayout()
        layout_examples.setSpacing(20)

        # Left column
        left_column = QVBoxLayout()
        left_column.addWidget(self._create_vbox_example())
        left_column.addWidget(self._create_hbox_example())
        left_column.addStretch()
        layout_examples.addLayout(left_column)

        # Right column
        right_column = QVBoxLayout()
        right_column.addWidget(self._create_grid_example())
        right_column.addWidget(self._create_form_example())
        right_column.addStretch()
        layout_examples.addLayout(right_column)

        main_layout.addLayout(layout_examples)

    def _create_vbox_example(self) -> QGroupBox:
        """Create a VBoxLayout example."""
        group = QGroupBox("QVBoxLayout (Vertical)")
        layout = QVBoxLayout(group)
        layout.setSpacing(10)

        # Add some widgets
        layout.addWidget(QLabel("Widgets stack vertically"))

        btn1 = QPushButton("Primary Button")
        layout.addWidget(btn1)

        btn2 = QPushButton("Secondary Button")
        btn2.setProperty("class", "secondary")
        layout.addWidget(btn2)

        progress = QProgressBar()
        progress.setValue(65)
        layout.addWidget(progress)

        return group

    def _create_hbox_example(self) -> QGroupBox:
        """Create a HBoxLayout example."""
        group = QGroupBox("QHBoxLayout (Horizontal)")
        layout = QHBoxLayout(group)
        layout.setSpacing(10)

        # Add some widgets horizontally
        layout.addWidget(QPushButton("Left"))
        layout.addWidget(QPushButton("Center"))
        layout.addWidget(QPushButton("Right"))

        return group

    def _create_grid_example(self) -> QGroupBox:
        """Create a GridLayout example."""
        group = QGroupBox("QGridLayout (Grid)")
        layout = QGridLayout(group)
        layout.setSpacing(10)

        # Add widgets in a grid pattern
        layout.addWidget(QLabel("Row 0, Col 0"), 0, 0)
        layout.addWidget(QLabel("Row 0, Col 1"), 0, 1)
        layout.addWidget(QPushButton("Row 1, Col 0"), 1, 0)
        layout.addWidget(QPushButton("Row 1, Col 1"), 1, 1)

        # Spanning example
        span_btn = QPushButton("Spans 2 columns")
        span_btn.setProperty("class", "accent")
        layout.addWidget(span_btn, 2, 0, 1, 2)

        return group

    def _create_form_example(self) -> QGroupBox:
        """Create a FormLayout example."""
        group = QGroupBox("QFormLayout (Form)")
        layout = QFormLayout(group)
        layout.setSpacing(10)

        # Add form fields
        layout.addRow("Username:", QLineEdit())
        layout.addRow("Email:", QLineEdit())

        spin = QSpinBox()
        spin.setRange(0, 100)
        spin.setValue(25)
        layout.addRow("Age:", spin)

        combo = QComboBox()
        combo.addItems(["Option 1", "Option 2", "Option 3"])
        layout.addRow("Select:", combo)

        return group


class WidgetShowcaseWidget(QWidget):
    """Widget showcasing various Qt widgets with styling."""

    def __init__(self):
        super().__init__()
        self._setup_ui()

    def _setup_ui(self):
        """Set up the widget showcase UI."""
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Title
        title = QLabel("Widget Showcase")
        title.setProperty("class", "title")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title)

        # Create showcase sections
        content_layout = QHBoxLayout()
        content_layout.setSpacing(20)

        content_layout.addWidget(self._create_input_showcase())
        content_layout.addWidget(self._create_selection_showcase())
        content_layout.addWidget(self._create_display_showcase())

        main_layout.addLayout(content_layout)

    def _create_input_showcase(self) -> QGroupBox:
        """Create input widgets showcase."""
        group = QGroupBox("Input Widgets")
        layout = QVBoxLayout(group)
        layout.setSpacing(15)

        # Text input
        layout.addWidget(QLabel("Text Input:"))
        text_input = QLineEdit()
        text_input.setPlaceholderText("Enter text here...")
        layout.addWidget(text_input)

        # Number input
        layout.addWidget(QLabel("Spin Box:"))
        spin = QSpinBox()
        spin.setRange(0, 100)
        layout.addWidget(spin)

        # Slider
        layout.addWidget(QLabel("Slider:"))
        slider = QSlider(Qt.Orientation.Horizontal)
        slider.setRange(0, 100)
        slider.setValue(50)
        layout.addWidget(slider)

        layout.addStretch()
        return group

    def _create_selection_showcase(self) -> QGroupBox:
        """Create selection widgets showcase."""
        group = QGroupBox("Selection Widgets")
        layout = QVBoxLayout(group)
        layout.setSpacing(15)

        # Checkboxes
        layout.addWidget(QLabel("Checkboxes:"))
        for i in range(1, 4):
            cb = QCheckBox(f"Option {i}")
            if i == 1:
                cb.setChecked(True)
            layout.addWidget(cb)

        # Radio buttons
        layout.addWidget(QLabel("Radio Buttons:"))
        for i in range(1, 4):
            rb = QRadioButton(f"Choice {i}")
            if i == 1:
                rb.setChecked(True)
            layout.addWidget(rb)

        # Combo box
        layout.addWidget(QLabel("Combo Box:"))
        combo = QComboBox()
        combo.addItems(["First", "Second", "Third"])
        layout.addWidget(combo)

        layout.addStretch()
        return group

    def _create_display_showcase(self) -> QGroupBox:
        """Create display widgets showcase."""
        group = QGroupBox("Display Widgets")
        layout = QVBoxLayout(group)
        layout.setSpacing(15)

        # Progress bars
        layout.addWidget(QLabel("Progress Bars:"))
        for value in [25, 50, 75]:
            progress = QProgressBar()
            progress.setValue(value)
            layout.addWidget(progress)

        # Styled frame/card
        layout.addWidget(QLabel("Styled Card:"))
        card = QFrame()
        card.setProperty("class", "card")
        card_layout = QVBoxLayout(card)
        card_layout.addWidget(QLabel("Card Title"))
        card_layout.addWidget(QLabel("This is a styled card widget"))
        layout.addWidget(card)

        layout.addStretch()
        return group
