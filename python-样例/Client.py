#! /usr/bin/python!
# __*__ coding:utf-8 __*__

import socket
import time

s = socket.socket()
port = 10002
hostname = socket.gethostname()
s.connect((hostname, port))

while True:
    str = raw_input('please input:')
    print "客戶端：" .decode("utf-8")+ str
    s.send(str)
    time.sleep(1)
    recvStr = s.recv(1024)
    print "服務端：".decode("utf-8") + recvStr
    if recvStr == 'ok':
        s.close()
        break;