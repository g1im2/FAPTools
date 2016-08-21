# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\ShaJJTools.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    """ShaJJToolsUI code with PyQt4 by auto with command pyuic.py"""
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(682, 163)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.recovery_line = QtGui.QLineEdit(Form)
        self.recovery_line.setObjectName(_fromUtf8("recovery_line"))
        self.horizontalLayout.addWidget(self.recovery_line)
        self.rec_bt = QtGui.QPushButton(Form)
        self.rec_bt.setObjectName(_fromUtf8("rec_bt"))
        self.horizontalLayout.addWidget(self.rec_bt)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.boot_line = QtGui.QLineEdit(Form)
        self.boot_line.setObjectName(_fromUtf8("boot_line"))
        self.horizontalLayout_4.addWidget(self.boot_line)
        self.boot_button = QtGui.QPushButton(Form)
        self.boot_button.setObjectName(_fromUtf8("boot_button"))
        self.horizontalLayout_4.addWidget(self.boot_button)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.sideload_line = QtGui.QLineEdit(Form)
        self.sideload_line.setObjectName(_fromUtf8("sideload_line"))
        self.horizontalLayout_2.addWidget(self.sideload_line)
        self.sideload_bt = QtGui.QPushButton(Form)
        self.sideload_bt.setObjectName(_fromUtf8("sideload_bt"))
        self.horizontalLayout_2.addWidget(self.sideload_bt)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.oem_bt = QtGui.QPushButton(Form)
        self.oem_bt.setObjectName(_fromUtf8("oem_bt"))
        self.horizontalLayout_3.addWidget(self.oem_bt)
        self.reboot_bt = QtGui.QPushButton(Form)
        self.reboot_bt.setObjectName(_fromUtf8("reboot_bt"))
        self.horizontalLayout_3.addWidget(self.reboot_bt)
        self.fastboot_bt = QtGui.QPushButton(Form)
        self.fastboot_bt.setObjectName(_fromUtf8("fastboot_bt"))
        self.horizontalLayout_3.addWidget(self.fastboot_bt)
        self.enter_rec_bt = QtGui.QPushButton(Form)
        self.enter_rec_bt.setObjectName(_fromUtf8("enter_rec_bt"))
        self.horizontalLayout_3.addWidget(self.enter_rec_bt)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.start_bt = QtGui.QPushButton(Form)
        self.start_bt.setObjectName(_fromUtf8("start_bt"))
        self.horizontalLayout_3.addWidget(self.start_bt)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "杀J工具包", None))
        self.label.setText(_translate("Form", "recovery镜像文件", None))
        self.rec_bt.setText(_translate("Form", "选择img文件", None))
        self.label_3.setText(_translate("Form", "boot镜像文件    ", None))
        self.boot_button.setText(_translate("Form", "选择img文件", None))
        self.label_2.setText(_translate("Form", "sideload刷机    ", None))
        self.sideload_bt.setText(_translate("Form", "选择zip包", None))
        self.oem_bt.setText(_translate("Form", "解锁OEM", None))
        self.reboot_bt.setText(_translate("Form", "重启", None))
        self.fastboot_bt.setText(_translate("Form", "进入fastboot", None))
        self.enter_rec_bt.setText(_translate("Form", "进入recovery", None))
        self.start_bt.setText(_translate("Form", "刷机", None))

