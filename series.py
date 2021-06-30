import pandas as pd

dict_data = {'a':1, 'b':2, 'c':3}

#판다스 Series 함수로 dictionary를 Series로 변환
sr = pd.Series(dict_data)

#sr의 자료형 출력
# print(type(sr))
# print('\n')
#
# print(sr)


#리스트를 시리즈로 변환하여 변수 sr에 저장
# list_data = ['2019-01-02',3.14,'ABC',100,True]
# sr = pd.Series(list_data)
# # print(sr)
#
# idx =sr.index
# val = sr.values
#
# print(idx)
# print('\n')
# print(val)

#튜플을 시리즈로 변환(인덱스 옵션 저장)
tup_data = ('영인','2010-0501','여',True)

sr = pd.Series(tup_data,index=['이름','생년월일','성별','학생여부'])
# print(sr)
# print(sr[0])
# print(sr['이름'])

#여러 개의 원소를 선택(인덱스 리스트 활용)
# print(sr[[1,2]])
# print('\n')
# print(sr[['생년월일','성별']])

#여러 개의 원소를 선택(인덱스 범위 사용)

print(sr[1:2])
print('\n')
print(sr['생년월일':'성별'])
