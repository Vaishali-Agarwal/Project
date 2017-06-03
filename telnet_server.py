#!/usr/bin/python

import os,sys,commands,time,socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(("",3333))

#data stores the username ip and port no.
data=s.recvfrom(100)

#data1 stores user password ip and port no.
data1=s.recvfrom(100)

if data[0] == 'root' and data1[0] == 'redhat' :
	s.sendto("connected !!",data[1])
	while True :
		#rcmd is the command received from client to execute
		rcmd=s.recvfrom(100)[0]

		#output stores the output of the command entered by client 
		output=commands.getoutput(rcmd)
		s.sendto(output,data[1])

else :
	s.sendto("Not Connected !!",data[1])
