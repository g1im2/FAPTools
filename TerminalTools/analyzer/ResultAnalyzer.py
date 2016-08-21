#-*-coding:UTF-8-*-
__author__ = 'fxf'

import subprocess,time
import os


class ResultAnalyzer(object):
	def __init__(self):
		pass
	
	def resultout(self,local_result_url,fingerInfo):
		resulttxt=local_result_url+"\\"+"result.txt"
		version_finger=subprocess.Popen("adb shell getprop ro.build.version.hwincremental",shell=True,stdout=subprocess.PIPE)
		version_finger_info=version_finger.communicate()
		if fingerInfo.strip("\\r\\r\\n") == version_finger_info[0].strip("\r\r\n"):
			resultinfo = open(resulttxt,'a+')
			times = time.asctime(time.localtime(time.time()))
			resultinfo.write("Ready_Version:"+version_finger_info[0]+ "Target_Version:"+fingerInfo+ "\nat:"+times+" Updated Successed\n")
			resultinfo.write("#################################################################\n")
			resultinfo.close()
		else:
			resultinfo = open(resulttxt,'a+')
			times = time.asctime(time.localtime(time.time()))
			resultinfo.write("Ready_Version:"+version_finger_info[0]+ "Target_Version:"+fingerInfo+ "\nat:"+times+" Updated failed !!! Please Check The Right Versions\n")
			resultinfo.write("#################################################################\n")
			resultinfo.close()
	
	#find the finger information and check the keywords
	def check_log(self,log_url,lognums_url,keywords):
		f = open(log_url,'r')
		result = list()
		for line in f.readlines():
			line.strip()
			if keywords  not in line:
				continue
			result.append(line)
		f.close()
		if result:
			packinfo = open(info_url,'a+')
			packinfo.write(lognums_url+"error was happened , Please check it������\n")
			packinfo.write("#################################################################\n")
			packinfo.close()
		else:
			packinfor = open(info_url,'a+')
			packinfor.write(lognums_url+"no error was happened\n")
			packinfor.write("#################################################################\n")
			packinfor.close()
	
	def keyword_exits(self,command,key_info):
		text = subprocess.Popen(command, shell=True, stdout = subprocess.PIPE)
		text_info = text.communicate()
		if key_info in text_info[0]:
			print 'OK'
		else:
			print 'failed'

	def check_permission(self,manifest_url,manifest_source,apkname):
		if os.path.isfile(manifest_url):
			manifest_info = open(manifest_url,'r')
			result_info = open(manifest_source+'/android_manifest_result.txt','a+')
			result_info.write('################################################################################\n')
			result_info.write('AndroidManifest.xml with '+ apkname +'\n')
			for line in manifest_info.readlines():
				if "uses-permission" not in line:
					continue
				result_info.write(line)
			manifest_info.close()
			result_info.close()
		else:
			noresult = open(manifest_source + '/android_manifest_result.txt','a+')
			noresult.write('################################################################################\n')
			noresult.write('no AndroidManifest.xml in '+ apkname +'\n')
			noresult.close()

	

if __name__ == '__main__':
	ResultAnalyzer().resultout()