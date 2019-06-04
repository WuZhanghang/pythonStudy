import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
plt.rcParams['font.sans-serif']='SimHei'
plt.rcParams['axes.unicode_minus']=False
data=pd.read_excel('C:/Users/Wuzhanghang/Desktop/tempdata/schooldata.xls')
fid=data['成员2身份证件号']
del fid[0]
del fid[10]
print(type(fid[1]))
fidy=[]


for i in fid:
    tempi=i[6:10]
    fidy.append(int(tempi))

        

    

plt.figure(figsize=(6,6))#画布为方形，饼图为正圆
y1=0
y2=0
y3=0
y4=0

for n in fidy:
    if int(n) <= 1970 :
        y1 +=1
    elif int(n) > 1970 and int(n) <=1975 :
             y2+=1
    elif int(n) > 1975 and int(n) <1980 :
             y3+=1
    elif int(n) >=80 and int(n) <=1985:
            y4+=1
print(y1,y2,y3,y4)
pdata=[y1,y2,y3,y4]
label=['60-70','71-75','76-79','80-85']
expload=[0.01,0.01,0.01,0.01]
plt.legend(['年龄中位数',np.mean(fidy)])
plt.pie(pdata,labels=label,autopct='%1.1f%%')
plt.title('年龄分布')
plt.show()
