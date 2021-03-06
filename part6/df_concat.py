import pandas as pd

#데이터프레임 만들기
df1 = pd.DataFrame({'a': ['a0','a1','a2','a3'],
                    'b':['b0','b1','b2','b3'],
                    'c':['c0','c1','c2','c3'] },
                   index= [0,1,2,3])

df2 = pd.DataFrame( {'a':['a2','a3','a4','a5'],
                     'b':['b2','b3','b4','b5'],
                     'c':['c2','c3','c4','c5']},
                    index=[2,3,4,5])

print(df1.head())
# print('\n')
# print(df2.head())


result1 = pd.concat([df1,df2])
# print(result1,'\n')
result2 = pd.concat([df1,df2], ignore_index= True)
# print(result2)

result3 = pd.concat([df1,df2],axis=1)
# print(result3,'\n')

result3_in = pd.concat([df1,df2],axis=1,join='inner')
# print(result3_in)


sr1 = pd.Series(['e0','e1','e2','e3'], name='e')
sr2 = pd.Series(['f0','f1','f2'],name='f',index=[3,4,5])
sr3 = pd.Series(['g0','g1','g2','g3'],name='g')

result4 = pd.concat([df1,sr1],axis=1)

result5 = pd.concat([df2,sr2],axis=1,sort=True)
print(result5)