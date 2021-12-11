from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QLineEdit


class LoginUI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI Files/login.ui", self)
        self.Background.setStyleSheet("""
         [objectName^="Background"]
        {
        background-image:url(Resources/Login/LogIn.png)
        }
        
        QLineEdit
        {
            background-color:none;
            border:none;
            font-size:25px
        }
        """)
        self.visibilitypass.setStyleSheet("""
        QCheckBox::indicator:unchecked
        {
         image: url(Resources/visibility_off.png);
        }
        
        QCheckBox::indicator:checked
        {
         image: url(Resources/visibility.png);
        }
        """)

        self.visibilitypass.stateChanged.connect(self.visibility)

    def visibility(self):
        if self.visibilitypass.checkState() == QtCore.Qt.CheckState.Checked:
            self.passfield.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.passfield.setEchoMode(QLineEdit.EchoMode.Password)
