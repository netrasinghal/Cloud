#!usr/bin/python

import os,time,sys,commands,socket,getpass
x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sip="192.168.122.1"

os.system("sshpass -p '123' ssh test@"+sip+" -X gnome-calculator")
execfile('saas.py')
