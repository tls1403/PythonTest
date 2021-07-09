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

col_years = list(map(str,range(2010,2018)))
df_4 = df_seoul.loc[['충청남도','경상북도','강원도','전라남도'],col_years]
df_4['합계'] = df_4.sum(axis = 1) #합계변수 추가
df_total = df_4[['합계']].sort_values(by='합계',ascending= True) #df_4['합계'] 는 datatype이 Series 이고 df_4[['합계']] 는 datatype 이 dataFrame 이다.
#스타일 서식 지정
plt.style.use('ggplot')
#수평막대그래프 그리기
df_total.plot(kind = 'barh',color='cornflowerblue',width =0.5,figsize = (10,5))

plt.title('서울 -> 타시도 인구이동')
plt.ylabel('전입지')
plt.xlabel('이동 인구수')
plt.show()
