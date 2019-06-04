import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.interppolate
# data=pd.read_csv('C:/Users/Wuzhanghang/Desktop/tempdata/exp4/missing_data.csv')
# print(data)
eloss=pd.read_csv('C:\Users\Wuzhanghang\Desktop\tempdata\exp4\ele_loss.csv',sep=',',encoding='gb18030')
ealarm=pd.read_csv('C:\Users\Wuzhanghang\Desktop\tempdata\exp4\alarm.csv',sep=',',encoding='gb18030')

detail1=pd.read_csv('C:\Users\Wuzhanghang\Desktop\tempdata\exp4\ele_loss.csv',index_col=0,encoding='gbk')
detail2=pd.read_csv('C:\Users\Wuzhanghang\Desktop\tempdata\exp4\alarm.csv',index_col=0,encoding='gbk')
print('线损数据表的形状：',detail1)
print('用电量趋势与线路告警的形状：',detail2)
eloss['ID']=eloss['ID'].astype('str')
ealarm['date']=ealarm['date'].astype('str')
data=pd.merge(eloss,ealarm,left_on='ID',right_on='date',how='inner')
print('两张表数据主键合并后的大小为：',data.shape)


