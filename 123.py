#coding:utf-8
import os
import re
import sys

a=os.popen('netsh wlan show profiles')
b=a.read()
c=re.findall('�����û������ļ� : (.*?)\n    �����û������ļ�',b,re.S)
print(c)
for i in c:
    a=os.popen('netsh wlan show profiles '+i+' key=clear')
    b=a.read()
    c=re.findall('�ؼ�����            : (.*?)\n\n��������',b,re.S)
    for ii in c:
        e=open('1.txt','a+')
        e.write(i+' : '+ii+'\n')
sys.exit()