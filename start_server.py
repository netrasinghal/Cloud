#!/usr/bin/python2

import os,time,sys,commands,socket
x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
x.bind(("",4321))

#receiving username
data=x.recvfrom(100)
#receiving password
data1=x.recvfrom(100)

if data[0]=="test" and data1[0]=="123" :
	x.sendto("success",(data[1]))
else :
	x.sendto("Enter correct username and password",(data1[1]))
