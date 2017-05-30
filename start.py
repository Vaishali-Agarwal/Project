#!/usr/bin/python

import os
import time
import getpass
print "welcome to aed cloud"
print "---------------------------"

user=raw_input("enter user name :")
password=getpass.getpass("enter password :")
if user=='root' and password=='redhat' :
	print "access granted"
	time.sleep(2)
	print "plz wait"
	exec file('useradd.py')
else :
	print "check authentication"
