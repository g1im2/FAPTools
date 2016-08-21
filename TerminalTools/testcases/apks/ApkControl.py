#-*-coding:UTF-8-*-
__author__ = 'fxf'

class ApkControl(object):
	
	def __init__(self):
		pass
	
	def install(self, filename):
		subprocess.call("adb install "+filename)

	def push(self, sourcename, targetdir):
		subprocess.call("adb push " + sourcename + " " + targetdir)