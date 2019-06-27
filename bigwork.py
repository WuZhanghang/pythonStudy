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





#实验二

import pandas as pd
import numpy as np

data=pd.read_csv()
sj=pd.read_csv()
data['发生时间']=pd.to_datetime(data['发生时间'],,format='%Y%m%d%H%M%S')

timeDel=pd.Timedelta("1 sec")
sj["事件开始时间"]=data.iloc[sj["事件起始编号"]-1,0].values-timeDel
sj["事件结束时间"]=data.iloc[sj["事件结束编号"]-1,0].values+timeDel
sj["洗浴时间点"]=[i.hour for i in sj["事件开始时间"]]
temp1=sj["事件结束时间"]-sj["事件开始时间"]temp1)/1000000000
sj["总用水时长"]=np.int64

#构造用水停顿事件
for i in range(len(data)-1):
    if(data.loc[i,"水流量"]!=0)&(data.loc[i+1,"水流量"==0]):
        data.loc[i+1,"停顿开始时间"]=\
        data.loc[i+1,"发生时间"]-timeDel
    if(data.loc[i,"水流量"]==0)&(data.loc[i+1,"水流量"!=0]):
        data.loc[i,"停顿结束时间"]=\
        data.loc[i,"发生时间"]+timeDel


#提取停顿开始时间与结束时间对应的行号
indStopStart=data.index[data["停顿开始时间"].notnull()]+1
indStopEnd=data.index[data["停顿结束时间"].notnull()]+1
Stop=pd.DataFrame(data={"停顿开始编号":indStopStart[:-1],"停顿结束编号":indStopEnd[1:]})

#计算停顿时长
tmp2=data.loc[indStopEnd[1:]-1,"停顿结束时间"]
tmp3=data.loc[indStopStart[:-1]-1,"停顿开始时间"]
tmp4=tmp2.values-tmp3.values
Stop["停顿时长"]=np.int64(tmp4)/1000000000

#将每次停顿与事件匹配
for i in range(len(sj)):
    Stop.loc[(Stop["停顿开始编号"]>sj.loc[i,"事件起始编号"])&(Stop["停顿结束编号"]<sj.loc[i,"事件终止编号"]),"停顿归属事件"]=i+1


Stop=Stop[Stop["停顿归属事件"].notnull()]

#构造特征
stopAgg=Stop.groupby("停顿归属事件").agg({"停顿时长":sum,"停顿开始编号":len})

sj.loc[stopAgg.index-1,"总停顿时长"]=\
    stopAgg.loc[:,"停顿时长"].values
sj.loc[stopAgg.index-1,"停顿次数"]=\
    stopAgg.loc[:,"停顿开始编号"].values

sj.fillna(0,inplace=True)
stopNo0=sj["停顿次数"]!=0#判断用水是否停顿
sj.loc[stopNo0,"平均停顿时长"]=\
sj.loc[stopNo0,"总停顿时长"]/sj.loc[stopNo0,"停顿次数"]
sj.fillna(0,inplace=True)
sj["用水时长"]=sj["总用水时长"]-sj["总停顿时长"]

sj["用水/总时长"]=sj["用水时长"]/sj["总用水时长"]

print("用水事件用水时长与频率特征构造完成后数据的特征为：\n",sj.columns)
print("用水事件用水时长与频率特征构造完成后数据的前5行5列特征： \n",sj.iloc[:5,:5])


#构建用水量与波动特征

data["水流量"]=data["水流量"]/60
sj["总用水量"]=0
for i in range(len(sj)):
    Start=sj.loc[i,"事件起始编号"]-1
    End=sj.loc[i,"事件终止编号"]-1
    if Start!=End:
        for j in range(Start,End):
            if data.loc[j,"水流量"]!=0:
                sj.loc[i,"总流量"]=(data.loc[j+1,"发生时间"]-data.loc[j,"发生时间"]).seconds*\
                    data.loc[j,"水流量"]+\
                    sj.loc[i,"总用水量"]
        sj.loc[i,"总用水量"]=sj.loc[i,"总用水量"]+\
        data.loc[End,"水流量"]*2
    else:
        sj.loc[i,"总用水量"]=data.loc[Start,"水流量"]*2

sj["平均水流量"]=sj["总用水量"]/sj["用水时长"]


sj["水流量波动"]=0
for i in range(len(sj)):
    Start=sj.loc[i,"事件起始编号"]-1
    End=sj.loc[i,"事件终止编号"]-1
    for j in range(Start,End+1):
        if data.loc[j,"水流量"]!=0:
            slbd=(data.loc[j,"水流量"]-sj.loc[i,"平均水流量"])**2
            slsj=(data.loc[j+1,"发生事时间"]-data.loc[j,"发生时间"]).seconds
            sj.loc["水流量波动"]=slbd*sj.loc[i,"水流量波动"]
        
    sj.loc[i,"水流量波动"]=sj.loc[i,"水流量波动"]/sj.loc[i,"用水时长"]


sj["停顿时长波长"]=0
for i in range(len(sj)):
    if sj.loc[i,"停顿次数"]>1:
        for j in Stop.loc[Stopp["停顿归属事件"]==(i+1),"停顿时长"].values:
            sj.loc[i,"停顿时长波动"]=((j-sj.loc[i,"平均停顿时长"])**2)*j+sj.loc[i,"停顿时长波动"]

        sj.loc[i,"停顿时长波动"]=sj.loc[i,"停顿时长波动"]/sj.loc[i,"总停顿时长"]

print("用水量和波动特征构造完成后数据的特征为：\n",sj.columns)
print("用水量和波动特征构造完成后数据的前5行5列特征为:\n",sj.loc[:5,:5])



#筛选候选洗浴事件
sj_bool=(sj["用水时长"]>100)&(sj["总用水时长"]>120)&(sj["总用水量"]>5)
sj_final=sj.loc[sj_bool,:]
sj_fianl.to_excel("sj_fianl.xlsx",index=False)
print("筛选出候选洗浴事件前的数据形状：",sj.shape)
print("筛选出候选洗浴事件后的数据形状：",sj_final.shape)
        



#增加的备注







