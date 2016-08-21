#-*-coding=UTF-8-*-
__author__ = 'fxf'

import os

class GetTestcases(object):

	def __init__(self):
		pass

	def getcases_ini(self,dir,file_ini):
		if os.path.exists('testcases/'+dir):
			if os.path.exists('testcases/'+dir+'/'+file_ini):
				return ('testcases/'+dir+'/'+file_ini)
			raise IOError("Can't find testcases files")
		raise IOError("Can't find contents")

	# def __loop_dir(self,dir):
	# 	for i in os.listdir(dir):
	# 		if os.path.isdir(dir+'/'+i):
	# 			self.__loop_dir(dir+'/'+i)
	# 		else:
	# 			if '.ini' in i:
	# 				filedir = dir+'/'+i
	# 				self.testcase_list.append(filedir)

	def getcases_list(self,dir):
		testcase_list = []
		dircs = 'testcases/'+dir
		if os.path.exists(dircs):
			def loop_dir(dircs):
				for i in os.listdir(dircs):
					if os.path.isdir(dircs+'/'+i):
						loop_dir(dircs+'/'+i)
					else:
						if '.ini' in i:
							filedir = dircs+'/'+i
							testcase_list.append(filedir)
				return testcase_list
		else:
			raise IOError("Can't find contents")

if __name__ == '__main__':
	print GetTestcases().getcases_list('demo')



