#! /usr/bin/python!
# __*__ coding:utf-8 __*__

import socket

s = socket.socket()

hostname = socket.gethostname()

port = 10002

s.bind((hostname, port))

s.listen(5)
c, address = s.accept()
while True:
    strs = c.recv(1024)
    print  "客戶端：".decode("utf-8") + strs
    if strs == 'ok':
        c.close()
        s.close()
        break;
    mStr = raw_input('please input:')
    print "服務端：".decode("utf-8") + mStr
    c.send(mStr)
