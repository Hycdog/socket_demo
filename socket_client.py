# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'socket_server_dev.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, QtNetwork
import socket
import time


class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)



class Ui_MainWindow(QtWidgets.QMainWindow):


    def gettime(self):
        now = time.strftime("%Y/%m/%d-%H:%M:%S", time.localtime())
        return now


    def errlog(self,err):
        self.textBrowser.moveCursor(QtGui.QTextCursor.End)
        self.textBrowser.insertHtml(self.gettime()+'<font color="red">(Fail)</font> ' + str(err) + '<br>')

    def successlog(self,str):
        self.textBrowser.moveCursor(QtGui.QTextCursor.End)
        self.textBrowser.insertHtml(self.gettime()+'<font color="green">(Success)</font> ' + str + '<br>')

    def infolog(self,str):
        self.textBrowser.moveCursor(QtGui.QTextCursor.End)
        self.textBrowser.insertHtml(self.gettime() + '<font color="blue">(Info)</font> ' + str + '<br>')

    def disconnect(self):
        try:
            self.hidesend()
            self.s.close()
            self.successlog('Disconnected.')
            self.lineEdit.setEnabled(True)
            self.lineEdit_2.setEnabled(True)
            self.lineEdit_3.setEnabled(True)
            self.lineEdit_4.setEnabled(True)
            self.lineEdit_5.setEnabled(True)
            self.pushButton.disconnect()
            self.pushButton.setText('Connect')
            self.pushButton.clicked.connect(self.connectserver)
        except Exception as e:
            self.errlog(e)


    def sendmsg(self):
        msg = self.lineEdit_send.text()
        if len(msg) == 0:
            return
        try:
            self.s.send(msg.encode('utf-8'))
            self.successlog('Message sent.')
        except Exception as e:
            self.errlog(e)
            self.errlog(MyError('Message Failed to send.'))

    def connectserver(self):
        ip_0 = str(int(self.lineEdit.text()))
        ip_1 = str(int(self.lineEdit_2.text()))
        ip_2 = str(int(self.lineEdit_3.text()))
        ip_3 = str(int(self.lineEdit_4.text()))
        portnum = int(self.lineEdit_5.text())
        self.ip_port = (ip_0+'.'+ip_1+'.'+ip_2+'.'+ip_3, portnum)
        BUFSIZE = 1024
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.settimeout(2)
            ret = self.s.connect_ex(self.ip_port)
            if ret != 0:
                if ret == 11:
                    raise MyError('Connection timed out after '+str(self.s.gettimeout())+' secs.')
                elif ret == 111:
                    raise MyError('Connection failed.')
                else:
                    raise MyError('Unknown Error')

            self.s.settimeout(None)
            self.successlog('Connected to socket server on '+self.ip_port[0]+' port '+str(self.ip_port[1]))
            self.lineEdit.setEnabled(False)
            self.lineEdit_2.setEnabled(False)
            self.lineEdit_3.setEnabled(False)
            self.lineEdit_4.setEnabled(False)
            self.lineEdit_5.setEnabled(False)
            self.pushButton.disconnect()
            self.pushButton.setText('Disconnect')
            self.pushButton.clicked.connect(self.disconnect)
            self.enablesend()
        except Exception as e:
            self.errlog(e)
            self.errlog(MyError('Failed to connect to socket server.'))



    def hidesend(self):
        self.lineEdit_send.setVisible(False)
        self.pushButton_send.setVisible(False)

    def enablesend(self):
        self.lineEdit_send.setVisible(True)
        self.pushButton_send.setVisible(True)

    def checkchanged(self,obj):
        print(obj)

    def setupUi(self):
        self.setObjectName("self")
        self.resize(800, 600)

        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 0, 761, 531))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 50))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout.addWidget(self.lineEdit_4)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_5.setMaximumSize(QtCore.QSize(16777215, 50))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout.addWidget(self.lineEdit_5)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.gridLayoutWidget)
        self.tabWidget.setObjectName("tabWidget")

        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")

        self.gridLayout_tab_1 = QtWidgets.QGridLayout(self.tab_1)
        self.gridLayout_tab_1.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_tab_1.setObjectName("gridLayout_tab_1")

        self.textBrowser = QtWidgets.QTextBrowser(self.tab_1)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_tab_1.addWidget(self.textBrowser, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_1, "logs")

        self.gridLayout.addWidget(self.tabWidget, 2, 1, 1, 1)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_send = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_send.setMaximumSize(QtCore.QSize(16777215, 50))
        self.lineEdit_send.setObjectName("lineEdit_send")
        self.horizontalLayout_2.addWidget(self.lineEdit_send)
        self.pushButton_send = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_send.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_send.setObjectName("pushButton_send")
        self.horizontalLayout_2.addWidget(self.pushButton_send)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 1, 1, 1)
        self.hidesend()

        self.lineEdit.setValidator(QtGui.QIntValidator(0,255))
        self.lineEdit.setMaxLength(3)
        self.lineEdit_2.setValidator(QtGui.QIntValidator(0, 255))
        self.lineEdit_2.setMaxLength(3)
        self.lineEdit_3.setValidator(QtGui.QIntValidator(0, 255))
        self.lineEdit_3.setMaxLength(3)
        self.lineEdit_4.setValidator(QtGui.QIntValidator(0, 255))
        self.lineEdit_4.setMaxLength(3)
        self.lineEdit_5.setValidator(QtGui.QIntValidator(0, 65535))
        self.lineEdit_5.setMaxLength(5)
        self.retranslateUi()


        self.pushButton.clicked.connect(self.connectserver)
        self.pushButton_send.clicked.connect(self.sendmsg)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Socket Client"))
        self.lineEdit.setText(_translate("MainWindow", "127"))
        self.label_2.setText(_translate("MainWindow", ":"))
        self.lineEdit_2.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", ":"))
        self.lineEdit_3.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", ":"))
        self.lineEdit_4.setText(_translate("MainWindow", "1"))
        self.label_5.setText(_translate("MainWindow", "Port"))
        self.lineEdit_5.setText(_translate("MainWindow", "9000"))
        self.pushButton.setText(_translate("MainWindow", "Connect"))
        self.pushButton_send.setText(_translate("MainWindow", "Sendmsg"))


if __name__ == "__main__":
    import sys

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
