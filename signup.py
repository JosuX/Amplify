from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QLineEdit


class SignupUI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI Files/signup.ui", self)
        self.Background.setStyleSheet("""
        [objectName^="Background"]
        {
        background-image: url(Resources/Signup/signup.png);
        }
        
        QLineEdit
        {
            background-color:none;
            border:none;
            font-size:20px
        }
        
        QCheckBox::indicator
        {
            width: 30px;
            height: 30px;
        }
        
        QCheckBox::indicator:unchecked
        {
         image: url(Resources/visibility_off.png);
        }
        
        QCheckBox::indicator:checked
        {
         image: url(Resources/visibility.png);
        }
        
        [objectName^="terms"]::indicator:unchecked
        {
         image: none;
        }
        
        [objectName^="terms"]::indicator:checked
        {
         image: url(Resources/check.png);
        }
         """)
        self.p1_cb.stateChanged.connect(self.visibility_p1)
        self.p2_cb.stateChanged.connect(self.visibility_p2)


    def visibility_p1(self):
        if self.p1_cb.checkState() == QtCore.Qt.CheckState.Checked:
            self.pass1_f.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.pass1_f.setEchoMode(QLineEdit.EchoMode.Password)

    def visibility_p2(self):
        if self.p2_cb.checkState() == QtCore.Qt.CheckState.Checked:
            self.pass2_f.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.pass2_f.setEchoMode(QLineEdit.EchoMode.Password)