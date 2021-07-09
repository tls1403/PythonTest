import folium
import pandas as pd

#대학교 리스트를 데이터 프레임으로 변환
df = pd.read_excel('D:/5674-833_4th/part4/서울지역 대학교 위치.xlsx',engine= 'openpyxl')


#서울 지도 만들기
seoul_map = folium.Map(location=[37.55,126.98], tiles= 'Stamen Terrain',
                       zoom_start= 12)
df.set_index('학교',inplace = True)


#대학교 위치 정보를 Marker로 표시
for name,lat,lng in zip(df.index,df.위도,df.경도):
    folium.CircleMarker([lat,lng],
                  radius = 10,  #원의 반지름
                  color = 'brown', #원의 둘레 색상
                  fill = True,
                  fill_color = 'coral', #원을 채우는 색
                  fill_opacity = 0.7, #투명도
                  popup= name
                  ).add_to(seoul_map)

seoul_map.save('D:/seoul_colleges2.html')



