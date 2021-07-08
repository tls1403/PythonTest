import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('default')

df = pd.read_csv('D:/5674-833_4th/part4/auto-mpg.csv',header= None)

#열이름지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleraiton','model_year','origin','name']

#데이터 개수 카운트를 위해 값 1을 가진 열 추가
df['count'] = 1
df_origin = df.groupby('origin').sum() #origin 열을 기준으로 그룹화 ,합계 연산
print(df_origin)

#제조국가 값을 실제 지역명으로 변경
df_origin.index = ['USA',"EU",'JPN']

# 제조국가 열에 대한 파이 차트 그리기 -count열데이터 사용

df_origin['count'].plot(kind = 'pie',
                        figsize = (7,5),
                        autopct = '%1.1f%%', #퍼센트 %표시
                        startangle = 10, #파이조각을 나누는 시작점( 각도표시)
                        colors = ['chocolate','bisque','cadetblue']
                        )

plt.title('Model Origin',size =10)
plt.axis('equal') #axis() 함수는 x,y축의 범위를 설정할수있게 하는것과 동시에 여러 옵션을 설정할수있는 함수이다. eqaul = 각 축의 범위와 축의 스케일을 동일하게 설정한다.
plt.legend(labels = df_origin.index,loc = 'upper right')
plt.show()