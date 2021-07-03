import pandas as pd
import matplotlib.pyplot as plt

#read_csv() 함수로 df 생성
df = pd.read_csv('D:/5674-833_4th/part3/auto-mpg.csv')

#열이름 지정

df.columns= ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','name']

#데이터프레임 df의 내용을 일부 확인

print(df.head())
print('\n')
print(df.tail())

#df의 모양과 크기 확인
print(df.shape)
#
# #데이터프레임 df의 내용확인
print(df.info())
#
# #데이터프레임 df의 자료형 확인
print(df.dtypes)
print('\n')
# #시리즈(mpg)의 자료형 확인
print(df.mpg.dtypes)

#데이터프레임 df의 기술통계 정보 확인
print(df.describe())
print('\n')
print(df.describe(include='all')) #산술데이터가 아닌 열에 대한 정보를 포함하고 싶을때 include = 'all' 옵션 추가
#
# 각 열이 가지고 있는 원소 개수
print(df.count())
print('\n')
print(type(df.count()))

unique_value = df['origin'].value_counts()
print(unique_value)
print('\n')
print(type(unique_value))


#평균값
print(df.mean())
print('\n')
print(df['mpg'].mean())
print(df.mpg.mean())
print('\n')
print(df[['mpg','weight']].mean())

#중간값
print(df.median())
print('\n')
print(df['mpg'].median())

#최대값
print(df.max())
print('\n')
print(df['mpg'].max())


#최소값
print(df.min())
print('\n')
print(df['mpg'].min())

#표준편차
print(df.std())
print('\n')
print(df['mpg'].std())

#상관계수
print(df.corr())
print('\n')
print(df[['mpg','weight']].corr())

#선그래프

df =pd.read_excel('D:/5674-833_4th/part3/남북한발전전력량.xlsx',engine='openpyxl')
#
df_ns = df.iloc[[0,5],3:]    #남한,북한 발전량 합계 데이터만 추출
df_ns.index = ['South','North']    #행인덱스 변경
df_ns.columns = df_ns.columns.map(int)
print(df_ns.head())
print('\n')
plt.plot(df_ns)
plt.legend(df_ns.index)   #범례표시
plt.show()

#시간에 따라 보여주기 위해 행열 전치하여 다시그리기
tdf_ns = df_ns.T
print(tdf_ns.head())
plt.plot(tdf_ns)
plt.legend(tdf_ns.columns)
plt.show()

plt.bar(tdf_ns.columns)
plt.xticks()
plt.show()