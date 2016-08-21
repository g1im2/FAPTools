# -*- coding: UTF-8 -*-

import subprocess
import sys
from stbctrl.BoxControl import BoxControl
from filectrl.FileControl import FileControl
from serverctrl.ServerControl import  ServerControl
reload(sys)
   

if __name__ == '__main__':
	rebootnum = 0
	ServerControl().adb_connect()
  for i in range(numb):
  	ServerControl().adb_connect_again()
    time.sleep(3)
		print "##########################################################################"
		print "Getting the log, automatically saved in ~\\testResult\n terminal initialization will operate automatically after 60s, please wait"
		print "##########################################################################"
		rebootnum = rebootnum + 1
		lg = "D:\\autoini"+str(rebootnum)
		log = lg+".log"
		subprocess.Popen("adb shell logcat -vtime > "+log,shell=True)
		BoxControl().waittimes(60)
		BoxControl().initializ()
		print "#################################################################"
		print "Initializing terminal, please wait for 270s"
		print "#################################################################"
		BoxControl().waittimes(270)
		print "#################################################################"
		print "Is the log analysis, please slightly wait"
		print "#################################################################"
		FileControl().check_log(log)
		print "#################################################################"
		print "Initialize the statistics:",rebootnum
		print "#################################################################"
		time.sleep(5)

    
    
