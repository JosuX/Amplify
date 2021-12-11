from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QWidget


class sidebarUI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI Files/sidebar.ui", self)
        self.Background.setStyleSheet("""
        QFrame
        {
            image: url(Resources/sidebar/sb.png)
        }
        
        [objectName^="b_H"]::indicator::unchecked
        {
            image: url(Resources/sidebar/H_0.png)
        }
        
        [objectName^="b_H"]::indicator::unchecked::hover
        {
            image: url(Resources/sidebar/H_1.png)
        }
        
        [objectName^="b_H"]::indicator::checked
        {
            image: url(Resources/sidebar/H_2.png)
        }
        
        [objectName^="b_R"]::indicator::unchecked
        {
            image:  url(Resources/sidebar/R_0.png)
        }
        
        [objectName^="b_R"]::indicator::unchecked::hover
        {
            image:  url(Resources/sidebar/R_1.png)
        }
        
        [objectName^="b_R"]::indicator::checked
        {
            image: url(Resources/sidebar/R_2.png)
        }
        
        
        [objectName^="b_F"]::indicator::unchecked
        {
            image:  url(Resources/sidebar/F_0.png)
        }
        
        [objectName^="b_F"]::indicator::unchecked::hover
        {
            image:  url(Resources/sidebar/F_1.png)
        }
        
        [objectName^="b_F"]::indicator::checked
        {
            image: url(Resources/sidebar/F_2.png)
        }
         """)
        self.b_F.clicked.connect(self.goto_flags)
        self.b_H.clicked.connect(self.goto_home)
        self.b_R.clicked.connect(self.goto_raise)

    def goto_home(self):
        print("Transfer to Home page")

    def goto_raise(self):
        print("Transfer to Raise a Flag page")

    def goto_flags(self):
        print("Transfer to My Flags page")
