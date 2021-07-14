import pandas as pd
import numpy as np

df = pd.read_csv('D:/5674-833_4th/part5/auto-mpg.csv')

df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

df['horsepower'].replace('?',np.nan,inplace=True)
df.dropna(subset = ['horsepower'],axis =0,inplace = True)
df['horsepower'] = df['horsepower'].astype('float')

#horsepower 열의 통계 요약정보로 최대값 확인
# print(df['horsepower'].describe()) #max 값 230
# print('\n')

#horsepower 열의 최대값의 절대값으로 모든 데이터를 나눠서 저장
# df.horsepower = df.horsepower/abs(df.horsepower.max())

# print(df.horsepower.head())
#
# print('\n')
#
# print(df.horsepower.describe())

print(df.horsepower.describe()) #최대값 230 최소값 46
print('\n')

#horsepower 열에서 최소값을 뺀것을 분모로
min_x = df.horsepower - df.horsepower.min()
#최대값에서 최소값을 뺀것을 분자로
min_max = df.horsepower.max() - df.horsepower.min()
df.horsepower = min_x/min_max

print(df.horsepower.head())



