#!/usr/bin/python3

import cgi

# to receive data from web http protocol
print("Content-type:text/html")
print("")

html_data=cgi.FieldStorage()
#onlu looking for form data and those variables data as well 
username=html_data.getvalue('u')
password=html_data.getvalue('p')

if username == 'adhoc' and password == 'devops' :
    print("<meta http-equiv='refresh' content='1;url=http://54.84.162.166/service.html'>")

else   :
    print("no hello at all")
