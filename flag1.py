from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QWidget


class flag1UI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI Files/flag1.ui", self)
        self.Background.setStyleSheet("""
        [objectName^="Background"]
        {
            background-image:url(Resources/flagging/background.png)
        }
        
        [objectName^="stepFrame"]
        {
            background-image:url(Resources/flagging/s1.png)
        }
        
        QPushButton
        {
            background-color: none;
            border:none;
        }
        
        QPlainTextEdit
        {
            background-color: rgb(242, 242, 242);
            border:none;
            font-size:19px;
            color: rgb(79, 79, 79)
        }
        
        QLineEdit
        {
            background-color: rgb(242, 242, 242);
            border:none;
            font-size:20px;
            color: rgb(79, 79, 79)
        }
        
        [objectName^="step1"]
        {
            image:url(Resources/flagging/s1_a.png)
        }
        
        [objectName^="step2"]
        {
            image:url(Resources/flagging/s2_d.png)
        }
        
        [objectName^="step3"]
        {
            image:url(Resources/flagging/s3_d.png)
        }
        
        """)

