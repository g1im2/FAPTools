#-*-coding:UTF-8-*-
__author__ = 'fxf'
import subprocess,time,os,shutil
import sys
sys.path.append("..")
from config.ConfigSet import ConfigSet
from modules.ServerControl import ServerControl
from modules.FileControl import FileControl
from analyzer.ResultAnalyzer import ResultAnalyzer

class  Run_Tools(object):
	
	# config = ConfigSet("config/resource/serverstart.ini")
	# mercury_bin = config.get('mercury','bin')
	# chkbugreport_file = config.get('chkbugreport','file')
	manifest_source = "result/AndroidManifest"
	apk_url = "result/AndroidManifest/apks"
	manifest = "result/AndroidManifest/manifest"

	
	def __init__(self):
		pass
		
	def start_mercury(self):
		ServerControl().adb_usb_if()
		subprocess.call("adb install testcases/apks/agent.apk")
		subprocess.call("adb forward tcp:31415 tcp:31415")
		subprocess.call("adb shell am start -n com.mwr.droidhg.agent/com.mwr.droidhg.agent.MainActivity")
		subprocess.call("adb push testcases/jars/mercurystart.jar /data/local/tmp")
		subprocess.call("adb shell uiautomator runtest mercurystart.jar -c com.fxf.autorun")
		subprocess.Popen("start " + Run_Tools.mercury_bin + " console connect",shell=True)
	
	def check_bugreport(self):
		ServerControl().adb_usb_if()
		os.system("adb shell bugreport > " + Run_Tools.chkbugreport_file)
		print ("waitting for 3 seconds and the report will be build")
		time.sleep(3)
		subprocess.call("java -jar tools/chkbugreport-0.5-203.jar " + Run_Tools.chkbugreport_file)

	def get_apk_androidmanifest(self):
		#FileControl().get_apks()
		apk_list = os.listdir(Run_Tools.apk_url)
		for i in apk_list:
			if '.apk' in i:
				ii = i.rstrip('.apk')
				subprocess.call("java -jar tools/apktool.jar d "+Run_Tools.apk_url+"/"+i+" "+Run_Tools.manifest+"/"+ii)
				manifest_url = Run_Tools.manifest+"/"+ii+"/AndroidManifest.xml"
				ResultAnalyzer().check_permission(manifest_url,Run_Tools.manifest_source,i)

	def test(self):
		f = open('../result/AndroidManifest/manifest/AirSharing/AndroidManifest.xml','r')
		for line in f.readlines():
			if line.find('allowBackup') > -1:
				print line[line.find('allowBackup="')+13:line.rfind('" android')]
			elif line.find('uses-permission') > -1:
				print line[line.find('permission.')+11:line.rfind('"')]





if __name__ == '__main__':
	start = Run_Tools()
	start.test()