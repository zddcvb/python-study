# coding=utf-8
'''
Created on 2017年12月18日

@author: Administrator
'''
import os



class FileUtil(object):
    '''
    classdocs
    '''
    name = "";
    dic=[]

    def __init__(self):
        pass;
    
    def readFile(self, path):
        dirs = os.listdir(path)
        for index in dirs:
            newPath = path + "/" + index
#             print "new path:" + newPath
            self.dic.append(newPath)
            if os.path.isdir(newPath):
                self.readFile(newPath)
            else :
                    self.dic.append(index)
#                     print index;
        return self.dic;
    def __str__(self , *args, **kwargs):
        print args
        print kwargs
        return object.__str__(self, *args, **kwargs)
