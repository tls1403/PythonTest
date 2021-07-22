import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age','fare']]
df['ten'] = 10

def add_10(n):
    return n+10

def add_two_obj(a,b):
    return a+b

#시리즈 변수에 적용
# print(df['age'].head())
# print('\n')
sr1 = df['age'].apply(add_10) #모든행에 add_10 함수 적용
# print(sr1.head())
# print('\n')

sr2 = df['age'].apply(add_two_obj,b = 10) #모든행에 add_two_obj('age',10)
# print(sr2.head())
# print('\n')

#lambda 함수 활용: 시리즈 객체에 적용
sr3 = df['age'].apply(lambda x: add_10(x)) # x = df['age']
# print(sr3.head())



#데이터프레임에 적용

#데이터프레임에 add_10() 함수를 매핑 적용
df_map = df.applymap(add_10)
# print(df_map.head())


#시리즈객체에 함수 매핑
#데이터 프레임의 각 열에 함수 매핑

def missing_value(series): #시리즈를 인자로 전달
    return series.isnull()

result = df.apply(missing_value,axis =0) #각 열 age, fare 을 매핑함수에 전달하고 각 열의 리턴값은 시리즈 형태로 반환된다. 시리즈가 합쳐져서 데이터프레임이된다.
# print(result.head())

def min_max(x):    #최대값 - 최소값
    return x.max() - x.min()

result1 =df.apply(min_max) #기본값 axis = 0
# print(result1)

def add_two_obj(a,b):
    return a + b
# x = df , a = df['age'] , b = df['ten']
df['add'] = df.apply(lambda x : add_two_obj(x['age'],x['ten']),axis = 1)
# print(df.head())

#각 열의 NaN 찾기 = 데이터프레임 반환
def missing_value(x):
    return x.isnull()

#각 열의 NaN 개수 반환 = 시리즈 반환
def missing_count(x):
    return missing_value(x).sum()

# 데이터프레임의 총 NaN 개수 - 데이터프레임을 전달하면 값 반환
def total_number_missing(x):
    return missing_count(x).sum()

df.drop(['ten','add'],inplace= True,axis = 1)
result_df = df.pipe(missing_value)

result_series = df.pipe(missing_count)
# print(result_series)

result_value = df.pipe(total_number_missing)
print(result_value)