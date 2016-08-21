# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\FdroidTools.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_FdroidTools(object):
    def setupUi(self, FdroidTools):
        FdroidTools.setObjectName(_fromUtf8("FdroidTools"))
        FdroidTools.resize(750, 250)
        self.centralwidget = QtGui.QWidget(FdroidTools)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tableView = QtGui.QTableView(self.centralwidget)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.verticalLayout.addWidget(self.tableView)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        FdroidTools.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(FdroidTools)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        FdroidTools.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(FdroidTools)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        FdroidTools.setStatusBar(self.statusbar)
        self.actionConfig = QtGui.QAction(FdroidTools)
        self.actionConfig.setObjectName(_fromUtf8("actionConfig"))
        self.menuMenu.addAction(self.actionConfig)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(FdroidTools)
        QtCore.QMetaObject.connectSlotsByName(FdroidTools)

    def retranslateUi(self, FdroidTools):
        FdroidTools.setWindowTitle(_translate("FdroidTools", "FdroidTools", None))
        self.menuMenu.setTitle(_translate("FdroidTools", "Menu", None))
        self.actionConfig.setText(_translate("FdroidTools", "exit", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWindow = QtGui.QMainWindow()
    ui = Ui_FdroidTools()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())


