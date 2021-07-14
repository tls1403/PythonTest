import pandas as pd

df = pd.read_csv('D:/5674-833_4th/part5/stock-data.csv')

df['new_Date'] = pd.to_datetime(df['Date']) #df에 새로운 new_Date 라는 열 추가


#시계열 값으로 변환된 열을 새로운 행 인덱스로 지정, 기존 날짜 열은 삭제
df.set_index('new_Date',inplace=True)
df.drop('Date',axis = 1,inplace = True)





