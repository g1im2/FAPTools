#-*-coding:utf-8-*-
__author__ = 'fxf'

from PyQt4 import QtGui, QtCore
from Ui.FdroidTools import Ui_FdroidTools

class Main(QtGui.QMainWindow, Ui_FdroidTools):

    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.statusbar.showMessage("this is statusbar")
        model = QtGui.QStandardItemModel(4,2,self.tableView)
        self.tableView.setModel(model)
        self.tableView.show()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FdroidTools = Main()
    FdroidTools.show()
    sys.exit(app.exec_())
