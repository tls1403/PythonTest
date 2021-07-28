import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns',10) #출력할 최대 열의 개수
pd.set_option('display.max_colwidth',20) #출력할 열의 너비

titanic = sns.load_dataset('titanic')

df = titanic.loc[:,['age','sex','class','fare','survived']]


pdf = pd.pivot_table(df,             #피벗할 데이터 프레임
                     index = 'class', # 행 위치에 들어갈 열
                     columns= 'sex', # 열 위치에 들어갈 열
                     values='age', # 데이터로 사용할 열
                     aggfunc='mean') # 데이터 집계함수

# print(pdf.head())

pdf2 = pd.pivot_table(df,
                      index= 'class',
                      columns= 'sex',
                      values= 'survived',
                      aggfunc=['mean','sum'])
# print(pdf2.head())

pdf3 = pd.pivot_table(df,                    #피벗할 데이터프레임
                      index = ['class','sex'], #행 위치에 들어갈 열
                      columns= 'survived',  # 열 위치에 들어갈 열
                      values= ['age','fare'], # 데이터로 사용할 열
                      aggfunc=['mean','max']) #데이터 집계함수

# print(pdf3.head(),'\n')
#
# print(pdf3.xs('First')) #행 인덱스가 First 인것을 선택

print(pdf3.xs(('First','female'))) #행 인덱스가 ('First','female')인 행을 선택

print(pdf3.xs('male',level='sex')) #행 인덱스의 sex 레벨이 male인 행을 선택

print(pdf3.xs(('Second','male'),level=['class','sex'])) #Second, male 인 행을 선택

print(pdf.xs('mean',axis=1)) #열 인덱스가 mean인 데이터를 선택

print(pdf3.xs(1,level='survived',axis=1)) #survived 레벨이 1인 데이터 선택

