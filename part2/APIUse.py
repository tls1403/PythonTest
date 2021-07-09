## google 지오코딩 API 를 통해 , 위도 경도 데이터 가져오기

import googlemaps
import pandas as pd


my_key = "AIzaSyA87_UWoXDkWL1c3TvAQAWDsmIVBDMd8i8"

#구글맵스 객체 생성하기


maps = googlemaps.Client(key= my_key)

lat = [] #위도
lng = [] #경도

#장소( 또는 주소) 리스트
places = ["창원대학교","정우상가","해운대해수욕장"]

i = 0

for place in places:
    i = i+1
    try:
        print(i,place)
        #지오코딩 API 결과값 호출하여 geo_location 변수에 저장
        geo_location = maps.geocode(place)[0].get('geometry')
        lat.append(geo_location['location']['lat'])
        lng.append(geo_location['location']['lng'])
    except:
        lat.append('')
        lng.append('')
        print(i)
#데이터 프래임으로 변경

df = pd.DataFrame({'위도':lat,'경도':lng},index=places)
print(df)