import pandas as pd

pd.set_option('display.max_columns',10) #출력할 최대 열의 개수
pd.set_option('display.max_colwidth',20) #출력할 열의 너비
pd.set_option('display.unicode.east_asian_width',True) # 유니코드 사용 너비 조정

df1 = pd.read_excel('D:/5674-833_4th/part6/stock price.xlsx',engine='openpyxl')
df2 = pd.read_excel('D:/5674-833_4th/part6/stock valuation.xlsx',engine='openpyxl')

merge_inner = pd.merge(df1,df2,how='outer',on='id')
# print(merge_inner)

merge_left = pd.merge(df1,df2, how='left',left_on='stock_name',right_on='name')
# print(merge_left)

merge_right = pd.merge(df1,df2,how = 'right',left_on='stock_name',right_on='name')
print(merge_right)

price = df1[df1['price']<50000]

value = pd.merge(price,df2)
print(value)