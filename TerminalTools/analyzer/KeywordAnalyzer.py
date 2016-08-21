#-*-coding:UTF-8-*-
__author__ = 'fxf'
import os
import shutil
import time

from config.ConfigSet import ConfigSet

class KeywordAnalyzer(object):

	def __init__(self):
		pass

	def __loop_dir(self,dir):
		for i in os.listdir(dir):
			if os.path.isdir(dir+'/'+i):
				self.__loop_dir(dir+'/'+i)
			else:
				if '.log' in i:
					filedir = dir+'/'+i
					self.files_list.append(filedir)

	def __getfiles_list(self,dir):
		if os.path.exists(dir):
			self.__loop_dir(dir)
			return self.files_list
		else:
			raise IOError("Can't find contents")

	def analyzer(self,filename):
		result = []
		config = ConfigSet('config/result-analyzer/check-keyword.ini')
		keyword = config.get_keyword_list('analyzer','keyword')
		f = open(filename,'r')
		for line in f.readlines():
			for i in keyword:
				if i in line:
					result.append(line)
				continue
		f.close()
		return result

	def analyzer_filelist(self,dir):
		times = time.strftime('%y-%m-%d-%H-%M-%S',time.localtime(time.time()))
		dirct = 'result/log/' + dir
		analyzer_log = 'result/analyzer/log/' + dir + times
		analyzer_result = 'result/analyzer/result/' + dir + times
		if os.path.exists('result/analyzer/log'):
			pass
		else:
			os.mkdir('result/analyzer/log')
		if os.path.exists('result/analyzer/result'):
			pass
		else:
			os.mkdir('result/analyzer/result')
		os.mkdir(analyzer_log)
		os.mkdir(analyzer_result)
		for files in self.__getfiles_list(dirct):
			result_list = self.analyzer(files)
			print result_list
			if result_list:
				for i in result_list:
					packinfo = open(analyzer_result + '/result.txt','a+')
					packinfo.write(files + " with Bug was happened :\n" + i + '\n')
					packinfo.write("#################################################################\n")
					packinfo.close()
		shutil.move(dirct,analyzer_log)

if __name__ == '__main__':
	key = KeywordAnalyzer()
	key.analyzer_filelist('demo')