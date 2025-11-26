import sys
from pathlib import Path

from PySide6.QtCore import qInstallMessageHandler
from PySide6.QtWidgets import QApplication

# Ensure src is importable
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from style_loader import build_application_qss  # type: ignore
from theme import ThemeMode  # type: ignore


def qt_handler(mode, context, message):  # pragma: no cover - debugging helper
    print("QT:", message)


def main() -> None:
    qInstallMessageHandler(qt_handler)
    app = QApplication(sys.argv)
    qss = build_application_qss(mode=ThemeMode.LIGHT)
    app.setStyleSheet(qss)


if __name__ == "__main__":
    main()
