import pandas as pd

df = pd.read_csv('D:/5674-833_4th/part5/stock-data.csv')

#문자열인 날짜 데이터를 판다스 Timestamp로 변환
df['new_date']=pd.to_datetime(df['Date'])

df.set_index('new_date',inplace= True)


# print(df.loc['2018'].head())
# df_ym = df.loc['2018-07']
# print(df_ym)
#

today = pd.to_datetime('2018-12-25')
df['time_delta'] = today - df.index
df.set_index('time_delta',inplace=True)
df_180 = df['180 days':'189 days']
print(df_180)
