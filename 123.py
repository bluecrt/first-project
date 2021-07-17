#coding:utf-8
import os
import re
import sys

a=os.popen('netsh wlan show profiles')
b=a.read()
c=re.findall('所有用户配置文件 : (.*?)\n    所有用户配置文件',b,re.S)
print(c)
for i in c:
    a=os.popen('netsh wlan show profiles '+i+' key=clear')
    b=a.read()
    c=re.findall('关键内容            : (.*?)\n\n费用设置',b,re.S)
    for ii in c:
        e=open('1.txt','a+')
        e.write(i+' : '+ii+'\n')
sys.exit()