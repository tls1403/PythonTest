import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

#스타일 테마 설정
sns.set_style('whitegrid')

#그래프 객체 생성
fig = plt.figure(figsize=(15,5))
ax1 = fig.add_subplot(1,3,1)
ax2 = fig.add_subplot(1,3,2)
ax3 = fig.add_subplot(1,3,3)

#x축 y축에 변수 할당
sns.barplot(x = 'sex',y = 'age', data = titanic ,ax =ax1)

# x축 y축에 변수 할당하고 hue 옵션을 추가한다
#hue 여러열에서 집단묶어서 세부 집단 시각화
sns.barplot(x = 'sex', y = 'age', data = titanic, hue = 'class',ax = ax2)

# x축 y축에 변수 할당하고 hue옵션을 추가하여 누적출력
sns.barplot(x = 'sex', y = 'age', data = titanic , hue = 'class', dodge = False ,ax = ax3)

ax1.set_title('titanic survived - sex')
ax2.set_title('titanic survived - sex/class')
ax3.set_title('titanic survived - sex/class(stacked)')

plt.show()