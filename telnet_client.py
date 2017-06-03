#!/usr/bin/python

import os,time,sys,commands,socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#s_ip is ip of server and s_port is portno. 
s_ip="192.168.10.151"
s_port=3333

#telnet server username
user=raw_input("Enter username : ")

#telnet server password
password=raw_input("Enter user password : ")

s.sendto(user,(s_ip,s_port))
s.sendto(password,(s_ip,s_port))

print s.recvfrom(100)[0]

while True :
	cmd=raw_input("[root@localhost ]# ")
	s.sendto(cmd,(s_ip,s_port))
	print s.recvfrom(100)[0] 




