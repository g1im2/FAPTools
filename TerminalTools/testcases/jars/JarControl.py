#-*-coding:UTF-8-*-
import os

class JarControl(object):
	def __init__( self):
		pass
	
	def push(self, filedir):
		os.system("adb push" + filedir +"")
	
	def start(self, filename, classname):
		os.system("adb shell " + filename +"." + classname+"") 