# todo_calendar.py
import json
from PySide6.QtWidgets import (
    QMainWindow, QVBoxLayout, QWidget,
    QListWidget, QLineEdit, QPushButton,
    QMenu, QColorDialog
)
from PySide6.QtCore import Qt, QDate  # QDateをインポート
from custom_calendar import CustomCalendar


class TodoCalendar(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("カレンダーとTo-Doリスト")
        self.setGeometry(100, 100, 400, 300)

        self.calendar = CustomCalendar(self)
        self.todo_list = QListWidget()
        self.todo_input = QLineEdit()
        self.add_button = QPushButton("追加")

        layout = QVBoxLayout()
        layout.addWidget(self.calendar)
        layout.addWidget(self.todo_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.todo_list)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.add_button.clicked.connect(self.add_todo)
        self.calendar.clicked.connect(self.load_todos)

        self.todo_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.todo_list.customContextMenuRequested.connect(
            self.show_context_menu)

        self.todos = {}
        self.load_data()  # データをロードします

    def add_todo(self):
        date = self.calendar.selectedDate()
        todo_text = self.todo_input.text().strip()

        if todo_text:
            if date not in self.todos:
                self.todos[date] = []
                self.calendar.add_todo_date(date)
            self.todos[date].append(todo_text)
            self.todo_input.clear()
            self.load_todos(date)
            self.calendar.update()
            self.save_data()  # データを保存

    def show_context_menu(self, pos):
        item = self.todo_list.itemAt(pos)
        if item is None:
            return

        menu = QMenu()
        change_color_action = menu.addAction("色を変更")
        delete_action = menu.addAction("削除")

        action = menu.exec_(self.todo_list.viewport().mapToGlobal(pos))

        if action == change_color_action:
            self.change_color(item)
        elif action == delete_action:
            self.delete_todo(item)

    def change_color(self, item):
        new_color = QColorDialog.getColor()
        if new_color.isValid():
            item.setForeground(new_color)

    def delete_todo(self, item):
        date = self.calendar.selectedDate()
        self.todos[date].remove(item.text())
        if not self.todos[date]:
            del self.todos[date]
            self.calendar.dates_with_todos.discard(date)
        self.load_todos(date)
        self.calendar.update()
        self.save_data()  # データを保存

    def load_todos(self, date=None):
        if date is None:
            date = self.calendar.selectedDate()

        self.todo_list.clear()  # リストをクリア
        if date in self.todos:  # 日付にTo-Doがあるか確認
            for todo in self.todos[date]:
                self.todo_list.addItem(todo)  # To-Doをリストに追加

    def load_data(self):
        try:
            with open("todos.json", "r", encoding="utf-8") as f:
                contents = f.read().strip()
                if contents:  # 内容がある場合
                    # 内容を辞書としてデコードし、各日付をQDateに変換
                    loaded_todos = json.loads(contents)
                    self.todos = {QDate.fromString(
                        date_str, "yyyy-MM-dd"): todos for date_str, todos in loaded_todos.items()}
                else:
                    self.todos = {}  # 空のファイルの場合
        except FileNotFoundError:
            self.todos = {}  # ファイルが見つからなければ空の辞書を作成
        except json.JSONDecodeError:
            print("JSONファイルの読み込み中にエラーが発生しました。")
            self.todos = {}  # 読み込みエラーの場合も空の辞書を設定

    def save_data(self):
        with open("todos.json", "w", encoding="utf-8") as f:
            # 辞書を保存する際に日付を文字列に変換
            json.dump({date.toString(
                "yyyy-MM-dd"): self.todos[date] for date in self.todos}, f, ensure_ascii=False, indent=4)

    def closeEvent(self, event):
        """ウィンドウが閉じられるときにデータを保存します。"""
        self.save_data()  # データを保存
        event.accept()  # ウィンドウの閉じる処理を続行
