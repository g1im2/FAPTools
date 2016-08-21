#-*-coding:utf-8-*-
__author__ = 'fxf'

import subprocess
import time
from PyQt4 import QtCore

class ScriptHelper(QtCore.QThread):

    def __init__(self,parent = None):
        QtCore.QThread.__init__(self,parent)
        self.currentNum = 0
        self.values = 0

    def run(self):
        try:
            f = open('./runscripts_cache.ini')
            filedir = f.readline()
            f.close()
            #os.remove('./runscripts_cache.ini')
        except IOError:
            print "Can't find install_cache.ini"
        #loop_nums = int(filedir[0])
        self.emit(QtCore.SIGNAL("setProcessBar(int)"), 10)
        f = open(filedir,"r")
        mem = f.readlines()
        f.close()
        for j in range(10):
            for i in mem:
                command = i.split(":")
                if command[0] == "key":
                    subprocess.call("adb shell input keyevent " + command[1])
                elif command[0] == "tap":
                    subprocess.call("adb shell input tap  " + command[1])
                elif command[0] == "swipe":
                    subprocess.call("adb shell input swipe " + command[1])
                elif command[0] == "app":
                    subprocess.call("adb shell am start -n " + command[1])
                elif i == "\n":
                    pass
                time.sleep(int(command[2]))
            self.emit(QtCore.SIGNAL("updateProcessBar(int)"), (j + 1))