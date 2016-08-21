#-*-coding:UTF-8-*-
__author__ = 'fxf'

import subprocess

class Ping_Ip(object):
'use threads to modify this script and make it work more powerfull'
	def __init__(self):
		pass

	def ping(self,ip_address):
		ip_head = ip_address.split('-')
		ip_nums = ip_head[0].split('.')
		if int(ip_head[1]) >= 255:
			print 'Error input'
		else:
			for i in range(int(ip_head[1])-int(ip_nums[3])+1):
				ipaddr = ip_nums[0]+'.'+ip_nums[1]+'.'+ip_nums[2]+'.'+str(int(ip_nums[3])+i)
				p = subprocess.Popen("ping "+ipaddr,shell = True,stdout = subprocess.PIPE)
				info = p.communicate()
				if '=32' in info[0]:
					print ipaddr + ' : was ok'
				else:
					print ipaddr + " : can't pinging"

if __name__ == '__main__':
	ip_address = raw_input("please input the ip and endwith nums:")
	ping = Ping_Ip()
	ping.ping(ip_address)