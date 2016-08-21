#-*-coding:UTF-8-*-
__author__ = 'fxf'

import subprocess,time,os
from config.ConfigSet import ConfigSet
from modules.BoxControl import BoxControl
from modules.ServerControl import ServerControl

class Product_Diag(object):
	
	config = ConfigSet('config/resource/scripts.ini')
	upgrade_version = config.get('M_product_test','upgrade_version')
	result_url = config.get('M_product_test','result_url')
	product_apk = config.get('M_product_test','product_apk')
	video_4k = config.get('M_product_test','video_4k')
	video = config.get('M_product_test','video')
	
	def __init__(self):
		self.product_dict=['"display version"',\
		'"pingtest"',\
		'"usb test"',\
		'"sd test"',\
		'"set barcode" "123456789"',\
		'"display barcode"',\
		'"led on"',\
		'"led off"',\
		'"set sn" "12345678"',\
		'"display sn" "21530134938W4A000021"',\
		'"set macaddr" "38F8895D87B6"',\
		'"display macaddr"',\
		'"set hdcp" "123456789123456789123456789"',\
		'"set ssid" "abcd"',\
		'"display ssid"',\
		'"set wpakey" "abcdef"',\
		'"display wpakey"',\
		'"set customersn1" "123456789"',\
		'"display customersn1"',\
		'"display mmi"',\
		'"display hdcp"',\
		'"display productversion"',\
		'"set hdcprootkey" "1234567812345678"',\
		'"display hdcprootkey"']
	
	def diagtest(self):
		ServerControl().adb_usb_if()
		if os.path.exists(Product_Diag.result_url):
			os.system("del " + Product_Diag.result_url)
		for i in self.product_dict:
			print ("test with "+ i)
			tests = subprocess.Popen("adb shell diag " + i,shell=True,stdout = subprocess.PIPE)
			test_info = tests.communicate()
			time.sleep(1)
			if 'success' in test_info[0]:
				print "OK"
				packinfo = open(Product_Diag.result_url,'a+')
				packinfo.write(i+" is OK\n")
				packinfo.write("#----------------------------------------------------------------#\n")
				packinfo.close()
			else:
				print "error was happend"
				packinfor = open(Product_Diag.result_url,'a+')
				packinfor.write(i+" error was happened,Please check it！！！\n")
				packinfor.write("#----------------------------------------------------------------#\n")
				packinfor.close()
	
	def upgrade_reboot(self):
		BoxControl().upgrade_usb(Product_Diag.upgrade_version)
		print "waiting for upgrade"
		BoxControl().waittimes(160)
		ServerControl().adb_usb_if()
		BoxControl().waittimes(90)
		subprocess.call("adb shell diag \"restore default\"")
		time.sleep(3)
		subprocess.call("adb reboot")
	
	def copy_apk(self):
		ServerControl().adb_usb_if()
		ServerControl().udisk_if()
		product_dir = subprocess.Popen("adb shell ls /mnt/sda/sda1",shell = True, stdout = subprocess.PIPE)
		product_info = product_dir.communicate()
		if "product\r\r\n" in product_info[0]:
			print("product dir was exists,and SWProductTest.apk will be copy")
			BoxControl().push(Product_Diag.product_apk,'/mnt/sda/sda1/product')
			#BoxControl().push(Product_Diag.video_4k,'/mnt/sda/sda1/product')
			#BoxControl().push(Product_Diag.video,'/mnt/sda/sda1/product')
			subprocess.call("adb shell \"setprop persist.net.write.efuse 1\"")
			raw_input("re plug U-disk with terminal,and press Enter to continue to test mmi")
		else:
			print("product dir was no found")
			subprocess.call("adb shell mkdir /mnt/sda/sda1/product")
			print("product dir was on and SWProductTest.apk will be copy")
			BoxControl().push(Product_Diag.product_apk,'/mnt/sda/sda1/product')
			subprocess.call("adb shell \"setprop persist.net.write.efuse 1\"")
			raw_input("re plug U-disk with terminal,and press Enter to continue to test mmi")
				
			
		
		
if __name__ == '__main__':
	product = Product_Diag()
	product.diagtest()
	product.upgrade_reboot()
	
