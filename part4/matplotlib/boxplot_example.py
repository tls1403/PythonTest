import pandas as pd
import matplotlib.pyplot as plt

#matplotlib 한글 폰트 오류해결
from IPython.core.pylabtools import figsize
from matplotlib import font_manager,rc
font_path = "D:/5674-833_4th/part4/malgun.ttf"
font_name = font_manager.FontProperties(fname= font_path).get_name()
rc('font',family = font_name)

plt.style.use('seaborn-poster')
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('D:/5674-833_4th/part4/auto-mpg.csv',header=None)

#열이름지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleraiton','model_year','origin','name']

# 그래프 객체 생성(figure에 2개의 subplot 생성)
fig = plt.figure(figsize=(15,5))
ax1 = fig.add_subplot(1,2,1) #1행 2열 중 1번째
ax2 = fig.add_subplot(1,2,2) #1행 2열 중 2번째

#axe 객체에 boxplot 메소드로 그래프 출력

ax1.boxplot(x = [df[df['origin']== 1]['mpg'],
            df[df['origin'] == 2]['mpg'],
            df[df['origin'] == 3]['mpg']],
            labels = ['USA','EU','JAPAN']

            )
ax2.boxplot(x=[df[df['origin'] == 1]['mpg'],
               df[df['origin'] == 2]['mpg'],
               df[df['origin'] == 3]['mpg']],
            labels=['USA', 'EU', 'JAPAN'],
            vert =False
            )

ax1.set_title('제조국가별 연비 분포(수직 박스 플롯)')
ax2.set_title('제조국가별 연비 분포(수평 박스 플롯)')
plt.show()

