from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QWidget


class firstUI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI Files/firstflag.ui", self)
        self.background.setStyleSheet("""
        [objectName^="background"]
        {
            background-image: url(Resources/Misc/myflag_bg.png)
        }
        """)
