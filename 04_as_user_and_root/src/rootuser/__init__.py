from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout


class MyDialog(QDialog):
    def __init__(self, text: str):
        super().__init__()
        wdg = QLabel(self, text=text)
        layout = QVBoxLayout(self)
        layout.addWidget(wdg)


def get_main_window(text: str):
    return MyDialog(text)
