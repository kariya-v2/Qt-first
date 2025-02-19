# main.py
import sys
from PySide6.QtWidgets import QApplication
from todo_calendar import TodoCalendar


def main():
    app = QApplication(sys.argv)
    window = TodoCalendar()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
