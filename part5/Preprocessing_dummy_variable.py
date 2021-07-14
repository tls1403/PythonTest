import pandas as pd
import numpy as np

df = pd.read_csv('D:/5674-833_4th/part5/auto-mpg.csv')

df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

df['horsepower'].replace('?',np.nan,inplace=True)
df.dropna(subset = ['horsepower'],axis =0,inplace = True)
df['horsepower'] = df['horsepower'].astype('float')

count,bin_dividers = np.histogram(df['horsepower'], bins=3)

bin_names = ['저출력','보통출력','고출력']

df['hp_bin'] = pd.cut(x =df['horsepower'],
                      bins= bin_dividers,
                      labels= bin_names,
                      include_lowest= True)

horsepower_dummies = pd.get_dummies(df['hp_bin'])
# print(horsepower_dummies.head(5))

#one_hot_encoding
from sklearn import preprocessing

#전처리를 위한 encoder 객체 만들기

label_encoder = preprocessing.LabelEncoder() #label encoder 생성
onehot_encoder = preprocessing.OneHotEncoder() #one hot encoder 생성

#label encoder로 문자열 범주를 숫자형 범주로 변환
onehot_labeled = label_encoder.fit_transform(df['hp_bin'].head(15))
print(onehot_labeled)
print(type(onehot_labeled) )

#2차원 행렬로 변경
onehot_reshaped = onehot_labeled.reshape(len(onehot_labeled),1)
print(onehot_reshaped)
print(type(onehot_reshaped))

#희소행렬
onehot_fitted = onehot_encoder.fit_transform(onehot_reshaped)
print(onehot_fitted)
print(type(onehot_fitted))



