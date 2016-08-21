#-*-coding=UTF-8-*-
__author__ = 'otherplugins'
import os,sys,shutil,time,re
from xml.dom import minidom
import subprocess
from config.ConfigSet import ConfigSet


class Check_Cert(object):
	
	config = ConfigSet('config/resource/plugins.ini')
	rootpath = config.get('check_cert','rootpath')
	apkpath = config.get('check_cert','apkpath')
	certpath = config.get('check_cert','certpath')
	#rootpath = "d:\\apkTest"
	#apkpath = rootpath+"\\apks"
	#certpath = rootpath+"\\certs"
	certfile = "cert.txt"
	certDetail = "certDetails.txt"

	errorinfo = ""

	DebugAPK = ""
	AndroidAPK = ""
	GMSAPK = ""
	HuaweiAPK = ""
	EmptyAPK = ""
	OtherAPK = ""

	DebugCertKey = "CN=Android Debug, O=Android, C=US"
	AndroidCertKey = "EMAILADDRESS=android@android.com, CN=Android, OU=Android"
	GMSCertKey = "O=Google Inc., L=Mountain View, ST=California"
	GMSCertKey2 = "O=\"Google, Inc\", L=Mountain View, ST=CA"
	HuaweiCertKey = "EMAILADDRESS=mobile@huawei.com, CN=AndroidTeam, OU=TerminalCompany, O=Huawei"

	def __init__(self):
		pass
		
	def getAllAPKs(self,pcPath): 
		print "searching apks ..."
		apklist = subprocess.check_output("adb shell busybox find -name \"*.apk\"")
		apklist = apklist.splitlines()
		for apk in apklist:
			if not ".apk" in apk: 
				continue
			apkname = apk.split('/')[-1]
			print "exporting " + apkname + "..."
			subprocess.call("adb pull " + apk + " " + pcPath+"\\"+apkname)
		print "Done."
		
	def getCert(self):
		fCertInfo = open(Check_Cert.rootpath+'\\'+ Check_Cert.certDetail, 'w')
		apklist = os.listdir(Check_Cert.apkpath)
		for apk in apklist:
			print "processing "+apk+"\'sign",
			name = Check_Cert.apkpath + "\\" + apk
			s = subprocess.check_output("jar tf " + name)
			saFile = ""
			lines = s.splitlines()
			for line in lines:
				if (".RSA" in line) or (".DSA" in line):
					saFile = line
					break
			if saFile == "":
				print "no sign"
				Check_Cert.EmptyAPK += apk + "\n"
				continue
			subprocess.call("jar -xf " + name + " " + saFile)
			newCertName = Check_Cert.certpath+"\\" + apk + "_CERT" + saFile[-4:]
			shutil.move(saFile, newCertName)
			certinfo = subprocess.check_output("keytool -printcert -file " + newCertName)
			Check_Cert().classifyAPK(certinfo, apk, fCertInfo)
			print "Done"        
		fCertInfo.close()
    
	def classifyAPK(self,certinfo, apkname, log):
		s = certinfo.split('\n')
		log.write("\nApk'name:" + apkname)
		log.write("\nApk'sign:")
		log.write("\n" + s[0] + "\n" + s[3] + "\n" + s[4] + "\n" + s[5] + "\n" + s[6] + "\n" + s[7])
		log.write("\n---------------------------------------------------------------------\n")
		log.flush()
	
		if Check_Cert.DebugCertKey in s[0] :
			Check_Cert.DebugAPK += apkname + "\n"
		elif Check_Cert.HuaweiCertKey in s[0] :
			Check_Cert.HuaweiAPK += apkname + "\n"
		elif (Check_Cert.GMSCertKey in s[0]) or (Check_Cert.GMSCertKey2 in s[0]):
			Check_Cert.GMSAPK += apkname + "\n"
		elif Check_Cert.AndroidCertKey in s[0] :
			Check_Cert.AndroidAPK += apkname + "\n"
		else:
			Check_Cert.OtherAPK += apkname + "\nsign information:" + s[0][7:] + "\n\n"
	
	def checkFrameworkCert(self):
		if "framework-res.apk" in Check_Cert.HuaweiAPK:
			pass
		else :
			Check_Cert.errorinfo += "framework-res.apk'didn't sign by Huawei! \n"
	
	def checkSpecGMSCert(self):
		ver = subprocess.check_output("adb shell getprop ro.build.version.release")
		ver = ver[:3]
		print "now Android_version: " + ver
		if ver == "2.1":
			if ("Googlecheckin.apk" in Check_Cert.GMSAPK) or ("Googlecheckin.apk" in Check_Cert.AndroidAPK) :
				Check_Cert.errorinfo += "2.1_version Googlecheckin.apk sign by Huawei!\n"
			if ("GoogleSubscribedFeedsProvider.apk" in Check_Cert.GMSAPK) or ("GoogleSubscribedFeedsProvider.apk" in Check_Cert.AndroidAPK) :
				Check_Cert.errorinfo += "2.1_version GoogleSubscribedFeedsProvider.apk sign by Huawei!\n"
			if ("NetworkLocation.apk" in Check_Cert.GMSAPK) or ("NetworkLocation.apk" in Check_Cert.AndroidAPK) :
				Check_Cert.errorinfo += "2.1_version NetworkLocation.apk sign by Huawei!\n"
		elif ver == "2.2":
			if ("NetworkLocation.apk" in Check_Cert.GMSAPK) or ("NetworkLocation.apk" in Check_Cert.AndroidAPK) :
				Check_Cert.errorinfo += "2.2_version NetworkLocation.apk sign by Huawei!\n"
			if ("GoogleBackupTransport.apk" in Check_Cert.GMSAPK) or ("GoogleBackupTransport.apk" in Check_Cert.AndroidAPK) :
				Check_Cert.errorinfo += "2.2_version GoogleBackupTransport.apk sign by Huawei!\n"
		else:
			if ("GoogleBackupTransport.apk" in Check_Cert.GMSAPK) or ("GoogleBackupTransport.apk" in Check_Cert.AndroidAPK)  or ("GoogleBackupTransport.apk" in Check_Cert.AndroidAPK) :
				Check_Cert.errorinfo += "GoogleBackupTransport.apk sign by Huawei!\n"

    
	def PrintTestResult(self):
		f = open(Check_Cert.rootpath+'\\' + Check_Cert.certfile, 'w')
		f.write("\n=============================================================================================")
		f.write("\ntest by error information:\n"+Check_Cert.errorinfo)
		if Check_Cert.EmptyAPK != "":
			f.write("\n-------------------------------------------------------------------------")
			f.write("\n\nThe nosign APK is exits:\n" + Check_Cert.EmptyAPK)
		if Check_Cert.DebugAPK != "" :
			f.write("\n-------------------------------------------------------------------------")
			f.write("\n\nuse Android Debug always unallow debug sign with APK!)\nsign information" + Check_Cert.DebugCertKey + "\n" + Check_Cert.DebugAPK)
			
		f.write("\nerror information was over\n")
		f.write("=============================================================================================\n\n")
		f.write("\ntest by right information:\n")
		if Check_Cert.HuaweiAPK != "" :
			f.write("\n\n-------------------------------------------------------------------------")
			f.write("\n\nuseHuawei's sign APK Product by Huawei always use with Huawei's sign\nsign information" + Check_Cert.HuaweiCertKey + "\n" + Check_Cert.HuaweiAPK)
		if Check_Cert.GMSAPK != "" :
			f.write("\n\n-------------------------------------------------------------------------")
			f.write("\n\nuse Google'sign(Product by GMS always use with Google )\nsign information" + Check_Cert.GMSCertKey + "\n" + Check_Cert.GMSAPK)
		if Check_Cert.AndroidAPK != "" :
			f.write("\n\n-------------------------------------------------------------------------")
			f.write("\n\nuse Android signs APK( usefull Android app)\nsign information:" + Check_Cert.AndroidCertKey + "\n" + Check_Cert.AndroidAPK)
		if Check_Cert.OtherAPK != "":
			f.write("\n\n-------------------------------------------------------------------------")
			f.write("\n\nuse other sign,signed by others\n" + Check_Cert.OtherAPK)
		f.close()

	def init(self):
		print "init ..."
		# check connection
		try:
			s = subprocess.check_output("adb get-state")
			if not "device" in s:
				sys.exit("adb connect error") 
		except:
			sys.exit("adb connect error") 
		# make working dir
		try:
			shutil.rmtree(Check_Cert.rootpath, True)
			time.sleep(5) 
			os.mkdir(Check_Cert.rootpath)
			os.mkdir(Check_Cert.apkpath)
			os.mkdir(Check_Cert.certpath)
		except Exception,e: 
			print e

if __name__ == '__main__':
	cert = Check_Cert()
	cert.init()
	cert.getAllAPKs(Check_Cert.apkpath)
	cert.getCert()
	cert.checkSpecGMSCert()
	cert.checkFrameworkCert()
	cert.PrintTestResult()
	print "\nthe Scripts was successed"
	print "come to " + Check_Cert.rootpath+'\\'+ Check_Cert.certfile + " to take the APK's list, come to " + Check_Cert.rootpath+'\\'+ Check_Cert.certDetail + " check with apk's informations"



