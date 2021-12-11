from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QWidget



class homeUI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI Files/home.ui", self)
        self.ScrollArea.setStyleSheet("""
        QWidget
        {
            background-color: rgb(238, 240, 242)
        }
        
        [objectName^="card"]
        {
            color: white;
            background-color: white;
            border-radius: 30px;
            border: none;
        }
        
        [objectName^="image"]
        {
            border-top-left-radius: 30px;
            border-top-right-radius: 30px;
            image: url(Resources/Home/ci_1.png);
        }
        
        [objectName^="image_3"]
        {
            image: url(Resources/Home/ci_2.png);
        }
        
        [objectName^="image_4"]
        {
            image: url(Resources/Home/ci_3.png);
        }
        
        [objectName^="topframe"]
        {
            border-top-left-radius: 30px;
            border-top-right-radius: 30px;
        }
        
        [objectName^="title"]
        {
            font-weight: bold;
            font-size: 48px;
            color:white;
            background-color: none;
            font-family: "Arial";
        
        }
        
        [objectName^="icon_loc"]
        {
            background-color: none;
            image: url(Resources/Home/i_location.png);
        }
        
        [objectName^="t_loc"]
        {
            background-color: none;
            color: white;
            font-weight:bold;
            font-size: 17px;
        }
        
        QLabel
        {
            background-color:none;
        }
        
        [objectName^="desc"]
        {
            color: black;
            font-size: 20px
        }
        
        [objectName^="details"]
        {
            border-bottom-left-radius: 30px;
            border-bottom-right-radius: 30px;
            background-image: url(Resources/Home/details.png)
        }
        
        QRadioButton
        {
            background-color: none;
            font-size: 18px;
        }
        
        [objectName^="like"]::indicator::checked
        {
            image: url(Resources/Home/l_0.png)
        }
        
        
        [objectName^="like"]::indicator::unchecked
        {
            image: url(Resources/Home/l_1.png)
        }
        
        [objectName^="dislike"]::indicator::checked
        {
            image: url(Resources/Home/d_0.png)
        }
        
        [objectName^="dislike"]::indicator::unchecked
        {
            image: url(Resources/Home/d_1.png)
        }
        
        [objectName^="description"]
        {
            font-size:18px;
            background-color: none;
            font-weight: 300;
            font-family: "Open Sans";
            color: rgb(138, 138, 138)
        }
        
        [objectName^="poster"]
        {
            font-size:18px;
            background-color: none;
            font-weight: 500;
            font-style:italic;
        }
        
        [objectName^="posted"]
        {
            font-size:18px;
            background-color: none;
            font-weight: 500;
            font-style:italic;
        }
        
        [objectName^="Header"]
        {
            background-image: url(Resources/Home/header.png)
        }
        
        QPushButton
        {
            background-color: none;
            border: none;
        }
        
        [objectName^="ico_cat"]
        {
            image: url(Resources/Filter/blue.png)
        }
        
        [objectName^="ico_prio"]
        {
            image: url(Resources/Filter/pink.png)
        }
        
        [objectName^="ico_status"]
        {
            image: url(Resources/Filter/red.png)
        }
        
        [objectName^="ico_status_4"]
        {
            image: url(Resources/Filter/yel.png)
        }
        
         """)
