import pandas as pd

df = pd.read_excel('D:/5674-833_4th/part6/주가데이터.xlsx',engine= 'openpyxl')
#
# print(df.head(),'\n')
# print(df.dtypes,'\n')

#연월일 데이터 분리하기
df['연월일'] = df['연월일'].astype('str')
dates = df['연월일'].str.split('-')
print(dates.head())

#분리된 정보를 각각 새로운 열에 담아 df에 추가한다.
df['연']= dates.str.get(0)
df['월'] = dates.str.get(1)
df['일'] = dates.str.get(2)

print(df.head())