from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QWidget



class flag2UI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI Files/flag2.ui", self)
        self.Background.setStyleSheet("""
        [objectName^="Background"]
        {
            background-image:url(Resources/flagging/background.png)
        }
        
        [objectName^="stepFrame"]
        {
            background-image:url(Resources/flagging/s2.png)
        }
        
        QPushButton
        {
            background-color: none;
            border:none;
        }
        
        QLineEdit
        {
            background-color: rgb(242, 242, 242);
            border:none;
            font-size:20px;
            color: rgb(79, 79, 79)
        }
        
        [objectName^="filename"]
        {
            font-size: 15px;
        }
        
        QComboBox
        {
            border: none;
            font-size: 19px;
            padding-left: 15px;
            background-color:rgba(255, 255, 255, 0);
            icon-size: 20px
        }
        
        QComboBox::drop-down
        {
            image: none;
            border-radius: 10px;
        }
        
        QComboBox QAbstractItemView
        {
            border-radius: 10px;
            background-color: rgb(255, 255, 255);
        }
        
        [objectName^="step1"]
        {
            image:url(Resources/flagging/s1_d.png)
        }
        
        [objectName^="step2"]
        {
            image:url(Resources/flagging/s2_a.png)
        }
        
        [objectName^="step3"]
        {
            image:url(Resources/flagging/s3_d.png)
        }
        
        """)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resources/Filter/blue.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.d_cat.addItem(icon, " Peacekeeping")
        self.d_cat.addItem(icon, " Land Issue")
        self.d_cat.addItem(icon, " Sanitation")
        self.d_cat.addItem(icon, " Electricity")
        self.d_cat.addItem(icon, " Water Issue")
        self.d_cat.addItem(icon, " Health")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Resources/Filter/red.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.d_prio.addItem(icon1, " Emergency")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Resources/Filter/pink.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.d_prio.addItem(icon2, " Urgent")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Resources/Filter/green.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.d_prio.addItem(icon3, " Low")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Resources/Filter/red.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

