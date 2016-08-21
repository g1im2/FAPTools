#-*-coding:UTF-8-*-
__author__ = 'fxf'

class Interface_Help(object):
	
	def __init__(self):
		pass
		
	def help_upgrade(self):
		print "upgrade [options][options]\n\
	[usb][option]	upgrade by usb disk\n\
		[auto]	auto upgrade with full-versions and path-versions\n\
		[autofull]	auto upgrade with full-versions\n\
		[autopath]	auto upgrade with path-versions\n\
	[ota][option] upgrade by ota\n\
		[auto]	auto upgrade with full-versions and path-versions\n\
		[autofull]	auto upgrade with full-versions\n\
		[autopath]	auto upgrade with path-versions\n\
		[manual]	manual upgrade with full-versions and path-versions\n\
		[manualfull]	manual upgrade with full-versions\n\
		[manualpath]	manual upgrade with path-versions"
	
	def help_check(self):
		print "check [option]\n\
	[cert]	check cert with apks where in /system/app and it will be build report\n\
	[bugreport]	check the information with Android Terminal and build report\n\
	[permission] check the permission with Android-apks"
	
	def help_mercury(self):
		print "a usefull tools for android-test with security, and no more informations here"
	
	def help_auto(self):
		print "auto [options]\n\
  [installapks]	install apks auto by adb"

	def help_autorun(self):
		print "autorun [options]\n\
	[dir][file_ini] autorun scripts by one scripts\n\
	[dir][all] autorun scripts by all"

	def help_diag(self):
		print "diag [option]\n\
	 [test] Product diag autotest\n\
	 [copy] Copy SWProductTest.apk to U-disk and skip cache fool"
