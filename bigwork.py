import pandas as pd
import numpy as np

data=pd.read_excel()
print('初始状态的数据形状为',data.shape)

data.drop(labels=["热水器"，"有无水流","节能模式"],axis=1,inplace=True)
print("删除冗余特征后的数据形状为：",data.shape)
data.to_csv("./tmp/water_heart.csv",index=False)


#划分用水事件

threshold=pd.Timedelta('4 min')
data['发生时间']=pd.to_datetime(data['发生时间']，format='%Y%m%d%H%M%S')
data=data[data['发生时间']>0]
sjKs=data['发生时间'].diff()>threshold
sjKs.iloc[1:]
sjJs=sjKs.iloc[1:]

sjKs=pd.concat([sjJs,pd.Series(True)])

sj=pd.DataFrame(np.arange(1,sum(sjKs)+1),columns=['事件序号'])
sj["事件起始编号"]=data.index[sjKs==1]+1 #定义起始编号
sj["事件终止编号"]=data.index[sjJs==1]+1
print('当阈值为4 min的时候事件数目为：',sj.shape[0])
sj.to_csv("./tmp/sj.csv",index=False)


#确定单次用水时长阈值
n=4
threshold=pd.timedelta(minutes=5)
data['发生时间']=pd.to_datetime(data['发生时间'],format='%Y%m%d%H%M%S')
data=data[data['水流量']>0]

def event_num(ts):
    d=data['发生时间'].diff()>ts
    return d.sum()+1


dt=[pd.Timedelta(minutes=i)for i in np.arange(1,9,0.25)]
h=pd.DataFrame(dt,columns=['阈值'])
h['事件数']=h['阈值'].apply(event_num)
h['斜率']=h['事件数'].diff()/0.25

h['斜率指标']=h['斜率'].abs().rolling(4).mean()
ts=h['阈值'][h['斜率指标'].idxmin()-n]

if ts >threshold:
    ts=pd.Timedelta(minutes=4)
print('计算出的单次用水时长的阈值：',ts)



########## parttwo

import pandas as pd
import numpy as np
data=pd.read_excel('')
print('初始状态的数据形式：',data.shape)

data.drop(labels=['热水器编号','有无水流','节能模式'],axis=1,inplace=True)
print('删除冗余特征后的数据形状为：',data.shape)
data.to_csv('./')


threshold=pd.Timedelta('4 min')
data['发生时间']=pd.to_datetime(data['发生时间'],format='%Y%m%d%H%M%S')
data=data[data['水流量']>0]

sjks=data['发生时间'].diff() > threshold
sjKs.iloc[0]=True
sjJs=sjKs.iloc[1:]

sjKs=pd.concat([sjKs,pd.Series(True)])

sj=pd.DataFrame(np.arange(1,sum(sjKs)+1),columns=['事件序号'])
sj['事件起始编号']=data.index[sjKs==1]+1
sj['事件终止编号']=data.index[sjJk==1]+1
print("当阈值为4 min的时候事件数目为：",sj.shape[0])
sj.to_csv('')

#确定单次用水时长
n=4
threshold=pd.Timedelta(minutes=5)
data['发生时间']=pd.to_datetime(data['发生时间'],,format='%Y%m%d%H%M%S')
data=data[data['水流量']>0]

def event_num(ts):
    d=data['发生时间'].diff()>ts
    return d.sum()+1

dt=[pd.Timedelta(minutes=i)for i in np.arange(1,9,0.25)]
h=pd.DataFrame(dt,columns=['阈值'])
h['事件数']=h['阈值'].apply(event_num)
h['斜率']=h['事件数'].diff()/0.25

h['斜率指标']=h['斜率'].abs().rolling(4).mean()
ts=h['阈值'][h['斜率指标'].idxmin()-n]


#用idxmin返回最小值的index

if ts> threshold:
    ts=pd.Timedelta(minutes=4)
print('计算出单次用水时长的阈值：',ts)




