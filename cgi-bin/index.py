import os
f=open(os.getcwd()+'/template/index.html','r', encoding="UTF-8")
s=f.read()
f.close()
print("Content-type: text/html\n")
print(s)
