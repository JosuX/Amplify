from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QWidget


class FiltersUI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI Files/filters.ui", self)
        self.Background.setStyleSheet("""
        [objectName^="Background"]
        {
            background-image: url(Resources/Filter/filters_bg.png)
        }
        
        QSlider:groove:horizontal
        {
            height: 2px; 
            background: rgb(52, 157, 254);
        }
        
        QSlider::handle:horizontal {
            background:rgb(52, 157, 254);
            width: 18px;
            margin: -9px 0;
            border-radius: 9px;
        }
        
        [objectName^="RadiusValue"]
        {
            font-size: 25px;
            background-color: rgb(255, 255, 255);
        }
        
        QComboBox
        {
            border: none;
            font-size: 19px;
            padding-left: 15px;
            background-image: url(Resources/Filter/dropdown.png);
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
        
        [objectName^="d_cat"]
        {
            font-size: 16px;
        }
        
        QPushButton
        {
            background-color: none;
            border:none;
        }
         """)
        self.RadiusSlider.valueChanged.connect(self.updateVal)

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
        self.d_stat.addItem(icon4, " Hot")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Resources/Filter/yel.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.d_stat.addItem(icon5, " New")

    def updateVal(self):
        value = self.RadiusSlider.value() * .5
        if value > 10:
            self.RadiusValue.setText("Unlimited")
        else:
            self.RadiusValue.setText(str(value) + " km")

        return value