#-*-coding:UTF-8-*-
__author__ = 'fxf'

import os

from config.ConfigSet import ConfigSet
from config.GetTestcases import GetTestcases
from analyzer.KeywordAnalyzer import KeywordAnalyzer
from modules.PlayTestcases import PlayTestcases
from modules.ServerControl import ServerControl

class Run_Operation(object):

	def __init__(self):
		pass

	def autoplay(self,dir,file_ini):
		testcases = GetTestcases()
		num = 0
		if file_ini == 'all':
			cases_list = testcases.getcases_list(dir)
			for i in cases_list:
				config = ConfigSet(i)
				step = config.get_file_list('testcases','step')
				loop = config.get('testcases','loop')
				file_name = os.path.split(i)
				p = PlayTestcases().play_logcat(dir,file_name[1])
				if loop != '0':
					for i in range(int(loop)):
						for play in step:
							PlayTestcases().play(play)

				elif loop == '0':
					print 'loop times was wrong'
				num += 1
				ServerControl().adb_kill()
			KeywordAnalyzer().analyzer_filelist(dir)
		else:
			cases = testcases.getcases_ini(dir,file_ini)
			config = ConfigSet(cases)
			step = config.get_file_list('testcases','step')
			loop = config.get('testcases','loop')
			p = PlayTestcases().play_logcat(dir,file_ini)
			if loop != '0' :
				for i in range(int(loop)):
					for play in step:
						PlayTestcases().play(play)
			elif loop == '0':
				print 'loop times was wrong'
			ServerControl().adb_kill()
			KeywordAnalyzer().analyzer_filelist(dir)