#!/usr/bin/python
import os
import sys
import getpass


u=raw_input("enter username :")
os.system('useradd '+u)
p=getpass.getpass("enter password:")
os.system('echo '+p+ ' |passwd '+u+' --stdin')



'''u=sys.argv[1:]
print u
for i in u:
	print i
	os.system('useradd '+i)
	
	os.system('echo '+i+' | passwd '+i+' --stdin')'''
