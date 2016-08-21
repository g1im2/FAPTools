#-*-coding:UTF-8-*-
__author__ = 'fxf'

from serial import Serial
from config.ConfigSet import ConfigSet

class SerialControl(object):
	
	config = ConfigSet('../config/resource/serial.ini')
	serial_port = config.get('serial','serial_port')
	baud_rate = config.get('serial','baud_rate')
	byte_size = config.get('serial','byte_size')
	parity = config.get('serial','parity')
	stop_bits = config.get('serial','stop_bits')
	timeout = config.get('serial','timeout')
	xonxoff = config.get('serial','xonxoff')
	rtscts = config.get('serial','rtscts')
	
	def __init__(self):
		pass
		
	def open_serial_port(self):
		ser = Serial(SerialControl.serial_port)
		print ser.name
		ser.write("getprop")
		print ser.readline(100)
		ser.close
		
if __name__ == '__main__':
	serial = SerialControl()
	serial.open_serial_port()
	
