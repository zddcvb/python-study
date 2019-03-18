#! /usr/bin/python!
# __*__ coding:utf-8 __*__
import xml.sax
from  msaxHandler import *


def parseXml(path):
    parse = xml.sax.make_parser()
    parse.setFeature(xml.sax.handler.feature_namespaces, 0)
    parse.setContentHandler(msaxHandler())
    parse.parse(path)


# parseXml('person.xml')
parseXml('d:/person.xml')
