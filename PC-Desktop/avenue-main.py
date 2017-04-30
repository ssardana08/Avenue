# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AvenueUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import socket
import pyautogui as pyag

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(439, 435)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.btn2 = QtGui.QToolButton(self.centralwidget)
        self.btn2.setMinimumSize(QtCore.QSize(50, 50))
        self.btn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../ui_files/settings_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn2.setIcon(icon)
        self.btn2.setIconSize(QtCore.QSize(30, 30))
        self.btn2.setObjectName(_fromUtf8("btn2"))
        self.gridLayout_2.addWidget(self.btn2, 0, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.btn3 = QtGui.QToolButton(self.centralwidget)
        self.btn3.setMinimumSize(QtCore.QSize(50, 50))
        self.btn3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../ui_files/help_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn3.setIcon(icon1)
        self.btn3.setIconSize(QtCore.QSize(30, 30))
        self.btn3.setObjectName(_fromUtf8("btn3"))
        self.gridLayout_2.addWidget(self.btn3, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 3, 0, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)

        # TextEdit Column
        self.txtedit = QtGui.QLineEdit(self.centralwidget)
        self.txtedit.setObjectName(_fromUtf8("txtedit"))
        self.gridLayout_4.addWidget(self.txtedit, 0, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.gridLayout.addLayout(self.gridLayout_4, 1, 0, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("../ui_files/logo._with_title.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))

        #Button Start
        self.btn1 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn1.sizePolicy().hasHeightForWidth())
        self.btn1.setSizePolicy(sizePolicy)
        self.btn1.setMinimumSize(QtCore.QSize(101, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn1.setFont(font)
        self.btn1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn1.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(52, 152, 219);\n"
"border-radius: 15px;\n"
"border-width: 0px;"))
        self.btn1.setFlat(False)
        self.btn1.setObjectName(_fromUtf8("btn1"))
        self.gridLayout_3.addWidget(self.btn1, 1, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.gridLayout.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 439, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btn1.clicked.connect(self.server)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Avenue", None))
        self.btn2.setText(_translate("MainWindow", "Settings", None))
        self.btn3.setText(_translate("MainWindow", "...", None))
        self.label_2.setText(_translate("MainWindow", "IP Address", None))
        self.btn1.setText(_translate("MainWindow", "Start", None))


    def server(self):

        self.host = socket.gethostbyname(socket.gethostname())
        self.txtedit.setText('host')
        self.port = 5000
        print("Server's IP Address:"+self.host)

        self.mySocket = socket.socket()
        self.mySocket.bind((self.host,self.port))

        self.mySocket.listen(1)
        self.conn, self.addr = self.mySocket.accept()
        print ("Connection from: " + str(self.addr))
        while True:
            self.data = conn.recv(1024).decode()
            if not self.data:
                break
            print ("from connected  user: " + str(data))
            if (self.data == 'b!'):
                pyag.press('left')
            elif (self.data == 'd!'):
                pyag.press('right')
            elif (self.data == 'a!'):
                pyag.hotkey('shift','f5')
            elif (self.data == 'c!'):
                pyag.press('esc')




        conn.close()
        


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

