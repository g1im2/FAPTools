#-*-coding:utf-8-*-
__author__ = 'fxf'

from PyQt4 import QtGui

class LogHelper(object):

    def __init__(self):
        pass

    #Get logs file and analysis of it
    def getLogsLine(self,files):
        i = 0
        items = []
        keyword_List = []
        numberDicts = {}
        try:
            f = open(files, 'r')
            filesname = f.name
            read = f.readlines()
            f.close()
            for line in read:
                i += 1
                keyword = line.split(' ')[2]
                keyword_List.append(keyword)
                if keyword not in items:
                    items.append(keyword)
            for key in items:
                numberDicts[key] = keyword_List.count(key)
            countDicts = sorted(numberDicts.iteritems(), key=lambda asd: asd[1], reverse=True)
            print type(countDicts)

            # test only
            print countDicts
            #Creat new result files for CountLines
            newname = self.set_newName(filesname)
            print newname
            fi = open(newname, "a+")
            fi.write('the logs counts is ' + str(i) + '\n')
            for words in countDicts:
                fi.write(words[0] + "-------------------------:" + str(words[1]) + "\n")
            fi.close()
            successWindow = QtGui.QWidget()
            QtGui.QMessageBox.information(successWindow,u"Completed",u"logs Count success")
        except IOError:
            warningWindow = QtGui.QWidget()
            QtGui.QMessageBox.information(warningWindow, u"Warning", u"Please choice logs file")
            print 'no found target logs files'

    def set_newName(self,names):
        if '\\' in names:
            systemTags = '\\'
        else:
            systemTags = '/'
        new_name = names.split(systemTags)
        new_name[-1] = 'result_'+ new_name[-1]
        real_Name = new_name[0]
        new_numbers = len(new_name)
        for i in range(1, new_numbers):
            real_Name = real_Name + systemTags + new_name[i]
        return real_Name
