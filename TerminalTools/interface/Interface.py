#-*-coding:UTF-8-*-
__author__ = 'fxf'

import os

from fbin.Run_Operation import Run_Operation
from testcases.scripts.Install_Apks import Install_Apks
from testcases.scripts.Product_Diag import Product_Diag

class Interface(object):

	def __init__(self):
		pass

	def play_testcases(self,dir,file_ini):
		play = Run_Operation()
		play.autoplay(dir,file_ini)

	def install_apk(self):
		install = Install_Apks()
		print "put apks in D:\\apks and run this scripts\nAnd you must connect adb with product first"
		try:
			install.install()
		except WindowsError:
			print 'D:\\apks was no exists'

	def product_diag(self,item):
		diag = __import__(testcase)
		if item == 'only':
			diag.diagtest()
		elif item == 'upgrade':
			diag.upgrade_reboot()
		elif item == 'both':
			diag.diagtest()
			diag.upgrade_reboot()
		elif item == 'all':
			diag.copy_apk()
			diag.diagtest()
			diag.upgrade_reboot()
		else:
			print 'input error'