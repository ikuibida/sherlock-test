import os, cgi
import sys
import subprocess

form = cgi.FieldStorage()
nick = form.getfirst("nick", "не задано")

fileout = open(os.getcwd()+'/cgi-bin/sherlock/scan.txt', 'w')
theproc = subprocess.Popen(os.getcwd()+"/cgi-bin/sherlock/sherlock.py "+nick, stdout=fileout, shell = True)
theproc.communicate()
fileout.close()

f=open(os.getcwd()+'/cgi-bin/sherlock/scan.txt','r', encoding="UTF-8")
r=f.read()
f.close()

f=open(os.getcwd()+'/template/form.html','r', encoding="UTF-8")
htmltemplate=f.read()
f.close()
htmltemplate=htmltemplate.replace('%result%', r)

print("Content-type: text/html\n")
print(htmltemplate)

