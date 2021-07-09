import pandas as pd
import folium
import json

file_path = 'D:/5674-833_4th/part4/경기도인구데이터.xlsx'

df =pd.read_excel(file_path,index_col='구분',engine= 'openpyxl')
#열(2007,2008,,,)을 string 으로 바꿔줌
df.columns = df.columns.map(str)

#경기도 시군구 경계 정보를 가진 geo-json 파일 불러오기
geo_path = 'D:/5674-833_4th/part4/경기도행정구역경계.json'

try:
    geo_data = json.load(open(geo_path,encoding='utf-8'))
except:
    geo_data = json.load(open(geo_path,encoding='utf-8-sig'))

# 경기도 지도 만들기
g_map = folium.Map(location=[37.5502,126.982],
                   tiles='Stamen Terrain',zoom_start=9)

#출력할 연도 선택
year = '2007'

#Choropleth 클래스로 단계구분도 표시하기
folium.Choropleth(geo_data= geo_data,
                  data = df[year],
                  columns=[df.index,df[year]],
                  fill_color='YlOrRd',fill_opacity= 0.7, line_opacity=0.3,
                  threshold_scale= [10000,100000,300000,500000,700000],
                  key_on='feature.properties.name',
                  ).add_to(g_map)

g_map.save('D:/gyonggi_population_'+year+'.html')
