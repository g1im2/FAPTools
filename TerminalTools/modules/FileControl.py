#-*-coding:UTF-8-*-
__author__ = 'fxf'

import os
import shutil
import subprocess
from hashlib import md5

class FileControl:
	def __init__(self):
		self.files_list = []
				
	#check the files and sum MD5
	def calMd5forfile(self,version_file_url):
		a_file = open(version_file_url,'rb')
		md5sum=md5(a_file.read()).hexdigest()
		a_file.close()
		return md5sum.upper()

	#copy update files to update dir and rename
	def inputupgradefile(self,version_file_url,target_url):
		copy_command="copy "+version_file_url+" "+ target_url
		os.system(copy_command)
		
	#modify filelist.xml in update dir
	def filelist_xml(self,xml_filelist_url,md5_sum):
		f=open(xml_filelist_url,'r+')
		amodify_line=f.readlines()
		amodify_line[11]="<md5>"+md5_sum+"</md5>\n"
		f.close()
		ff=open(xml_filelist_url,'w+')
		ff.writelines(amodify_line)
		ff.close()
		
	#modify changelog.xml in update dir
	def changelog_xml(self,xml_changelog_url,filename):
		fi=open(xml_changelog_url,'r+')
		modify_line=fi.readlines()
		modify_line[4]='<component name="TCPU" version='+"\""+filename+"\""+"/>\n"
		fi.close()
		df=open(xml_changelog_url,'w+')
		df.writelines(modify_line)
		df.close()

	def __loop_dir(self,dir):
		for i in os.listdir(dir):
			if os.path.isdir(dir+'/'+i):
				self.__loop_dir(dir+'/'+i)
			else:
				if '.log' in i:
					filedir = dir+'/'+i
					self.files_list.append(filedir)

	def getfiles_list(self,dir):
		if os.path.exists(dir):
			self.__loop_dir(dir)
			return self.files_list
		else:
			raise IOError("Can't find contents")

	def get_apks(self):
		manifest_source = 'result/AndroidManifest'
		apk_url = 'result/AndroidManifest/apks'
		manifest = 'result/AndroidManifest/manifest'
		if os.path.exists(manifest_source):
			shutil.rmtree(manifest_source)
			os.mkdir(manifest_source)
			os.mkdir(apk_url)
			os.mkdir(manifest)
		subprocess.call("adb pull /system/app "+apk_url)
		subprocess.call("adb pull /system/priv-app "+apk_url)


if __name__ == '__main__':
	control = FileControl()
	control.check_dir('D:')