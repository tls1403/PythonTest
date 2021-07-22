import pandas as pd

pd.set_option('display.max_columns',10) #출력할 최대 열의 개수
pd.set_option('display.max_colwidth',20) #출력할 열의 너비
pd.set_option('display.unicode.east_asian_width',True) # 유니코드 사용 너비 조정

df1 = pd.read_excel('D:/5674-833_4th/part6/stock price.xlsx',index_col= 'id',engine='openpyxl')
df2 = pd.read_excel('D:/5674-833_4th/part6/stock valuation.xlsx',index_col='id',engine='openpyxl')

df3 = df1.join(df2)
# print(df3)
df4 = df1.join(df2,how='inner')
print(df4)