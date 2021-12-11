from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QWidget



class flag3UI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI Files/flag3.ui", self)
        self.Background.setStyleSheet("""
        [objectName^="Background"]
        {
            background-image:url(Resources/flagging/background.png)
        }
        
        [objectName^="stepFrame"]
        {
            background-image:url(Resources/flagging/s3.png)
        }
        
        QPushButton
        {
            background-color: none;
            border:none;
        }
        
        [objectName^="step1"]
        {
            image:url(Resources/flagging/s1_d.png)
        }
        
        [objectName^="step2"]
        {
            image:url(Resources/flagging/s2_d.png)
        }
        
        [objectName^="step3"]
        {
            image:url(Resources/flagging/s3_a.png)
        }
        
        """)