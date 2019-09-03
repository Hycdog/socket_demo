# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'socket_server_dev.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, QtNetwork
import socket
import time


class TcpThread(QtCore.QThread):

    signal_connect_received = QtCore.pyqtSignal(str)

    def __init__(self,s):
        super(TcpThread, self).__init__()
        self.s = s
        self.enabled = True

    def bind(self,s):
        self.s = s

    def stop(self):
        self.enabled = False

    def run(self):
        while self.enabled:
            conn, addr = self.s.accept()
            self.signal_connect_received.emit('Connection from ' + addr[0] + '.')
            while True:
                try:
                    msg = conn.recv(1024)
                    if len(msg) == 0:
                        self.signal_connect_received.emit(addr[0] + ' disconnected.')
                        return
                    # if not self.enabled:
                    #     return
                    self.signal_connect_received.emit(str(msg))
                    conn.send(msg.upper())
                except ConnectionResetError:
                    self.signal_connect_received.emit( addr[0]+' disconnected.')
                    return

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
        self.textBrowser.insertHtml(self.gettime()+'<font color="red">(Fail)</font> '+str(err)+'<br>')

    def successlog(self,str):
        self.textBrowser.moveCursor(QtGui.QTextCursor.End)
        self.textBrowser.insertHtml(self.gettime()+'<font color="green">(Success)</font> ' + str + '<br>')

    def infolog(self,str):
        self.textBrowser.moveCursor(QtGui.QTextCursor.End)
        self.textBrowser.insertHtml(self.gettime() + '<font color="blue">(Info)</font> ' + str + '<br>')

    def stopserver(self):
        try:
            self.s.close()
            self.thread.stop()
            self.successlog('Socket server has stopped.')
            self.lineEdit.setEnabled(True)
            self.lineEdit_2.setEnabled(True)
            self.lineEdit_3.setEnabled(True)
            self.lineEdit_4.setEnabled(True)
            self.lineEdit_5.setEnabled(True)
            self.pushButton.disconnect()
            self.pushButton.setText('Start Server')
            self.pushButton.clicked.connect(self.startserver)
        except Exception as e:
            self.errlog(e)


    def startserver(self):
        ip_0 = str(int(self.lineEdit.text()))
        ip_1 = str(int(self.lineEdit_2.text()))
        ip_2 = str(int(self.lineEdit_3.text()))
        ip_3 = str(int(self.lineEdit_4.text()))
        portnum = int(self.lineEdit_5.text())
        self.ip_port = (ip_0+'.'+ip_1+'.'+ip_2+'.'+ip_3, portnum)
        BUFSIZE = 1024
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.bind(self.ip_port)
            self.s.listen(5)
            self.successlog('Socket server is now listening on '+self.ip_port[0]+' port '+str(self.ip_port[1]))
            self.lineEdit.setEnabled(False)
            self.lineEdit_2.setEnabled(False)
            self.lineEdit_3.setEnabled(False)
            self.lineEdit_4.setEnabled(False)
            self.lineEdit_5.setEnabled(False)
            self.pushButton.disconnect()
            self.pushButton.setText('Stop Server')
            self.pushButton.clicked.connect(self.stopserver)
            self.thread = TcpThread(self.s)
            self.thread.signal_connect_received.connect(self.infolog)
            self.thread.start()
        except Exception as e:
            self.errlog(e)
            self.errlog('Socket server failed to start.')



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


        self.pushButton.clicked.connect(self.startserver)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Socket Server"))
        self.lineEdit.setText(_translate("MainWindow", "127"))
        self.label_2.setText(_translate("MainWindow", ":"))
        self.lineEdit_2.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", ":"))
        self.lineEdit_3.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", ":"))
        self.lineEdit_4.setText(_translate("MainWindow", "1"))
        self.label_5.setText(_translate("MainWindow", "Port"))
        self.lineEdit_5.setText(_translate("MainWindow", "9000"))
        self.pushButton.setText(_translate("MainWindow", "Start Server"))


if __name__ == "__main__":
    import sys

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
