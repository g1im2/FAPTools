#-*-coding:UTF-8-*-
__author__ = 'fxf'
import os

class DirControl(object):
	
	def __init__(self):
		pass
		
	def win_mkdir(self,url,dirname):
		os.mkdir(url+"\\"+dirname)
	
	def linux_mkdir(self,url,dirname):
		os.system("mkdir "+url+" "+dirname)