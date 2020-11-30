# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 10:52:51 2019

@author: Administrator
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

f = r'C:\Users\Administrator\Desktop\github\python-project\英语成绩汇总.xlsx'
df_analysis_english_score = pd.read_excel(f)
df_analysis_english_score.columns = ["听力成绩","阅读理解成绩","语言知识运用成绩",'写作成绩']
df_analysis_english_score.plot()
df_growth_rate = df_analysis_english_score/df_analysis_english_score.shift(1)
df_growth_rate = (df_growth_rate-1)*100
df_growth_rate.plot.bar()

df_all_growth_rate = df_analysis_english_score.sum(axis=1)
df_all_growth_rate = pd.DataFrame(df_all_growth_rate,columns = ["英语成绩总体平均分"])
df_all_growth_rate.plot()

df_var = df_analysis_english_score.var()
df_var = pd.DataFrame(df_var,columns = ['各部分方差情况'])
plt.plot(df_var)
plt.title('各部分方差情况')



