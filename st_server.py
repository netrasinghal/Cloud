#usr/bin/python
import os,sys,socket,commands,time
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("",4321))

#receiving device name given by client
data=s.recvfrom(100)
#receiving device size
data1=s.recvfrom(100)

dname=data[0]
dsize=data1[0]
cl_addr=data1[1][0]

#pysical volume created '/dev/vdb1' created
#virtual group 'mysystem' created
while True:
  if os.path.isdir(dname) :
	s.sendto("This device already exists",data[1])
  else :
	os.system("lvcreate --size 19G --thin mysystem/pool1")
	os.system("lvcreate -V"+dsize+"M --name "+dname+" --thin mysystem/pool1")
	os.system("mkdir /mnt/"+dname)
	os.system("mkfs.xfs /dev/mysystem/"+dname)
	os.system("mount /dev/mysystem/"+dname+" /mnt/"+dname)
	os.system("yum install nfs-utils")
	f=open("/etc/exports","a")
	msg="/drive "+cl_addr+"(rw,no_root_squash)"
	f.write(msg)
	f.write("\n")
	os.system("systemctl restart nfs-server")
	os.sytem("exportfs -r")
	os.system("iptables -F")
	os.system("setenforce=0")
	s.sendto("Success",data1[1])
