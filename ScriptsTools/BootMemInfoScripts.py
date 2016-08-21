# coding=utf-8
__author__ = 'fxf'

#work for: 用于进行Android设备的常驻进程测试。减少测试环节的手动输入，以及以严格模式对测试条件进行限制
#          重启时间为60秒
#          等待抓取时间为5分钟（300秒）
#          结果输出在该脚本相同文件夹内
#create on 2015-11-17
#change log: 2015-11-18, 改变输出结果的方式
#notice：为了在不同的电脑上没有乱码，输出方式最好不要使用中文。
#        该脚本为单线程，故可以使用pyinstaller打包成单个exe包

import xlwt
import time
import subprocess
import sys

class BootMemInfoScripts(object):

    def __init__(self):
        pass

    def runscripts(self):
        file = xlwt.Workbook()
        first_count = 1
        second_count = 4
        #设置两个字典，用于存储测试结果
        presistent_first = {"presistent_1": [], "presistent_2": [], "presistent_3": []}
        presistent_second = {"presistent_4": [], "presistent_5": [], "presistent_6": []}
        if self.StartNotification() == 1:
            sys.exit()
        else:
            table = file.add_sheet('MemInfo_Data', cell_overwrite_ok=True)
            table.write(0, 0, "Environment")
            #为表格写入抬头
            for i in range(3):
                table.write(0, i+1, "first datas")
                table.write(0, i+4, "second datas")
            for i in presistent_first:
                # self.rebootAndSleep("start")
                # self.rebootAndSleep("continue")
                #取得第一组数据，为表格抬头做准备
                if i == "presistent_1":
                    #为表格写入环境名称
                    presistent_values = self.CheckBootMemInfo()
                    first_presisent_values = self.FirstSheetValues(presistent_values)
                    presistent_first[i] = self.SecondSheetValues(presistent_values)
                    first_presisent_values.append("Total")
                    first_presisent_values.append("AVERAGE")
                    #将取得的环境名称以及预置名称写入表格
                    for k in range(1, len(first_presisent_values)+1):
                        table.write(k, 0, first_presisent_values[k-1])
                else:
                    presistent_first[i] = self.SecondSheetValues(self.CheckBootMemInfo())
                for values in range(1, len(presistent_first[i])+1):
                    table.write(values, first_count, presistent_first[i][values-1])
                first_count += 1
        #求得三组数据的平均值
        first_average = (int(presistent_first["presistent_1"][-1].split(" ")[0]) +
                         int(presistent_first["presistent_2"][-1].split(" ")[0]) +
                         int(presistent_first["presistent_3"][-1].split(" ")[0]))/3
        table.write(len(presistent_first["presistent_1"])+1, 1, str(first_average) + " kB")
        #设置询问，等待切换语言，如果不进行，则在保存测试结果后退出
        if self.MessageNotifications() == 1:
            file.save("./Meminfo" + str(int(time.time())) + ".xls")
            sys.exit()
        else:
            for i in presistent_second:
                # self.rebootAndSleep("start")
                # self.rebootAndSleep("continue")
                presistent_second[i] = self.SecondSheetValues(self.CheckBootMemInfo())
                for values in range(1, len(presistent_second[i])+1):
                    table.write(values, second_count, presistent_second[i][values-1])
                second_count += 1
            #求得第二组数据的平均值
            second_average = (int(presistent_second["presistent_4"][-1].split(" ")[0]) +
                             int(presistent_second["presistent_5"][-1].split(" ")[0]) +
                             int(presistent_second["presistent_6"][-1].split(" ")[0]))/3
            table.write(len(presistent_first["presistent_1"])+1, 4, str(second_average) + " kB")
            file.save("./Meminfo" + str(int(time.time())) + ".xls")

    #取得第一组数据作为表格抬头
    def FirstSheetValues(self, values_list):
        return_list = []
        for i in range(1, len(values_list)):
            return_list.append(values_list[i].split(":")[1].split(" ")[1])
        return return_list

    #取得测试结果
    def SecondSheetValues(self, values_list):
        return_values_list = []
        for i in range(1, len(values_list)):
            return_values_list.append(values_list[i].split(":")[0].lstrip())
        return_values_list.append(values_list[0].split(":")[0].lstrip())
        return return_values_list

    #进行dumpsys meminfo操作，并将取得的Presisent数据以列表的形式返回
    def CheckBootMemInfo(self):
        persistent_info = []
        start_int = 0
        end_int = 0
        p = subprocess.Popen("adb shell dumpsys meminfo", shell=True, stdout=subprocess.PIPE)
        pi = p.communicate()
        meminfo_list = pi[0].split("\r\r\n")
        for info in meminfo_list:
            if "Persistent" in info:
                start_int = meminfo_list.index(info)
            if "Foreground" in info:
                end_int = meminfo_list.index(info)
        for persistent_values in range(start_int, end_int):
            persistent_info.append(meminfo_list[persistent_values])
        return persistent_info

    #设置重启以及等待时间
    def rebootAndSleep(self,items):
        #设置重启等待时间：60s
        if items == "start":
            subprocess.call("adb reboot", shell=True)
            for i in range(60):
                time.sleep(1)
                print "wait for reboot " + str(i+1) + "/60s times"
        #设置等待时间：300s
        elif items == "continue":
            for j in range(300):
                time.sleep(1)
                print "wait for catch meminfo  " + str(j+1) + "/300 times"

    #结果直接输出
    #不再使用该形式，改为将测试结果解析后输出为表格，该方法弃用2015-11-18
    def WriteOnFiles(self):
        write_files = open("D:\\Persistent_info.txt", "a+")
        persistent_list = self.CheckBootMemInfo()
        for info in persistent_list:
            write_files.write(info+"\n");
        write_files.close()

    #更换语言的提示，应用等待输入换取无限的等待时间，知道按下enter为止，并根据输入结果返回相对应的数值
    def MessageNotifications(self):
        notification = raw_input("Now, please change Android devices' languages and press Enter to continue\nOr you want leave and please input 'N': ")
        if notification.upper() == 'N':
            return 1
        else:
            return 0

    #开始测试的提示，应用等待输入换取无限的等待时间，知道按下enter为止，并根据输入结果返回相对应的数值
    def StartNotification(self):
        notification = raw_input("If you do it well ,press Enter \nOr you want leave and please input 'N': ")
        if notification.upper() == "N":
            return 1
        else:
            return 0

#主运行，主要调用runscripts方法
if __name__ == "__main__":
    print """
    This Scripts will catch meminfo with Android Devices by auto.
    Notice: the result xls files will be create on current path
    First you must do somethings with this:
    1. Android Devices factory reset.
    2. Do not install any apps.
    """
    runs = BootMemInfoScripts()
    runs.runscripts()