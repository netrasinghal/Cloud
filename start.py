#!usr/bin/python

import os,time,sys,commands,socket,getpass
x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sip="192.168.122.1"
sport=4321

print "** Enter authentication details **"
time.sleep(1)
#server username
uname=raw_input("Enter username: ")
#server password
passwd=getpass.getpass("Enter password: ")
x.sendto(uname,(sip,sport))
x.sendto(passwd,(sip,sport))

#after username and password verification
msg=x.recvfrom(100)[0]
if msg=="success" :
	print "Authentication successfull!"
	print "Services are being loaded..."
	time.sleep(2)
	execfile('saas.py')
else :
	print "Authentication unsuccessfull!"
	print msg
