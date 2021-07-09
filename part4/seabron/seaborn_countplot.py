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

#기본값
sns.countplot(x = 'class',palette = 'Set1',data = titanic, ax =ax1)

#hue 옵션에 who 추가
sns.countplot(x = 'class',hue = 'who',palette = 'Set2',data= titanic, ax = ax2)

#dodge = False 옵션 추가 (축 방향으로 분리하지 않고 누적 그래프 출력)
sns.countplot(x = 'class',hue = 'who',palette = 'Set3',data= titanic, dodge = False,ax = ax3)

ax1.set_title('titanic class')
ax2.set_title('titanic class - who')
ax3.set_title('titanic class - who(stacked)')

plt.show()
