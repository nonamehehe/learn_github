# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 11:35:00 2019

@author: ASUS
"""
from urllib import request
fp = request.urlopen('http://www.cqjtkt.cn/')
content = fp.read()
print(content)
import requests
from bs4 import BeautifulSoup
url = "http://www.cqjtkt.cn/"
page =requests.get(url)
print(page.status_code)
print(page.content)
soup = BeautifulSoup(page.content, 'html.parser')

import urllib.request
import re
 
def getHtml(url):
    html=urllib.request.urlopen(url).read()
    html= html.decode('utf-8')
    return html
 
def getImg(html):
    #构建正则表达式，从页面代码里提取出图片url地址。
    img_re=re.compile(r'(?<=src=")\S+?jpg')
    #输出找到图片的类型
    print("the type of html is :",type(html))
    #输出整个html的结构
    print(html)
    #返回一个装img下载地址的集合
    img_list=img_re.findall(html)
    return img_list
 
def getUrl(source):
    if source.startswith("//"):
        url = "http:"+source
    else:
        url=source
    
    return url
#调用getHtml函数输入网址   
html=getHtml("http://www.cqjtkt.cn/")
#调用getImg函数得到集合
img_list = getImg(html)
print("正在下载图片......")
 
for i in range(len(img_list)):
    print(img_list[i])
    #调用urlretrieve方法把图片下载到指定地址
    urllib.request.urlretrieve(getUrl(img_list[i]),'.\img\%s.jpg' % i)
    
print("完成图片下载......")


