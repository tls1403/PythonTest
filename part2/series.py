import pandas as pd

dict_data = {'a':1, 'b':2, 'c':3}

#판다스 Series 함수로 dictionary를 Series로 변환
sr = pd.Series(dict_data)

#sr의 자료형 출력
print(type(sr))
# print('\n')
#
# print(sr)


#리스트를 시리즈로 변환하여 변수 sr에 저장
list_data = ['2019-01-02',3.14,'ABC',100,True]
sr = pd.Series(list_data)
print(sr)

idx =sr.index
val = sr.values

print(idx)
print('\n')
print(val)

#튜플을 시리즈로 변환(인덱스 옵션 저장)
tup_data = ('영인','2010-0501','여',True)

sr = pd.Series(tup_data,index=['이름','생년월일','성별','학생여부'])
print(sr)

print(sr[0])
print(sr['이름'])

#여러 개의 원소를 선택(인덱스 리스트 활용)
print(sr[[1,2]])
print('\n')
print(sr[['생년월일','성별']])

#여러 개의 원소를 선택(인덱스 범위 사용)

print(sr[1:2])
print('\n')
print(sr['생년월일':'성별'])

#데이터 프레임 만들기 딕셔너리 -> 데이터 프레임

#열 이름을 key로 하고, 리스트를 value로 갖는 딕셔너리 정의(2차원 배열)
#
dict_data = {'c0':[1,2,3],'c1':[4,5,6,],'c2':[7,8,9],'c3':[10,11,12],'c4':[13,14,15]}

#판다스 DataFrame 함수로 딕셔너리를 데이터프레임으로 변환
df = pd.DataFrame(dict_data)

#df 의 자료형출력
print(type(df))
print('\n')
print(df)

#
#행 인덱스/열 이름 지정하여 데이터프레임만들기
df = pd.DataFrame([[15,'남','덕영중'],[17,'여','수리중']],
                  index =['준서','예은'],
                  columns=['나이','성별','학교'])

#행 인덱스 , 열 이름 확인하기
print(df)
print('\n')
print(df.index)
print('\n')
print(df.columns)


df.index = ['학생1','학생2']
df.columns = ['연령','남녀','소속']

print(df)
print('\n')
print(df.index)
print('\n')
print(df.columns)

print(df)
print('\n')

#열 이름중 나이-> 연령  성별 -> 남녀  학교->소속 으로
df.rename(columns={'나이':'연령','성별':'남녀','학교':'소속'},inplace=True)

#df의 행 인덱스 중에서 '준서'를 '학생1'로 '예은'을 '학생2'로 바꾸기
df.rename(index= {'준서':'학생1','예은':'학생2'},inplace=True)

# print(df)

exam_data = {'수학':[90,80,70],'영어':[98,89,95],'음악':[85,95,100],'체육':[100,90,90]}

df = pd.DataFrame(exam_data,index=['서준','우현','인아'])

print(df)

print('\n')

# #df2에 df를 복사
df2 = df[:]
df2.drop('우현',inplace=True)
print(df2)
print('\n')

# #df3에 df를 복사하고 2개 행 제거
df3 = df[:]
df3.drop(['우현','인아'],axis=0,inplace=True)
print(df3)

#데이터프레임 df를 복제하여 변수 df4에 저장 df4의 1개의 열 삭제
df4 = df.copy()
df4.drop('수학',axis=1,inplace=True)
print(df4)
print('\n')

#데이터프레임 df를 복제하여 변수 df5에 저장 df5의 2개의 열 삭제
df5 = df.copy()
df5.drop(['영어','음악'],axis = 1,inplace = True)
print(df5)


