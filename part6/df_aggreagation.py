import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')

df = titanic.loc[:,['age','sex','class','fare','survived']]

grouped = df.groupby(['class'])


std_all = grouped.std() #표준편차 집계
# print(std_all)

std_fare = grouped['fare'].std()
# print(std_fare)

def min_max(x):
    return x.max() - x.min()

#각 그룹의 최대값과 최소값의 차이를 계산하여 그룹별로 집계
agg_minmax = grouped.agg(min_max) #함수를 그룹객체에 적용
# print(agg_minmax)

agg_all = grouped.agg(['min','max']) #여러함수를 각 열에 동일하게 적용하여 집계
print(agg_all.head(),'\n')

agg_sep = grouped.agg({'fare':['min','max'],'age': 'mean'}) #각 열마다 다른 함수를 적용하여 집계
print(agg_sep.head())