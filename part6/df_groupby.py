import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')

df = titanic.loc[:,['age','sex','class','fare','survived']]
#
# print('승객수:',len(df))
# print(df.head())


grouped = df.groupby(['class'])
print(grouped)

for key,group in grouped:        #key = 나누는기준
    print('*key:',key)
    print('*number',len(group))
    print(group.head())


average = grouped.mean()  # 그룹별 평균
print(average)

group3 = grouped.get_group('Third') #특정 그룹추출
print(group3.head())

grouped_two = df.groupby(['class','sex']) #두개의 column으로 그룹화

for key,group in grouped_two:
    print('*key:', key)
    print('*number', len(group))
    print(group.head())
    print('\n')

average_two = grouped_two.mean()
print(average_two)


group3f = grouped_two.get_group(('Third','female'))
print(group3f.head())

