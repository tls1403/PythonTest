import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')

df = titanic.loc[:,['age','sex','class','fare','survived']]

grouped = df.groupby(['class'])


std_all = grouped.std() #표준편차 집계
# print(std_all)

std_fare = grouped['fare'].std()
# print(std_fare)

def min_max(x):
    return x.max() - x.min()

#각 그룹의 최대값과 최소값의 차이를 계산하여 그룹별로 집계
agg_minmax = grouped.agg(min_max) #함수를 그룹객체에 적용
# print(agg_minmax)

agg_all = grouped.agg(['min','max']) #여러함수를 각 열에 동일하게 적용하여 집계
# print(agg_all.head(),'\n')

agg_sep = grouped.agg({'fare':['min','max'],'age': 'mean'}) #각 열마다 다른 함수를 적용하여 집계

# print(agg_sep.head())

agg_mean = grouped['age'].mean()
# print(agg_mean)

agg_std = grouped['age'].std()
# print(agg_std)

age_mean = grouped['age'].mean()

age_std = grouped['age'].std()
for key,group in grouped.age:
    group_zscore = (group - age_mean.loc[key])/age_std.loc[key] #zscore 구하는 식
    # print("* origin :",key)
    # print(group_zscore.head(3))


def z_score(x): #zscore 함수
    return (x-x.mean())/x.std()

age_zscore = grouped['age'].transform(z_score)
# print(age_zscore.loc[[1,9,0]])


#필터링

grouped_filter = grouped.filter(lambda x: len(x)>=200) #그룹의 데이터 개수가 200개 이상의 그룹만을 필터링
# print(grouped_filter.head())

age_filter = grouped.filter(lambda x: x.age.mean() <30) #age열의 평균값이 30보다 작은 그룹만을 선택한다.
# print(age_filter.tail())

#그룹객체에 함수 매핑

agg_grouped = grouped.apply(lambda x: x.describe())
print(agg_grouped)

def z_score(x): #zscore 함수
    return (x-x.mean())/x.std()

age_zscore = grouped.age.apply(z_score)
print(age_zscore.head())


for x in age_filter.index:
    if age_filter[x] == True:
        age_filter_df = grouped.get_group(x)
        print(age_filter_df.head())
        print('\n')