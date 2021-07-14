import pandas as pd

df = pd.DataFrame( {'c1':['a','a','b','a','b'],
                    'c2':[1,1,1,2,2],
                    'c3':[1,1,2,2,2]})
# df_dup = df.duplicated()
# print(df_dup)
#
# col_dup = df['c2'].duplicated()
# print(col_dup)
df2 = df.drop_duplicates() #전체 행에 대해 중복제거(전체중복)
df3 = df.drop_duplicates(subset=['c2','c3']) # c2,c3열의 중복 제거
print(df3)