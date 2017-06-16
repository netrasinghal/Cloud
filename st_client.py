#usr/bin/python
import os,sys,socket,commands,time
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#ip and port of server
sip="192.168.122.119"
sport=4321

#name of the device client wants
dname=raw_input("Enter device name(without giving any space) : ")
#size of that device
dsize=raw_input("Enter the size of device (just the amount in MiB) : ")

s.sendto(dname,(sip,sport))
s.sendto(dsize,(sip,sport))

response1=s.recvfrom(50)
if response[0]=="This device already exists" :
	exit()
elif response[0] == "Success" :
	os.system("showmount -e "+sip)
	os.system("mkdir /media"+dname)
	os.system("mount "+sip+":/drive /media"+dname)
else :
	print "Drive not created"
