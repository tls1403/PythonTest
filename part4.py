import pandas as pd
import matplotlib.pyplot as plt
#한글 폰트 오류 제거
from matplotlib import font_manager,rc
font_path ="D:/5674-833_4th/part4/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font',family = font_name)

df = pd.read_excel('D:/5674-833_4th/part4/시도별 전출입 인구수.xlsx',engine = 'openpyxl',header =0)
df = df.fillna(method='ffill') #누락값을 앞 데이터로 채움

#서울에서 다른 지역으로 이동한 데이터만 추출하여 정리
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'],axis= 1) #전출지별 column 삭제
df_seoul.rename({'전입지별':'전입지'},axis=1,inplace=True) #전입지별 column을 전입지로 바꿔줌
df_seoul.set_index('전입지',inplace = True)

#서울에서 경기도로 이동한 인구데이터 값만 선택
sr_one = df_seoul.loc['경기도']



plt.style.use('ggplot') #ggplot 스타일 지정


#그림 사이즈 지정
plt.figure(figsize=(14,5))
#x 축 눈금 라벨 회전하기
plt.xticks(size=10,rotation = 'vertical')

# 제목정함
plt.title('서울 -> 경기 인구 이동')

# 축이름 추가
plt.xlabel('기간')
plt.ylabel('이동인구수')

#x 축 y 축 데이터를 plot 함수에 입력
plt.plot(sr_one.index,sr_one.values,marker = 'o',markersize = 10)

plt.legend(labels=['서울 -> 경기'],loc = 'best')

#y축 범위지정
plt.ylim(50000,800000)

# #주석표시

plt.annotate('',
             xy= (20,620000), # 화살표의 머리부분(끝점)
             xytext=(2,290000), #화살표의 꼬리부분 (시작점)
             xycoords = 'data', #좌표체계
             arrowprops=dict(arrowstyle = '->',color = 'skyblue',lw = 5),)

plt.annotate('',
             xy = (47,450000),
             xytext=(30,580000),
             xycoords='data',
             arrowprops = dict(arrowstyle = '->',color = 'olive',lw =5),)

#주석표시-텍스트

plt.annotate('인구 이동 증가(1970~1995)', #텍스트입력
             xy = (10,550000), #텍스트 위치 기준점
             rotation = 25, #텍스트 회전 각도
             va = 'baseline', #텍스트 상하 정렬
             ha = 'center', #텍스트 좌우 정렬
             fontsize = 15, #텍스트 크기
             )

plt.annotate('인구 이동 감소(1995~2017)',
             xy = (40,560000),
             rotation = 11,
             va = 'baseline',
             ha = 'center',
             fontsize = 15,
             )

plt.show()