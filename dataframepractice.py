import pandas as pd

exam_data = {'수학':[90,80,70],'영어':[98,89,95],'음악':[85,95,100],'체육':[100,90,90]}
df = pd.DataFrame(exam_data,index=['서준','우현','인아'])
# print(df)
# print('\n')

#행 인덱스를 사용하여 행 1개 선택

labell = df.loc['서준'] #서준행 선택
positionl = df.iloc[0] #0번째 행 선택
# print(labell)
# # print('\n')
# print(positionl)

label2 = df.loc[['서준','우현']]
position2 = df.iloc[[0,1]]
print(label2)
print('\n')
print(position2)
#열선택부터 다음시간에