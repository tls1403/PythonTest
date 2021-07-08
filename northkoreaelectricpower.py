import pandas as pd
import matplotlib.pyplot as plt

#matplotlib 한글 폰트 오류해결
from IPython.core.pylabtools import figsize
from matplotlib import font_manager,rc
font_path = "D:/5674-833_4th/part4/malgun.ttf"
font_name = font_manager.FontProperties(fname= font_path).get_name()
rc('font',family = font_name)

plt.style.use('ggplot')
plt.rcParams['axes.unicode_minus'] = False #마이너스 깨짐 방지

#Excel 데이터를 데이터 프레임으로 변환
df = pd.read_excel("D:/5674-833_4th/part4/남북한발전전력량.xlsx",engine = 'openpyxl',convert_float= True)


df = df.loc[5:9]

df.drop('전력량 (억㎾h)',axis = 'columns',inplace = True)
df.set_index('발전 전력별',inplace = True)

df = df.T
print(df)
print('\n')

#증강률(변동률 계산)

df = df.rename(columns={'합계':'총발전량'})
print(df)
df['총발전량 - 1년'] = df['총발전량'].shift(1)
df['증감률'] = ((df['총발전량']/df['총발전량 - 1년'])-1) * 100

# 2축 그래프 그리기
ax1 = df[['수력','화력']].plot(figsize= (20,10),kind = 'bar' ,width = 0.7, stacked = True)
ax2 = ax1.twinx()
ax2.plot(df.index,df.증감률,ls = '--',marker = 'o',markersize =20, #ls = '--' 는 점선으로 그려라
         color ='red',label = '전년대비 증감률(%)')

ax1.set_ylim(0,500)
ax2.set_ylim(-50,50)

ax1.set_xlabel('연도',size =20)
ax1.set_ylabel('발전량 (억 KWh)')
ax2.set_ylabel('전년 대비 증감률(%)')
plt.title('북한 전력 발전량(1990~2016)',size =30)
ax1.legend(loc = 'upper left')

plt.show()

