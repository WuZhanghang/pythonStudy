import requests
from bs4 import BeautifulSoup

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

urllst = []
ui = 'https://travel.qunar.com/p-cs299878-shanghai-jingdian-1-'
for i in range(1,4):
    urllst.append(ui +str(i))


# u1=urllst[1]
# r=requests.get(u1)
# soup=BeautifulSoup(r.text, 'lxml')
# print(soup)
# ul = soup.find('table')
# tr = ul.find_all('tr')
# datai = []
# n=0
# for i in tr:
#     n+=1
#     #print(i.text)
#     dic = {}#字典
#     dic['姓名'] = i[0]
#     dic['出生日期'] = i[1]
#     dic['来自']=i[2]
#     # dic['景点名称'] = i.find('span',class_="cn_tit").text
#     # dic['攻略提到数量'] = i.find('div',class_="strategy_sum").text
#     # dic['点评数量'] = i.find('div',class_="comment_sum").text
#     # dic['景点排名'] = i.find('span',class_="ranking_sum").text
#     # dic['星级'] = i.find('span',class_="total_star").find('span')['style'].split(':')[1]
#     datai.append(dic)
#         # 分别获取字段内容
# print(datai[:2])
u1='http://www.snh48.com/member_list.html'
r=requests.get(u1)
r.encoding='utf-8'
soup=BeautifulSoup(r.text, 'lxml')

kuai=soup.find_all('div',class_='member_h zx5')
urllist=[]
for i in kuai:
    tmp=i.find('div',class_='zx_def_s').text
    print(tmp)
    urllist.append(tmp)
print(urllist)



   