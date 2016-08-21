#-*-coding:UTF-8-*-
__author__ = 'fxf'
from testcases.plugins.Check_Cert import Check_Cert

class Interface_Plugins(object):
	
	def __init__(self):
		pass
	
	def check_cert(self):
		cert = Check_Cert()
		cert.init()
		cert.getAllAPKs(Check_Cert.apkpath)
		cert.getCert()
		cert.checkSpecGMSCert()
		cert.checkFrameworkCert()
		cert.PrintTestResult()
		print "\nthe Scripts was successed"
		print "come to  " + Check_Cert.rootpath+'\\'+ Check_Cert.certfile + "to take the APK's list,come to  " + Check_Cert.rootpath+'\\'+ Check_Cert.certDetail + "check with apk's informations"
	