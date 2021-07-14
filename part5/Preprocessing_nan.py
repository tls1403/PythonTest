import seaborn as sns

df= sns.load_dataset('titanic')

missing_df = df.isnull()
# print(df.head().isnull().sum(axis=0))
# print(missing_df.columns)
# for col in missing_df.columns:
#     missing_count = missing_df[col].value_counts()
#     try:
#         print(col,":",missing_count[True])
#     except:
#         print(col,':',0)

# df_thresh = df.dropna(axis=1,thresh= 500) #NaN 값이 500개 이상인 열을 모두 삭제
# print(df_thresh.columns)

# df_age = df.dropna(subset=['age'],how='any',axis=0)
# print(len(df_age))

# print(df['age'].head(10))
# print('\n')
# age 열의 nan 값을 다른 나이 데이터의 평균으로 변경하기
mean_age = df['age'].mean(axis = 0) #age 열의 평균 계산
df['age'].fillna(mean_age,inplace=True)
#
# print(df['age'].head(6))
#
# print(df['embark_town'][825:830])
#
# #embark_town 열의 nan 값을 승선도시 중에서 가장 많이 출현한값으로 치환하기
# most_freq = df['embark_town'].value_counts(dropna=True).idxmax() #idxmax는 가장큰값을 갖는 열 반환
# print(most_freq)
# print('\n')
#
# df['embark_town'].fillna(most_freq,inplace=True)
#
# print(df['embark_town'][825:830])

print(df['embark_town'][825:830])
print('\n')

df['embark_town'].fillna(method='ffill',inplace=True)
print(df['embark_town'][825:830])

