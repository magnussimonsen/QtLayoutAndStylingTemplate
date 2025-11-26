"""
Stylesheet Generator Module
Generates Qt Style Sheets (QSS) based on the color palette.
"""

from .colors import ColorPalette


def generate_stylesheet(palette: ColorPalette) -> str:
    """Generate a complete QSS stylesheet from a color palette.
    
    Args:
        palette: ColorPalette to use for styling
        
    Returns:
        Complete QSS stylesheet string
    """
    return f"""
/* Main Window Styling */
QMainWindow, QWidget {{
    background-color: {palette.background};
    color: {palette.text_primary};
    font-family: "Segoe UI", "SF Pro Display", "Roboto", sans-serif;
    font-size: 14px;
}}

/* Group Box Styling */
QGroupBox {{
    background-color: {palette.surface};
    border: 1px solid {palette.primary};
    border-radius: 8px;
    margin-top: 16px;
    padding: 16px;
    padding-top: 24px;
    font-weight: bold;
}}

QGroupBox::title {{
    subcontrol-origin: margin;
    subcontrol-position: top left;
    padding: 4px 12px;
    background-color: {palette.primary};
    color: {palette.text_primary};
    border-radius: 4px;
    left: 12px;
}}

/* Button Styling */
QPushButton {{
    background-color: {palette.primary};
    color: {palette.text_on_primary};
    border: none;
    border-radius: 6px;
    padding: 10px 20px;
    font-weight: 600;
    min-width: 80px;
}}

QPushButton:hover {{
    background-color: {palette.primary_light};
}}

QPushButton:pressed {{
    background-color: {palette.primary_dark};
}}

QPushButton:disabled {{
    background-color: {palette.surface};
    color: {palette.text_secondary};
}}

/* Secondary Button */
QPushButton[class="secondary"] {{
    background-color: {palette.secondary};
}}

QPushButton[class="secondary"]:hover {{
    background-color: {palette.secondary_light};
}}

QPushButton[class="secondary"]:pressed {{
    background-color: {palette.secondary_dark};
}}

/* Accent Button */
QPushButton[class="accent"] {{
    background-color: {palette.accent};
}}

/* Line Edit / Text Input */
QLineEdit {{
    background-color: {palette.surface};
    border: 2px solid {palette.primary};
    border-radius: 6px;
    padding: 8px 12px;
    color: {palette.text_primary};
    selection-background-color: {palette.primary_light};
}}

QLineEdit:focus {{
    border-color: {palette.primary_light};
}}

QLineEdit:disabled {{
    background-color: {palette.background};
    color: {palette.text_secondary};
}}

/* Text Edit */
QTextEdit {{
    background-color: {palette.surface};
    border: 2px solid {palette.primary};
    border-radius: 6px;
    padding: 8px;
    color: {palette.text_primary};
    selection-background-color: {palette.primary_light};
}}

/* Combo Box */
QComboBox {{
    background-color: {palette.surface};
    border: 2px solid {palette.primary};
    border-radius: 6px;
    padding: 8px 12px;
    color: {palette.text_primary};
    min-width: 120px;
}}

QComboBox:hover {{
    border-color: {palette.primary_light};
}}

QComboBox::drop-down {{
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 30px;
    border-left: 1px solid {palette.primary};
    border-top-right-radius: 6px;
    border-bottom-right-radius: 6px;
}}

QComboBox::down-arrow {{
    width: 12px;
    height: 12px;
}}

QComboBox QAbstractItemView {{
    background-color: {palette.surface};
    border: 1px solid {palette.primary};
    selection-background-color: {palette.primary};
    color: {palette.text_primary};
}}

/* Slider */
QSlider::groove:horizontal {{
    background-color: {palette.surface};
    height: 8px;
    border-radius: 4px;
}}

QSlider::handle:horizontal {{
    background-color: {palette.primary};
    width: 20px;
    margin: -6px 0;
    border-radius: 10px;
}}

QSlider::handle:horizontal:hover {{
    background-color: {palette.primary_light};
}}

QSlider::sub-page:horizontal {{
    background-color: {palette.primary};
    border-radius: 4px;
}}

/* Progress Bar */
QProgressBar {{
    background-color: {palette.surface};
    border: none;
    border-radius: 6px;
    text-align: center;
    color: {palette.text_primary};
}}

QProgressBar::chunk {{
    background-color: {palette.primary};
    border-radius: 6px;
}}

/* Check Box */
QCheckBox {{
    spacing: 8px;
    color: {palette.text_primary};
}}

QCheckBox::indicator {{
    width: 20px;
    height: 20px;
    border: 2px solid {palette.primary};
    border-radius: 4px;
    background-color: {palette.surface};
}}

QCheckBox::indicator:checked {{
    background-color: {palette.primary};
}}

QCheckBox::indicator:hover {{
    border-color: {palette.primary_light};
}}

/* Radio Button */
QRadioButton {{
    spacing: 8px;
    color: {palette.text_primary};
}}

QRadioButton::indicator {{
    width: 18px;
    height: 18px;
    border: 2px solid {palette.primary};
    border-radius: 11px;
    background-color: {palette.surface};
}}

QRadioButton::indicator:checked {{
    background-color: {palette.primary};
    border: 4px solid {palette.surface};
}}

/* Tab Widget */
QTabWidget::pane {{
    background-color: {palette.surface};
    border: 1px solid {palette.primary};
    border-radius: 8px;
    padding: 8px;
}}

QTabBar::tab {{
    background-color: {palette.background};
    color: {palette.text_secondary};
    padding: 10px 20px;
    border-top-left-radius: 6px;
    border-top-right-radius: 6px;
    margin-right: 2px;
}}

QTabBar::tab:selected {{
    background-color: {palette.primary};
    color: {palette.text_on_primary};
}}

QTabBar::tab:hover:!selected {{
    background-color: {palette.surface};
    color: {palette.text_primary};
}}

/* Scroll Bar */
QScrollBar:vertical {{
    background-color: {palette.background};
    width: 12px;
    border-radius: 6px;
}}

QScrollBar::handle:vertical {{
    background-color: {palette.primary};
    border-radius: 6px;
    min-height: 30px;
}}

QScrollBar::handle:vertical:hover {{
    background-color: {palette.primary_light};
}}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
    height: 0px;
}}

QScrollBar:horizontal {{
    background-color: {palette.background};
    height: 12px;
    border-radius: 6px;
}}

QScrollBar::handle:horizontal {{
    background-color: {palette.primary};
    border-radius: 6px;
    min-width: 30px;
}}

/* Label Styling */
QLabel {{
    color: {palette.text_primary};
}}

QLabel[class="secondary"] {{
    color: {palette.text_secondary};
}}

QLabel[class="title"] {{
    font-size: 24px;
    font-weight: bold;
    color: {palette.primary};
}}

QLabel[class="subtitle"] {{
    font-size: 16px;
    color: {palette.text_secondary};
}}

/* Frame Styling */
QFrame {{
    background-color: {palette.surface};
    border-radius: 8px;
}}

QFrame[class="card"] {{
    background-color: {palette.surface};
    border: 1px solid {palette.primary};
    border-radius: 12px;
    padding: 16px;
}}

/* Spin Box */
QSpinBox, QDoubleSpinBox {{
    background-color: {palette.surface};
    border: 2px solid {palette.primary};
    border-radius: 6px;
    padding: 6px 10px;
    color: {palette.text_primary};
}}

QSpinBox::up-button, QDoubleSpinBox::up-button {{
    background-color: {palette.primary};
    border-top-right-radius: 4px;
}}

QSpinBox::down-button, QDoubleSpinBox::down-button {{
    background-color: {palette.primary};
    border-bottom-right-radius: 4px;
}}

/* Menu */
QMenuBar {{
    background-color: {palette.surface};
    color: {palette.text_primary};
    padding: 4px;
}}

QMenuBar::item:selected {{
    background-color: {palette.primary};
    border-radius: 4px;
}}

QMenu {{
    background-color: {palette.surface};
    border: 1px solid {palette.primary};
    border-radius: 6px;
    padding: 4px;
}}

QMenu::item {{
    padding: 8px 24px;
    border-radius: 4px;
}}

QMenu::item:selected {{
    background-color: {palette.primary};
}}

/* Status Bar */
QStatusBar {{
    background-color: {palette.surface};
    color: {palette.text_secondary};
    border-top: 1px solid {palette.primary};
}}

/* Tool Tip */
QToolTip {{
    background-color: {palette.surface};
    color: {palette.text_primary};
    border: 1px solid {palette.primary};
    border-radius: 4px;
    padding: 6px;
}}
"""
