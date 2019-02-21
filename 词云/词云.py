# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 19:45:33 2019

@author: ASUS
"""
import jieba
text="李小璐给王思聪买了微博热搜"
result=jieba.cut(text)
print("切分结果:  "+",".join(result))