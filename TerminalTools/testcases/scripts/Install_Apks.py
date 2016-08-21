#-*-coding:UTF-*-
import subprocess,time
import os
from modules.ServerControl import ServerControl
from config.ConfigSet import ConfigSet

class Install_Apks(object):
	
	config = ConfigSet('config/resource/scripts.ini')
	targeturl = config.get('installapk','targeturl')
	
	def __init__(self):
		pass

	def install(self):
		lists = os.listdir(Install_Apks.targeturl)
		nums = 1
		for line in lists:
			if '.apk' in line:
				subprocess.call("adb install "+Install_Apks.targeturl+line,shell=True)
				time.sleep(1)
				print"##------------------------------##"
				print" |%dst apps was installed, wait |"%nums
				print"##------------------------------##"
				nums += 1
			else:
				continue

if __name__ == '__main__':
	print"put apks in D:\\apks and run this scripts\nAnd you must connect adb with product first"
	install = Install_Apks()
	install.install()