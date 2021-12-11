from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class doneUI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI Files/confirm_message.ui", self)
        self.background.setStyleSheet("""
        [objectName^="background"]
        {
            background-image: url(Resources/Misc/alldone_bg.png)
        }
        
        QPushButton
        {
            background-color: none;
            border: none;
        }
        """)


