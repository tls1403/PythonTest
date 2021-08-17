import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#[데이터가져오기]

df = pd.read_csv('D:/5674-833_4th/part7/auto-mpg.csv',header=None)

#열이름저장
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

#데이터 살펴보기
# print(df.head())
# print(df.info())

#출력할 열의 개수 한도 늘리기
pd.set_option('display.max_columns',10)
# print(df.head())

#데이터 요약 정보확인
# print(df.describe())

# print(df['horsepower'].unique())

df['horsepower'].replace('?',np.nan,inplace=True) #?를 np.nan으로 변경
df.dropna(subset=['horsepower'],axis=0,inplace=True) #누락데이터 행 삭제
df['horsepower'] = df['horsepower'].astype('float')

# print(df.describe())

#분석에 활용할 열(속성) 선택(연비 실린더 출력 중량)
ndf = df[['mpg','cylinders','horsepower','weight']]
# print(ndf.head())

#연비(mpg)와 다른 변수간의 선형 관계를 그래프로 확인

ndf.plot(kind = 'scatter',x='weight',y='mpg',c='coral',s=10,figsize=(10,5))
# plt.show()

fig = plt.figure(figsize=(10,5)) #그래프 사이즈 설정
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
sns.regplot(x = 'weight', y = 'mpg', data = ndf, ax = ax1)
sns.regplot(x = 'weight', y = 'mpg', data = ndf,ax = ax2, fit_reg = False)

#seaborn 조인트 그래프 - 산점도, 히스토그램
sns.jointplot(x = 'weight',y= 'mpg',data = ndf)
sns.jointplot(x = 'weight', y = 'mpg',kind = 'reg',data = ndf)

#pairplot 함수를 이용하여 두 속성에서 짝을 지을수 있는 모든 경우의 수에 대하여 산점도를 그린다.
grid_ndf = sns.pairplot(ndf)

#훈련/검증 데이터 분할
X = ndf[['weight']]
Y = ndf['mpg']

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X, #독립변수(입력값이나 원인)
                                                 Y, #종속변수(결과물 이나 효과)
                                                 test_size=0.3, #검증 30$
                                                 random_state=10
                                                 )
print('train data 개수',len(X_train))
print('test data 개수',len(X_test))


# 모형 학습 및 검증

#sklearn 라이브러리에서 선형회귀분석 모듈 가져오기
from sklearn.linear_model import LinearRegression

# 단순회귀분석 모형 객체 생성
lr = LinearRegression()
#train data를 가지고 모형학습
lr.fit(X_train,Y_train)

r_squre = lr.score(X_test,Y_test)
# print(r_squre)

#회귀식 기울기
print('기울기 a:',lr.coef_)
print('\n')

#회귀식의 y절편
print('y절편 b',lr.intercept_)

#모형에 전체 x데이터를 입력하여 예측한 값 y_hat을 실제 값 y와 비교
y_hat = lr.predict(X)

plt.figure(figsize=(10,5))
ax1 = sns.kdeplot(Y,label='y')
ax2 = sns.kdeplot(y_hat,label='y_hat',ax=ax1)
plt.legend()
plt.show()
