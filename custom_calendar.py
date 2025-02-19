# custom_calendar.py
from PySide6.QtWidgets import QCalendarWidget
from PySide6.QtGui import QPen
from PySide6.QtCore import Qt


class CustomCalendar(QCalendarWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dates_with_todos = set()

    def add_todo_date(self, date):
        self.dates_with_todos.add(date)

    def paintCell(self, painter, rect, date):
        super().paintCell(painter, rect, date)

        if date in self.dates_with_todos:
            pen = QPen(Qt.red, 1, Qt.SolidLine)
            painter.setPen(pen)
            painter.drawLine(rect.left(), rect.bottom(),
                             rect.right(), rect.bottom())
