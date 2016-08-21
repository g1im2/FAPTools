#-*coding:UTF-8-*-
__author__ = 'fxf'

import subprocess
import sys
sys.path.append('..')
from serverctrl.ServerControl import ServerControl
from stbctrl.BoxControl import BoxControl
from config.ConfigSet import ConfigSet

config = ConfigSet('../config/resource/usb_config.ini')
usb_info = config.get('usb','usb_info')

if __name__ == '__main__':
	rebootnum = 0
	numbers = raw_input("Please enter the number of cycles to restart the need£º")
	numb = int(numbers)
	ServerControl().adb_connect()
	for i in range(numb):
		rebootnum = rebootnum + 1
		print "#################################################################"
		print "Restart frequency statistics:",rebootnum
		print "#################################################################"
		BoxControl().waittimes(5)
		ServerControl().adb_connect_again()
		print "#################################################################"
		print "Please wait for the 10s USB, are testing whether there"
		print "#################################################################"
		BoxControl().waittimes(10)
		p = subprocess.Popen("adb shell \"df|grep sda1\"",shell=True,stdout=subprocess.PIPE)
		pi = p.communicate()
		pii=str(pi[0])
		if pii == usb_info
			print "#################################################################"
			print "Detection of USB exist! Please wait for the 3S to restart"
			print "#################################################################"
 			BoxControl().waittimes(3)
			subprocess.Popen("adb reboot",shell=True)
		else:
			print "Found unable to mount the U disk, has stopped the script"
			print "If you run the script, you first, please confirm the terminal information in U disk and scripts in the U disk information is the same? If not, you will see the tips"
			print "If the confirmation U disk information has been checked, then to detect the terminal unable to mount the fault U disk."
			sys.exit()
		print "#################################################################"
		print "Please restart the process of waiting for 50s"
		print "#################################################################"
		BoxControl().waittimes(50)