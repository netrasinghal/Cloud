#!usr/bin/python

import os,time,sys,commands,socket,getpass
x='''
Service options :
1 for Firefox
2 for Gedit
3 for Calculator
4 for Webcam
5 for VLC
6 for office
7 for Screenshot
8 for Image Viewer '''

print x
ch=raw_input("Enter a choice to get the required service: ")
if ch=='1' :
	print "Firefox service"
	execfile('firefox.py')
elif ch=='2' :
	print "Gedit service"
	execfile('gedit.py')
elif ch=='3' :
	print "Calculator service"
	execfile('calculator.py')
elif ch=='4' :
	print "Webcam service"
	execfile('webcam.py')
elif ch=='5' :
	print "VLC media player service"
	execfile('vlc.py')
elif ch=='6' :
	print "Office service"
	execfile('office.py')
elif ch=='7' :
	print "Screenshot service"
	execfile('screenshot.py')
elif ch=='8' :
	print "Image viewer service"
	execfile('imageviewer.py')
else :
	print "Invalid option"
