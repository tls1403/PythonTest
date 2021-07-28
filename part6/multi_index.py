import seaborn as sns

titanic = sns.load_dataset('titanic')

df = titanic.loc[:,['age','sex','class','fare','survived']]

grouped = df.groupby(['class','sex'])

gdf = grouped.mean()
print(gdf)
print(gdf.loc['First'],'\n') #class가 First인것만
print(gdf.loc[('First','female')],'\n')  # class가 First이고 성별이 female인것
print(gdf.xs('male',level='sex')) #성별이 male 인것만
