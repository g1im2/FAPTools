#-*- coding:UTF-8 -*-
__author__ = 'fxf'
import sys
from cmd import Cmd

#The modules build by self
from interface.Interface import Interface
from interface.Interface_Plugins import Interface_Plugins
from interface.Interface_Tools import Interface_Tools
from interface.Interface_Help import Interface_Help



class Main(Cmd):	
	def __init__(self):
		Cmd.__init__(self)
		self.prompt = 'fxf-Android_Test:/> '
		self.intro = '''          Android-AutoTest Terminal
#---------------------------------------------#	
    j&=   y+ y*    jv+   yy-u    v &
   wE!"   jI7$T   7MPC   NV$E-   Ej&v-
   O*K^  yHH:Ovm+ UMMk   BMNTO: H1="7'
  jO&OH: "OH7"E~  U0H1   BB71` jCf'U:
  vM1H1   jB-j1  wHhHh*-/$B)B-   BkJUk
  ^HI'OH J""^N1  "OHOK~  H$H"Da jP'N ^
   "`  O|    "    jvHT   T ~ ""    "

                              -Write by fxf
                              -power by Python
#---------------------------------------------#
			'''
		
	def do_hello(self,arg):
		print "hello, world",arg		
	
	#def do_upgrade(self,arg):
	#	command = ('auto','autofull','autopath','manual','manualfull','manualpath')
	#	interface = Interface()
	#	method = arg.split()
	#	if len(method) != 2:
	#		print "error input"
	#	elif method[0] == 'usb' and method[1] in command:
	#		interface.upgrade_usb(method[1])
	#	elif method[0] == 'ota' and method[1] in command:
	#		interface.upgrade_ota(method[1])
	#	else:
	#		print"error input"
	
	def help_upgrade(self):
		interface = Interface_Help()
		interface.help_upgrade()
	
	def do_mercury(self,arg):
		interface = Interface_Tools()
		interface.mercury(arg)
	
	def help_mercury(self):
		interface = Interface_Help()
		interface.help_mercury()
	
	def do_check(self,arg):
		interface = Interface_Plugins()
		interfacetools = Interface_Tools()
		if arg == 'cert':
			interface.check_cert()
		elif arg == 'bugreport':
			interfacetools.chkbugreport()
		elif arg == 'permission':
			interfacetools.chkpermission()
		else:
			print("error input")
	
	def help_check(self):
		interface = Interface_Help()
		interface.help_check()
	
	def do_autorun(self,arg):
		interface = Interface()
		method = arg.split()
		if len(method) != 2:
			print 'error input'
		else:
			interface.play_testcases(method[0],method[1])

	def help_autorun(self):
		interface = Interface_Help()
		interface.help_autorun()

	def do_auto(self,arg):
		interface = Interface()
		if arg == 'installapks':
			interface.install_apk()

	def help_auto(self):
		interface = Interface_Help()
		interface.help_auto()
	
	def do_diag(self,arg):
		interface = Interface()
		interface.product_diag(arg)
	
	def help_diag(self):
		interface = Interface_Help()
		interface.help_diag()
	
	def do_exit(self,arg):
		print arg
		sys.exit()
if __name__ == '__main__':
	main = Main()
	main.cmdloop()
