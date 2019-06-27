import numpy as np
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.p


Xtrain=pd.read_excel("sj_final.xlsx")
Ytrain=pd.read_excel("water_heater_log.xlsx")
test=pd.read_excel("test_data.xlsx")


x_train,x_test,y_train,y_test=Xtrain.iloc[:,5:],test.iloc[:4:-1],ytrain.iloc[:,-1],test.iloc[:,-1]
#标准化
stdScaler=StandardScaler().fit(x_train)
x_stdtrain=stdScaler.transform(x_train)
x_stdtest=stdScaler.transform(x_test)
#建立标准模型
bpnn=MLPClassifier(hidden_layer_sizes=(17.10),max_iter=200,solver='lbfgs',random_state=50)
bpnn.fit(x_stdtrain,y_train)

joblib.dump(bpnn,'water_heater_nnet.m')
print('构建的模型为：\n',bpnn)


#模型预测
from
from
from
import matplotlib.pyplot as plt

bpnn=joblib.load('water_heater_nnet.m')
y_pred=bpnn.predict(x_stdtest)
print("神经网络预测结果平评价报告：\n",classification_report(y_test,y_pred))

plt.rcParams['font.sans-serif']='SimHei'
plt.rcParams['axes.unicode_minus']=False
fpr,tpr,thresholds=roc_curve(y_pred,y_test)
plt.figure(figsize=(6,4))
plt.plot(fpr,tpr)
plt.title('用户用水事件识别ROC曲线')
plt.xlabel('FPR')
plt.ylabel('TPR')
plt.savefig('用户用水事件识别ROC曲线.png')
plt.show()
