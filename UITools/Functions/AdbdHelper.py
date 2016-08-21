#-*-coding:utf-8-*-
__author__ = 'fxf'

import subprocess

class AdbdHelper(object):

    def __init__(self):
        pass

    #count and return adb devices Numbers' number
    def adb_devices_numbers(self):
        devices = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE)
        devices_info = devices.communicate()
        return devices_info[0].count("device")-1

    #get adb devices devicesName and serialNo
    def adb_devices_list(self):
        devices_list = []
        devices =subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE)
        devices_info = devices.communicate()
        devices_process = devices_info[0].split("\r\n")
        for i in range(1, len(devices_process)-2):
            devices_list.append(devices_process[i].split("\t"))
        return devices_list
