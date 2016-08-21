#-*-coding:UTF-8-*-
__author__ = 'fxf'

from fbin.Run_Tools import Run_Tools

class Interface_Tools(object):
	
	def __init__(self):
		pass
	
	def mercury(self,item):
		mercury = Run_Tools()
		if (item == 'start'):
			mercury.start_mercury()
		else:
			print("error input")
	
	def chkbugreport(self):
		chkbugreport = Run_Tools()
		chkbugreport.check_bugreport()

	def chkpermission(self):
		chkpermission = Run_Tools()
		chkpermission.get_apk_androidmanifest()