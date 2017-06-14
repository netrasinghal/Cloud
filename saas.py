#!usr/bin/python

import os,time,sys,commands,socket,getpass
x='''
Service options :
1 for Firefox
2 for Gedit
3 for Calculator
4 for Webcam
5 for VNC
6 for office
7 for Image Viewer '''

print x
ch=raw_input("Enter a choice to get the required service: ")
if ch=='1' :
	print "Firefox service"
	execfile('firefox.py')
elif ch=='2' :
	print "Gedit service"
	execfile('gedit.py')
else :
	print "Invalid option"
