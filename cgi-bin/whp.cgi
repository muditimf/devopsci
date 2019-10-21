#!/usr/bin/python3

import cgi.cgitb
cgitb.enable()

# to receive data from web http protocol
print("Content-type:text/html")
print("")

html_data=cgi.FieldStorage()
#onlu looking for form data and those variables data as well =html_data.getvalue('s')
tech=html_data.getvalue('t')

if tech == "docker" :
    print("<meta http-equiv='refresh' content='1;url=http://54.84.162.166/docker.html'>")

else   :
    print("<meta http-equiv='refresh' content='1;url=http://54.84.162.166/aws.html'>")
