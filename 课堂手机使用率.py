import pandas as pd
import numpy as np
import sys
import matplotlib as mpl
import matplotlib.pyplot as plt
sys.path.append(r'C:\Users\Administrator\Desktop\github\python-project')
import openpyxl

f = r'C:\Users\Administrator\Desktop\github\python-project\重庆公共运输职业学院课堂手机使用情况.xlsx'
df = pd.read_excel(f)
df1 = df.shift(1)

df.plot(kind='bar')
df1.plot()

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


fig = plt.figure()
plt.figure(figsize=(8, 4), dpi=100) #12,6
plt.subplot(111)
plt.grid(True)
plt.xlabel('日期')
plt.ylabel('学生手机使用率')
plt.yticks(np.linspace(0,1,8,endpoint=True))#y轴的分刻度
plt.title('重庆公共运输职业学院手机使用率数据')

plt.bar(df.values,color="green")

plt.plot(x1, df.values, color='red', linewidth=2.5, linestyle='-', label="使用率")
#    plt.plot(x1, y2, color='b', linewidth=2.5, linestyle='-', label="BTC价格")
plt.legend(loc='upper left')
plt.subplots_adjust(left=None, bottom=None, right=None, top=1.5, wspace=None, hspace=None)
    
    
    plt.subplot(2,1,2)
    plt.grid(True)
    plt.xlabel('日期')
    plt.ylabel('回撤率（%）')
    #plt.legend(loc='upper left' "回撤")
    plt.legend(loc='upper left')
    #plt.legend('回撤')
    sell_record_temp = sell_record2.copy()
    sell_record_temp.iloc[:,7] = np.array(list(map(lambda x:(sell_record_temp.iloc[x,6]-sell_record_temp.iloc[x,3])*sell_record_temp.iloc[x,4] if sell_record_temp.iloc[x,2]>0 else (sell_record_temp.iloc[x,3]-sell_record_temp.iloc[x,6])*sell_record_temp.iloc[x,4],range(len(sell_record_temp)))))
    right_ratio_all_temp = round(len(list(np.where(sell_record_temp.iloc[:,7]>0))[0])/len(sell_record_temp)*100,1)
 
    plt.title('目前收益: %s%%'%present_y1 + '  ' + '最大回测: %s%%'%drawdown  + '  ' +'发生日期: %s'%drawdown_i2 +'  ' + '夏普比率：%s'%sharpe_ratio +'\n' +'年化收益率：%s%%'%annual_return + '  ' + '最大收益率：%s%%'%h_y1 + '  ' + '最低收益率：%s%%'%ll_low + '  ' + '总开仓数：%s次'%len(sell_record_temp) + '  ' +'盈利率：%s%%'%right_ratio_all_temp)
    #plt.subplot(2,1,2).bar(x1,drawdown_rate,width=0.05,color='b', label="回撤")
    plt.bar(x1, drawdown_rate)
    #fig.subplots_adjust(right=0.7)
    #fig.set_size_inches(6.4, 4)
    #plt.subplots_adjust(top=0.8,bottom=0,left=0,right=0.8,hspace=0,wspace=0)
    #plt.savefig('./天深达-平台突破-MACD叠加-回测图形.jpeg',dpi=100)
    plt.tight_layout() #自动调增子图紧凑布局
    plt.show()