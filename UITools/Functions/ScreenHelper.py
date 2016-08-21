#-*-coding:utf-8-*-
__author__ = 'fxf'

import subprocess

class ScreenHelper(object):

    def __init__(self):
        pass

    def Cap(self, filename):
        sdcardUrl = "/sdcard/FdroidScreencap.png"
        subprocess.call(str("adb shell screencap -p "+sdcardUrl), shell=True)
        subprocess.call(str("adb pull " + sdcardUrl + " " + filename), shell=True)

    def Record(self, filename):
        sdcardUrl = "/sdcard/FdroidScreenrecord.mp4"
        subprocess.call(str("adb shell screenrecord "+sdcardUrl), shell=True)
        subprocess.call(str("adb pull " + sdcardUrl + " " + filename), shell=True)