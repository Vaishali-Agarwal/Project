#!/usr/bin/python

import cgi
print "Content-type:text/html\r\n\r\n"
#print ""

data=cgi.FieldStorage()

u=data.getvalue('x')
p=data.getvalue('y')

print u 
print p

