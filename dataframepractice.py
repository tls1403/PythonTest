import pandas as pd

# exam_data = {'수학':[90,80,70],'영어':[98,89,95],'음악':[85,95,100],'체육':[100,90,90]}
# df = pd.DataFrame(exam_data,index=['서준','우현','인아'])
# print(df)
# print('\n')

#행 인덱스를 사용하여 행 1개 선택

# labell = df.loc['서준'] #서준행 선택
# positionl = df.iloc[0] #0번째 행 선택
# print(labell)
# # print('\n')
# print(positionl)

# label2 = df.loc[['서준','우현']]
# position2 = df.iloc[[0,1]]
# print(label2)
# print('\n')
# print(position2)

exam_data = { '이름' : ['서준','우현','인이'],
              '수학' : ['90','80','70'],
              '영어' : ['98','89','95'],
              '음악' : ['85','95','100'],
              '체육' : ['100','90','90']
}

df = pd.DataFrame(exam_data)

print(df)
print('\n')
#
# #수학 열 만 선택
#
# math1 = df['수학']
# print(type(math1))
# print(math1)
# print('\n')
#
# #영어 열 선택
# english = df['영어']
# print(type(english))
# print(english)
# print('\n')
# #수학 열 데이터프레임
# math2 = df[['수학']]
# print(type(math2))
# print(math2)

# 음악 체육 점수 데이터를 선택
# music_gym = df[['음악','체육']]
# print(type(music_gym))
# print(music_gym)
# print('\n')

df.set_index('이름',inplace=True)

# c = df.loc['서준',['음악','체육']]
# print(c)
# d = df.iloc[0,[2,3]]
# print(d)
# e = df.loc['서준','음악':'체육']
# print(e)
#
# f = df.iloc[0,2:4]
# print(f)

g = df.loc[['서준','우현'],['음악','체육']]
print(g)