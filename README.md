# QtLayoutAndStylingTemplate

A comprehensive Qt (PyQt6) template demonstrating how to set up styling, layouts, and color themes for a Qt application.

## Features

- **Multiple Layout Types**: Examples of QVBoxLayout, QHBoxLayout, QGridLayout, and QFormLayout
- **Color Theme System**: Pre-defined themes (Dark, Light, Ocean, Forest) with easy switching
- **Qt Style Sheets (QSS)**: Complete stylesheet generation based on color palettes
- **Widget Showcase**: Demonstrations of various styled Qt widgets
- **Color Palette Visualization**: Visual display of theme colors

## Installation

```bash
# Clone the repository
git clone https://github.com/magnussimonsen/QtLayoutAndStylingTemplate.git
cd QtLayoutAndStylingTemplate

# Install dependencies
pip install -r requirements.txt
```

## Usage

Run the main application:

```bash
python main.py
```

### Using the Color Theme System

```python
from src.colors import get_theme, get_available_themes
from src.stylesheet import generate_stylesheet

# Get available themes
themes = get_available_themes()  # ['dark', 'light', 'ocean', 'forest']

# Get a specific theme palette
palette = get_theme('dark')

# Generate a stylesheet from the palette
stylesheet = generate_stylesheet(palette)

# Apply to your application
app.setStyleSheet(stylesheet)
```

### Creating Custom Themes

```python
from src.colors import ColorPalette, THEMES

# Define a custom theme
custom_theme = ColorPalette(
    primary="#FF5722",
    primary_light="#FF8A50",
    primary_dark="#C41C00",
    secondary="#2196F3",
    secondary_light="#64B5F6",
    secondary_dark="#1565C0",
    accent="#FFC107",
    background="#121212",
    surface="#1E1E1E",
    text_primary="#FFFFFF",
    text_secondary="#B0B0B0",
    text_on_primary="#FFFFFF",
    error="#F44336",
    success="#4CAF50",
    warning="#FF9800",
)

# Add to available themes
THEMES['custom'] = custom_theme
```

## Project Structure

```
QtLayoutAndStylingTemplate/
├── main.py              # Application entry point
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── src/
    ├── __init__.py     # Package initialization
    ├── colors.py       # Color palette definitions and themes
    ├── layouts.py      # Layout example widgets
    └── stylesheet.py   # QSS stylesheet generator
```

## Available Themes

| Theme  | Description                                      |
|--------|--------------------------------------------------|
| Dark   | Modern dark theme with purple/indigo accents     |
| Light  | Clean light theme with subtle colors             |
| Ocean  | Deep blue theme with cyan accents                |
| Forest | Green nature-inspired theme                      |

## Requirements

- Python 3.8+
- PyQt6 >= 6.6.0

## License

MIT License - See LICENSE file for details.
