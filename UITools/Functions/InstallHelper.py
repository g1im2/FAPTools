#-*-coding:utf-8-*-
__author__ = 'fxf'

from PyQt4 import QtCore
import subprocess
import os

class InstallHelper(QtCore.QThread):

    def __init__(self, parent= None):
        QtCore.QThread.__init__(self, parent)

    def run(self, filedir):
        values = 0
        filelists = []
        fileNums = os.listdir(filedir)
        for lines in fileNums:
            if '.apk' in lines:
                self.currentNum += 1
                filelists.append(lines)
        self.emit(QtCore.SIGNAL("setProcessBar(int)"), self.currentNum)
        if filedir[-1] != "\\":
            filedir = filedir + "\\"
        for apk in filelists:
            subprocess.call(str("adb install " + filedir + apk), shell=True)
            values += 1
            self.emit(QtCore.SIGNAL("updateProcessBar(int)"), values)
