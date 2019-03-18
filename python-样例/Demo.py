#! /usr/bin/python!
# __*__ coding:utf-8 __*__

import os

# fileList=os.listdir("d:/")
# for var in fileList:
#     print "d:/"+var


fileList=os.walk("d:/")

for parent,dirnames,filenames in fileList:
    for dirname in dirnames:
        print parent+os.sep+dirname
    for filename in filenames:
        print parent+os.sep+filename

