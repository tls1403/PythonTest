import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[0:4,'survived':'age']

columns = list(df.columns.values) #컬럼 다 추출
# print(columns)

columns_sorted = sorted(columns) #컬럼리스트 정렬 알파벳순
df_sorted = df[columns_sorted] #정렬된 리스트로 데이터프레임 정렬
# print(df_sorted)

columns_reversed = list(reversed(columns)) #원래 열순서의 역순으로 정렬
df_reversed = df[columns_reversed]
# print(df_reversed)

columns_customed = ['pclass','sex','age','survived'] #열 순서를 원하는데로 바꿀수있다.
df_customed  = df[columns_customed]
print(df_customed)

