#-*-coding=UTF-8-*-
__author__ = 'fxf'

import os
import subprocess
import time

from config.ConfigSet import ConfigSet

class PlayTestcases(object):

	def __init__(self):
		self.config = ConfigSet('config/resource/keyevent.ini')

	def play(self,step):
		methods = step.split('-')
		if len(methods) != 2:
			print "syntax error with testcases "
		else:
			item = self.config.get('key',methods[0])
			subprocess.call('adb shell input keyevent '+item)
			time.sleep(int(methods[1]))

	def play_monkey(self):
		subprocess.call('adb shell ')

	def play_logcat(self,dir,file_ini):
		subprocess.call('adb shell logcat -c')
		time.sleep(1)
		if os.path.exists('result/log/'+dir):
			pass
		else:
			os.mkdir('result/log/'+dir)
		file_name = file_ini.split('.')
		times = time.strftime('%y-%m-%d-%H-%M-%S',time.localtime(time.time()))
		command = 'result/log/' + dir + '/' + file_name[0] + '-' + times + '.log'
		return subprocess.Popen('adb shell logcat -vtime > ' + command,shell=True)