import os, cgi
import sys
import subprocess

form = cgi.FieldStorage()
nick = form.getfirst("nick", "не задано")

f=open(os.getcwd()+'/template/form.html','r', encoding="UTF-8")
s=f.read()

fileout = open(os.getcwd()+'/cgi-bin/sherlock/scan.txt', 'w')
theproc = subprocess.Popen(os.getcwd()+"/cgi-bin/sherlock/sherlock.py "+nick, stdout=fileout, shell = True)
theproc.communicate()
fileout.close()

f=open(os.getcwd()+'/cgi-bin/sherlock/scan.txt','r', encoding="UTF-8")
r=f.read()
f.close()
s=s.replace('%result%', r)
f.close()
print("Content-type: text/html\n")
print(s)

