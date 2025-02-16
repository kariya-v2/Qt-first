import sys
import PySide6.QtCore as Qc
import PySide6.QtWidgets as Qw

# 科目情報を扱うクラスの定義


class Subject():
    def __init__(self, name: str, credits: int, term: str):
        self.name = name        # 科目名
        self.credits = credits  # 単位数
        self.term = term        # 開講期


# 科目情報のインスタンスの生成
subjects = [Subject('国語2', 2, '通年'),
            Subject('微分積分1', 2, '前期'),
            Subject('論理回路1', 1, '後期'),
            Subject('メディアデザイン入門', 2, '後期'),
            Subject('プログラミング1', 2, '後期'),
            Subject('工学基礎実習', 4, '通年')]

# レイアウト設定用のエイリアス
sp = Qw.QSizePolicy.Policy

# GUI MainWindow クラス


class MainWindow(Qw.QMainWindow):

    def __init__(self):

        super().__init__()
        self.setWindowTitle('MainWindow')
        self.setGeometry(100, 50, 640, 100)

        # メインレイアウトの設定
        central_widget = Qw.QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = Qw.QVBoxLayout(central_widget)  # 要素を垂直配置
        main_layout.setAlignment(Qc.Qt.AlignmentFlag.AlignTop)  # 上寄せ
        main_layout.setContentsMargins(15, 10, 10, 10)

        # チェックボックスの生成と設定
        self.checkboxes: list[Qw.QCheckBox] = []
        for sub in subjects:
            cb = Qw.QCheckBox(self)
            cb.setText(f'【{sub.term}】 {sub.name} ( {sub.credits}単位 )')
            cb.setCheckState(Qc.Qt.CheckState.Checked)
            cb.setCursor(Qc.Qt.CursorShape.PointingHandCursor)  # カーソル形状
            # QCheckBox に 動的に subject属性 を追加。
            # VSCode からの型チェック警告を非表示にするため「type: ignore」を記述
            cb.subject = sub  # type: ignore
            cb.stateChanged.connect(self.cb_state_changed)
            self.checkboxes.append(cb)
            main_layout.addWidget(cb)

        # チェックボックス群とラベルの間に 20px スペーサを追加
        spacer = Qw.QSpacerItem(0, 10, sp.Fixed, sp.Fixed)
        main_layout.addSpacerItem(spacer)

        # ラベル
        self.lb_info = Qw.QLabel('', self)
        main_layout.addWidget(self.lb_info)

        # ラベルの表示を更新
        self.cb_state_changed()

    # チェックボックスの状態が変化したときのコールバック関数
    def cb_state_changed(self):
        sum_credits = 0
        for cb in self.checkboxes:
            if cb.isChecked():
                sum_credits += cb.subject.credits  # type: ignore
                cb.setStyleSheet('QCheckBox { color: black; }')
            else:
                cb.setStyleSheet('QCheckBox { color: red; }')
        self.lb_info.setText(f'合計の取得単位数は「{sum_credits}単位」です。')


# 本体
if __name__ == '__main__':
    app = Qw.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
