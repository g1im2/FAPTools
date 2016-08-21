#-*-coding:UTF-8-*-
__author__ = 'fxf'

import subprocess,sys
import time
from PyQt4 import QtGui, QtCore
from Screencap import Ui_Screencap

class GetScreencap(QtGui.QWidget,Ui_Screencap):

	def __init__(self,parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.setupUi(self)
		self.num = 0
		self.connect(self.acceptButton,QtCore.SIGNAL("clicked()"),self.on_savecap_clicked)
		self.connect(self.choiceButton,QtCore.SIGNAL("clicked()"),self.on_savefile_clicked)
		self.connect(self.CanelButton,QtCore.SIGNAL("clicked()"),self.on_canel_clicked)
		self.connect(self.installApkLine,QtCore.SIGNAL("returnPressed()"),self.on_savecap_clicked)

	def on_savefile_clicked(self):
		dlg = QtGui.QFileDialog()
		filename = dlg.getSaveFileName(self,'SaveUrl','/','PNG(*.png)')
		self.installApkLine.setText(filename)

	def on_canel_clicked(self):
		self.installApkLine.clear()
		sys.exit()

	def on_savecap_clicked(self):
		p = subprocess.Popen("adb get-state", shell = True,stdout = subprocess.PIPE)
		pi = p.communicate()
		if "unknown" in pi[0]:
			warningWindow = QtGui.QWidget()
			QtGui.QMessageBox.information(warningWindow,u"Error",u"ADB Disconnect")
		else:
			self.acceptButton.setEnabled(False)
			filename = self.installApkLine.text()
			if filename == "":
				filename = "Screencap"
			if '.png' in filename:
				pass
			else:
				filename = str(filename) + '.png'
			sdcardUrl = "/sdcard/fdroidscreencap.png"
			subprocess.call(str("adb shell screencap -p "+sdcardUrl),shell=True)
			subprocess.call(str("adb pull " + sdcardUrl + " " + filename),shell=True)
			self.acceptButton.setEnabled(True)
			if str(self.num) in filename:
				self.installApkLine.setText(filename.split(str(self.num))[0] + str(self.num + 1) + '.png')
			else:
				self.installApkLine.setText(filename.split('.')[0] + str(self.num +1) + '.png')
			self.num += 1

if __name__ == '__main__':
	import sys
	app = QtGui.QApplication(sys.argv)
	FDroidTools = GetScreencap()
	FDroidTools.show()
	sys.exit(app.exec_())