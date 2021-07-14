import pandas as pd
import numpy as np
df = pd.read_csv('D:/5674-833_4th/part5/auto-mpg.csv')

df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'accerleration','model_year','origin','name']


mpg_to_kpl = 1.630934/3.78541

df['kpl'] = df['mpg']*mpg_to_kpl #mpg값을 kpl로 변환해서 변수 kpl 에 저장
df['kpl'] = df['kpl'].round(2) #소수점 두번째자리까지
# print(df.head(3))

# print(df['horsepower'].unique())

df['horsepower'].replace('?',np.nan,inplace=True)
df.dropna(subset=['horsepower'],axis=0,inplace=True)
df['horsepower'] = df['horsepower'].astype('float')

# print(df['horsepower'].dtypes)

# print(df['origin'].unique())

df['origin'].replace({1:'USA',2:"EU",3:'JPN'},inplace=True)

# print(df['origin'].unique())
# print(df['origin'].dtypes)

df['origin'] = df['origin'].astype('category')
# print(df['origin'].dtypes)
#
# print(df['model_year'].sample())


#np.histogram 함수로 3개의 bin으로 구분할 경계값의 리스트 구하기
count,bin_dividers = np.histogram(df['horsepower'],bins=3) #count = 각 구간에 속하는 값의 개수, bin_dividers = 경계값 리스트
# print(bin_dividers)

#3개의 bin에 이름저장
bin_names =['저출력','보통출력','고출력']

#pd.cut 함수로 각 데이터를 3개의 bin에 할당

df['hp_bin'] = pd.cut(x = df['horsepower'], #데이터배열
                      bins = bin_dividers, #경계값 리스트
                      labels= bin_names, #bin 이름
                      include_lowest= True) #첫경계값 포함

#horsepower,hp_bin 출력
print(df[['horsepower','hp_bin']].head(10))