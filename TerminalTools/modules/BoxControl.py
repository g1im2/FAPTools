#-*-coding:UTF-8-*-
import subprocess,time
from config.ConfigSet import ConfigSet

class BoxControl(object):
	
	config = ConfigSet('../config/resource/keyevent.ini')
	
	def __init__(self):
		pass
	
	#M321
	def upgrade(self):
		subprocess.call("adb shell \"am start -a android.settings.SYSTEM_UPDATE_SETTINGS\"",shell = True)
		time.sleep(10)
		subprocess.call("adb shell input keyevent KEYCODE_DPAD_DOWN")
		print "Press Soft_Key Down"
		time.sleep(2)
		subprocess.call("adb shell input keyevent KEYCODE_DPAD_DOWN")
		print "Press Soft_Key Down"
		time.sleep(2)
		subprocess.call("adb shell input keyevent KEYCODE_ENTER")
		print "Press Soft_Key Enter"
	
	#USB upgrade by M321 release
	def upgrade_usb(self,version_url):
		subprocess.call("adb shell \"rm -rf /mnt/sda/sda1/dload\"")
		subprocess.call("adb shell mkdir /mnt/sda/sda1/dload")
		time.sleep(2)
		subprocess.call("adb push "+version_url+" /mnt/sda/sda1/dload")
		BoxControl().waittimes(3)
		subprocess.call("adb reboot")
		BoxControl().waittimes(50)
		subprocess.call("adb shell input keyevent KEYCODE_DPAD_DOWN")
		subprocess.call("adb shell input keyevent KEYCODE_ENTER")
	
	
	#
	def initializ(self):
		subprocess.call("adb shell input keyevent KEYCODE_HOME")
		time.sleep(1)
		BoxControl.loop_keycode(7,"RIGHT")
		time.sleep(1)
		subprocess.call("adb shell input keyevent KEYCODE_DPAD_DOWN")
		time.sleep(1)
		BoxControl.loop_keycode(6,"RIGHT")
		subprocess.call("adb shell input keyevent KEYCODE_ENTER")
		time.sleep(1)
		BoxControl.loop_keycode(3,"DOWN")
		subprocess.call("adb shell input keyevent KEYCODE_DPAD_RIGHT")
		time.sleep(1)
		subprocess.call("adb shell input keyevent KEYCODE_ENTER")
		time.sleep(1)
		subprocess.call("adb shell input keyevent KEYCODE_DPAD_RIGHT")
		time.sleep(1)
		subprocess.call("adb shell input keyevent KEYCODE_ENTER")
	
	#install app
	def install(self, filename):
		subprocess.call("adb install "+filename)
	
	#push source to the terminal
	def push(self, sourcename, targetdir):
		subprocess.call("adb push " + sourcename + " " + targetdir)
	
	# start an android's action
	def start_action(self, actionname):
		subprocess.call("adb shell am start -a " + actionname)
	
	#start uiautomators' jar action 
	def start_uiautomator(self, jarname, classname):
		subprocess.call("adb shell uiautomator runtest " + jarname + " -c "+ classname)
	
	def loop_keycode(n,event):
		m=int(n)
		for i in range(m):
			time.sleep(1)
			subprocess.call("adb shell input keyevent KEYCODE_DPAD_"+event)
	
		#input keyevent to control android
	def press_key(self,keyput):
		print ("press " + keyput)
		subprocess.call("adb shell input keyevent " + BoxControl().config.get('key',keyput))
	
	def waittimes(self,times):
		nums = 1
		for i in range(times):
			print "times:"+ str(i+1)
			time.sleep(1)

if __name__ == '__main__':
	while 1:
		key = raw_input("qqq:")
		BoxControl().press_key(key)	