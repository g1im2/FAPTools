#-*-coding:UTF-8-*-
__author__ = 'fxf'
import subprocess,os,time

class ServerControl(object):
	
	def __init__(self):
		pass
	
	ipaddr = None
	
	#
	def adb_connect(self):
		if ServerControl.ipaddr is None:
			ServerControl.ipaddr = raw_input("Please enter the terminal IP address, and an end to press the Enter key:")
		subprocess.call("adb kill-server")
		time.sleep(5)
		subprocess.call("adb connect " + ServerControl.ipaddr)
		ServerControl().adb_connect_if()
	
	def adb_connect_again(self):
		subprocess.call("adb connect " + ServerControl.ipaddr)
		ServerControl().adb_connect_if()
	
	#
	def adb_connect_if(self):
		while 1:
			adb_info = subprocess.check_out("adb get-state")
			time.sleep(3)
			if "device" not in adb_info:
				ServerControl.ipaddr = raw_input("Cannot find the ADB equipment, please check the cable is inserted into the terminal, the terminal ADB option is open. \n please input terminal IP address, and an end to press the enter key:")
				subprocess.call("adb kill-server")
				time.sleep(5)
				subprocess.call("adb connect " + ipaddr)
			else:
				break
	
	def adb_usb_if(self):
		while 1:
			adb_info = subprocess.check_output("adb get-state")
			time.sleep(3)
			if "device" not in adb_info:
				print"ADB device not found, please wait for the 10s, ADB will Connect ready"
				for i in range(10):
					print "waitting times(seconds):"+ str(i+1)
					time.sleep(1)
			else:
				break

	def adb_kill(self):
		subprocess.call('adb kill-server')
	
	#judge udisk was on 
	def udisk_if(self):
		while 1:
			usb = subprocess.Popen("adb shell df", shell = True, stdout = subprocess.PIPE)
			usb_info = usb.communicate()
			if '/mnt/sda/sda1' not in usb_info[0]:
				raw_input("check your U-disk is on terminal,and press Enter to continue")
				continue
			else:
				break
		
	def apache_control(self,filename):
			os.system(filename)
			
if __name__ == '__main__':
	stl = ServerControl()
	stl.adb_connect()
