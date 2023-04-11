import pandas as pd
import matplotlib.pyplot as plt


house_data = pd.read_csv('/Users/soyoung/git/playdata/titanic/house_price.csv')
data = pd.DataFrame(house_data)
data.dropna(axis=0,inplace=True)


def area_dis(str):
    if str == '전용면적 60㎡이하':
        return 0
    elif str == '전용면적 60㎡초과 85㎡이하':
        return 1
    elif str == '전용면적 85㎡초과 102㎡이하':
        return 2
    else:
        return 3

# 면적별 데이터
data['area']= data['규모구분'].apply(area_dis)
data['분양가격'] = data['분양가격(㎡)'].values[:]

area0 = data[data['2015'] & data['area']==0]

plt.scatter(area0['연도'],area0["분양가격"])
plt.show()