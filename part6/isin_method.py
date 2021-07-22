import seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')

#출력할 최대 열의 개수
pd.set_option('display.max_columns',10)

#함께 탑승한 형제 또는 배우자의 수가 3,4,5인 승객만 따로 추출
mask3 = titanic['sibsp'] == 3
mask4 = titanic['sibsp'] == 4
mask5 = titanic['sibsp'] == 5

df_boolean = titanic[mask3 | mask4 | mask5]
# print(df_boolean.head())

#isin() 메소드 활용
isin_filter = titanic['sibsp'].isin([3,4,5])
df_isin = titanic[isin_filter]
print(df_isin.head())