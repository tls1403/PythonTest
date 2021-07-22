import seaborn as sns

titanic = sns.load_dataset('titanic')

mask1 = (titanic.age >= 10) & (titanic['age'] <20)
df_teenager = titanic.loc[mask1,:]
# print(df_teenager.head())

mask2 = (titanic.age<10) & (titanic.sex == 'female')
df_female_under10 = titanic.loc[mask2,:]
# print(df_female_under10.head())

