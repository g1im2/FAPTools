# -*- coding: utf-8 -*-
# author: smileymou5
# data:2016-05-01

import time
import subprocess
import os
import sys

from PyQt4 import QtCore, QtGui

from ShaJJToolsUI import Ui_Form

reload(sys)
sys.setdefaultencoding('utf-8')


class ShaJJTools(QtGui.QWidget, Ui_Form):
    """a tools which can flash image and some control with android devices"""

    recovery_image = ''
    boot_image = ''
    sideload_zip = ''

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.recovery_thread = FlashRecoveryImage()
        self.boot_thread = FlashBootImage()
        self.sideload_thread = FlashSideloadZip()
        self.oem_unlock_thread = OemUnlockThread()
        self.connect(self.rec_bt, QtCore.SIGNAL('clicked()'), self.choice_recovery_img)
        self.connect(self.boot_button, QtCore.SIGNAL('clicked()'), self.choice_boot_img)
        self.connect(self.sideload_bt, QtCore.SIGNAL('clicked()'), self.choice_zip)
        self.connect(self.enter_rec_bt, QtCore.SIGNAL('clicked()'), self.reboot_recovery)
        self.connect(self.fastboot_bt, QtCore.SIGNAL('clicked()'), self.reboot_fastboot)
        self.connect(self.reboot_bt, QtCore.SIGNAL('clicked()'), self.reboot)
        self.connect(self.oem_bt, QtCore.SIGNAL('clicked()'), self.oem_unlock)
        self.connect(self.start_bt, QtCore.SIGNAL('clicked()'), self.flash_device)

    def flash_device(self):
        recovery_text = self.recovery_line.text()
        boot_text = self.boot_line.text()
        sideload_text = self.sideload_line.text()
        if recovery_text == '':
            if boot_text == '' and sideload_text != '':
                self.sideload_flash()
            elif boot_text != '' and sideload_text == '':
                self.flash_boot()
            else:
                self.warning_msg(u'请选择文件再刷机')
        else:
            if boot_text == '' and sideload_text == '':
                self.flash_recovery()
            elif boot_text != '' or sideload_text != '':
                self.warning_msg(u'不能同时刷机')

    def choice_recovery_img(self):
        """choice recovery image"""
        dlg = QtGui.QFileDialog
        filename = dlg.getOpenFileName(self, u'选择recovery的img文件', './', 'IMG FILE(*.img)')
        self.boot_line.clear()
        self.sideload_line.clear()
        self.recovery_line.setText(filename)

    def choice_boot_img(self):
        """choice boot image"""
        dlg = QtGui.QFileDialog
        filename = dlg.getOpenFileName(self, u'选择boot的img文件', './', 'IMG FILE(*.img)')
        self.recovery_line.clear()
        self.sideload_line.clear()
        self.boot_line.setText(filename)

    def choice_zip(self):
        """choice sideload update with zip package"""
        dlg = QtGui.QFileDialog
        filename = dlg.getOpenFileName(self, u'刷机包的zip文件', './', 'IMG FILE(*.zip)')
        self.recovery_line.clear()
        self.boot_line.clear()
        self.sideload_line.setText(filename)

    def flash_recovery(self):
        """flash recovery image control"""
        recovery_image_file = self.recovery_line.text()
        recovery_image_file = unicode(recovery_image_file, 'utf-8')
        if '.img' in recovery_image_file:
            if os.path.isfile(recovery_image_file):
                ShaJJTools.recovery_image = recovery_image_file
                self.reboot_fastboot()
                self.recovery_thread.start()
            else:
                self.warning_msg(u'文件不存在，请重新选择')
        else:
            self.warning_msg(u'文件没有包含.img')

    def flash_boot(self):
        """flash boot image control"""
        boot_image_file = self.boot_line.text()
        boot_image_file = unicode(boot_image_file, 'utf-8')
        if '.img' in boot_image_file:
            if os.path.isfile(boot_image_file):
                ShaJJTools.boot_image = boot_image_file
                self.reboot_fastboot()
                self.boot_thread.start()
            else:
                self.warning_msg(u'文件不存在，请重新选择')
        else:
            self.warning_msg(u'文件没有包含.img')

    def sideload_flash(self):
        """flash sizeload image control"""
        sideload_file = self.sideload_line.text()
        sideload_file = unicode(sideload_file, 'utf-8')
        if '.zip' in sideload_file:
            if os.path.isfile(sideload_file):
                ShaJJTools.sideload_zip = sideload_file
                self.warning_msg(u'请手动切换到到recovery下的sideload模式\n再点击OK')
                print 'waitfor result....ok'
                self.sideload_thread.start()
            else:
                self.warning_msg(u'文件不存在，请重新选择')
        else:
            self.warning_msg(u'文件没有包含.zip')

    def reboot_control(self, commands):
        """reboot control"""
        if self.check_adb_devices():
            subprocess.Popen(str(commands), shell=True)
        else:
            self.warning_msg(u'只能操作一台Android设备')

    def reboot(self):
        """android device reboot and connect with button reboot"""
        self.reboot_control('adb reboot')

    def reboot_recovery(self):
        """android device reboot to recovery and connect with button reboot to recovery"""
        self.reboot_control('adb reboot recovery')

    def reboot_fastboot(self):
        """android device reboot to fastboot and connect with button reboot to fastboot"""
        self.reboot_control('adb reboot bootloader')

    def oem_unlock(self):
        """android device oem unlock control and connect with button oem unlock"""
        self.reboot_fastboot()
        self.oem_unlock_thread.start()

    def warning_msg(self, msg):
        """a warining window"""
        warningWindow = QtGui.QWidget()
        QtGui.QMessageBox.information(warningWindow, u"提示", msg)

    def check_adb_devices(self):
        """when start a item which check devices first"""
        device_list = []
        out_info = subprocess.Popen('adb devices', shell=True, stdout=subprocess.PIPE)
        more_list = out_info.communicate()[0].split('\r\n')
        for i in more_list:
            if 'List of devices attached' in i:
                continue
            if '\t' in i:
                device_list.append(i.split('\t')[1])
        if len(device_list) > 1:
            return False
        else:
            return True


class OemUnlockThread(QtCore.QThread):
    """oem unlock control control with a new thread"""

    REBOOT_SLEEP_TIME = 15
    OEM_CONTROL_TIME = 5

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        time.sleep(OemUnlockThread.REBOOT_SLEEP_TIME)
        subprocess.call('fastboot oem unlock', shell=True)
        time.sleep(OemUnlockThread.OEM_CONTROL_TIME)
        subprocess.call('fastboot reboot', shell=True)


class FlashRecoveryImage(QtCore.QThread):
    """flash recovery image with a new thread"""
    REBOOT_SLEEP_TIME = 15
    FASTBOOT_CONTROL_TIME = 10

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        time.sleep(FlashRecoveryImage.REBOOT_SLEEP_TIME)
        subprocess.call(str('fastboot flash recovery ' + ShaJJTools.recovery_image), shell=True)
        time.sleep(FlashRecoveryImage.FASTBOOT_CONTROL_TIME)
        subprocess.call(str('fastboot reboot'), shell=True)


class FlashBootImage(QtCore.QThread):
    """flash boot image with a new thread"""
    REBOOT_SLEEP_TIME = 15
    FASTBOOT_CONTROL_TIME = 10

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        time.sleep(FlashBootImage.REBOOT_SLEEP_TIME)
        subprocess.call(str('fastboot flash boot ' + ShaJJTools.boot_image), shell=True)
        time.sleep(FlashRecoveryImage.FASTBOOT_CONTROL_TIME)
        subprocess.call(str('fastboot reboot'), shell=True)


class FlashSideloadZip(QtCore.QThread):
    """flash sideload zip package with a new thread"""
    FASTBOOT_CONTROL_TIME = 240

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        subprocess.call(str('adb sideload ' + ShaJJTools.recovery_image), shell=True)
        time.sleep(FlashSideloadZip.FASTBOOT_CONTROL_TIME)
        subprocess.call(str('adb reboot'), shell=True)

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    run = ShaJJTools()
    run.show()
    sys.exit(app.exec_())
