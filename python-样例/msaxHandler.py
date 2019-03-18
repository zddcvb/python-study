#! /usr/bin/python!
# __*__ coding:utf-8 __*__
import xml.sax


class msaxHandler(xml.sax.ContentHandler):
    def __init__(self):
        print '__init__'
        self.CurrentData = ""
        self.name = ""
        self.age = ""
        self.list = list

    def startDocument(self):
        print 'document start'

    def endDocument(self):
        print 'document end'

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == 'person':
            print '======person======'
            gendar = attributes['gendar']
            print 'gendar:' + gendar

    def endElement(self, tag):
        if self.CurrentData == 'name':
            print 'name:' + self.name
        elif self.CurrentData == 'age':
            print 'age:' + self.age
        self.CurrentData = ''

    def characters(self, content):
        if self.CurrentData == 'name':
            self.name = content
        elif self.CurrentData == 'age':
            self.age = content

# if __name__ == '__main__':
#     parse = xml.sax.make_parser()
#     parse.setFeature(xml.sax.handler.feature_namespaces, 0)
#     parse.setContentHandler(msaxHandler())
#     parse.parse('person.xml')
