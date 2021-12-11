import os
import sys
import threading
from time import sleep

from PyQt5 import QtCore
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QButtonGroup, QFileDialog

import alldone
import firstflag
import flag1
import flag2
import flag3
import home
import login
import signup
import sidebar
import filters
from php_req import flask_server

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

class MapWidget(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.load(QUrl.fromLocalFile("/templates/map.html"))

    def keyReleaseEvent(self, e):
        window.sidebar_w = self.focusProxy()
        QApplication.postEvent(window.sidebar_w, e)

class Done_holder(alldone.doneUI):
    def __init__(self):
        super().__init__()
        self.exit.clicked.connect(self.exitf)
        self.go.clicked.connect(self.conf)

    def exitf(self):
        window.close()

    def conf(self):
        window.setCentralWidget(window.sidebar_w)
        self.sidebar_w.horizontalLayout.addWidget(self.home_w)

class Flag_3(flag3.flag3UI):
    def __init__(self):
        super().__init__()
        self.confirm_but.clicked.connect(self.conf)
        self.back_but.clicked.connect(self.back)

    def conf(self):
        window.temp3 = window.flag3_w
        window.flag3_w = window.temp3
        window.setCentralWidget(window.done)


    def back(self):
        window.sidebar_w.horizontalLayout.itemAt(0).widget().setParent(None)
        window.temp3 = window.flag3_w
        window.flag3_w = window.temp3
        window.sidebar_w.horizontalLayout.addWidget(window.temp2)

class Flag_2(flag2.flag2UI):
    def __init__(self):
        super().__init__()
        self.selectedfiles = None
        self.next_but.clicked.connect(self.next)
        self.back_but.clicked.connect(self.back)
        self.choosefile.clicked.connect(self.upload)
        self.gps.clicked.connect(self.setloc)

    def setloc(self):
        pass


    def upload(self):
        fname = QFileDialog.getOpenFileName(self, 'Upload file',
                                            'c:\\', "Image files (*.jpg *.gif)")
        self.selectedfiles = os.path.basename(fname[0])
        self.filename.setText(self.selectedfiles)

    def back(self):
        window.sidebar_w.horizontalLayout.itemAt(0).widget().setParent(None)
        window.temp2 = window.flag2_w
        window.flag2_w = window.temp2
        window.sidebar_w.horizontalLayout.addWidget(window.temp1)

    def next(self):
        window.sidebar_w.horizontalLayout.itemAt(0).widget().setParent(None)
        window.temp2 = window.flag2_w
        window.flag2_w = window.temp2
        window.sidebar_w.horizontalLayout.addWidget(window.flag3_w)

class Flag_1(flag1.flag1UI):
    def __init__(self):
        super().__init__()
        self.next_but.clicked.connect(self.next)

    def next(self):
        window.sidebar_w.horizontalLayout.itemAt(0).widget().setParent(None)
        window.temp1 = window.flag1_w
        window.flag1_w = window.temp1
        window.sidebar_w.horizontalLayout.addWidget(window.flag2_w)


class HomeWindow(home.homeUI):
    def __init__(self):
        super().__init__()
        self.cl_button.clicked.connect(self.changeLoc)
        self.filter_button.clicked.connect(self.open_filter)
        self.like.clicked.connect(self.addlike)
        self.like_3.clicked.connect(self.addlike_3)

    def addlike(self):
        self.like.setText("88")

    def addlike_3(self):
        self.like_3.setText("149")

    def changeLoc(self):
        window.sidebar_w.horizontalLayout.itemAt(0).widget().setParent(None)
        window.flag1_w = flag1.flag1UI()
        window.sidebar_w.horizontalLayout.addWidget(window.map)

    def open_filter(self):
        window.setCentralWidget(window.map)

class SideBar(sidebar.sidebarUI):
    def __init__(self):
        super().__init__()
        self.b_F.clicked.connect(self.goto_flags)
        self.b_H.clicked.connect(self.goto_home)
        self.b_R.clicked.connect(self.goto_raise)

    def keyReleaseEvent(self, e):
        if e.key() == 16777220:
            window.sidebar_w.horizontalLayout.itemAt(0).widget().setParent(None)
            window.map = MapWidget()
            window.sidebar_w.horizontalLayout.addWidget(window.home_w)

    def goto_home(self):
        self.horizontalLayout.itemAt(0).widget().setParent(None)
        window.home_w = HomeWindow()
        self.horizontalLayout.addWidget(window.home_w)

    def goto_raise(self):
        self.horizontalLayout.itemAt(0).widget().setParent(None)
        window.flag1_w = Flag_1()
        self.horizontalLayout.addWidget(window.flag1_w)

    def goto_flags(self):
        self.horizontalLayout.itemAt(0).widget().setParent(None)
        window.myflag = firstflag.firstUI()
        self.horizontalLayout.addWidget(window.myflag)

class RegScene(signup.SignupUI):
    def __init__(self):
        super().__init__()
        self.login_b.clicked.connect(self.login)
        self.signup_b.clicked.connect(self.signup)
        self.p1_cb.stateChanged.connect(self.visibility_p1)
        self.p2_cb.stateChanged.connect(self.visibility_p2)

    def login(self):
        window.setCentralWidget(window.log_w)
        window.signup_w = RegScene()

    def signup(self):
        print(self.pass1_f.text())

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

class LoginScene(login.LoginUI):
    def __init__(self):
        super().__init__()
        self.loginbut.clicked.connect(self.login)
        self.signupbut.clicked.connect(self.signup)

    def login(self):
        if self.EmailField.text() == "johndoe@domain.com" and self.passfield.text() == "123123":
            window.setCentralWidget(window.sidebar_w)

    def signup(self):
        window.setCentralWidget(window.signup_w)
        window.log_w = LoginScene()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.temp1 = None
        self.temp2 = None
        self.temp3 = None
        self.setWindowTitle("Thingy")
        self.setGeometry(0,0,1440,1024)
        self.filters_w = filters.FiltersUI()
        self.myflag = firstflag.firstUI()
        self.map = MapWidget()
        self.log_w = LoginScene()
        self.signup_w = RegScene()
        self.sidebar_w = SideBar()
        self.home_w = HomeWindow()
        self.flag1_w = Flag_1()
        self.flag2_w = Flag_2()
        self.flag3_w = Flag_3()
        self.done = Done_holder()
        self.sidebar_w.horizontalLayout.addWidget(self.home_w)
        self.setCentralWidget(self.log_w)

if __name__ == '__main__':
    threading.Thread(target=lambda: flask_server.run(debug=True, use_reloader=False)).start()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()