import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')

sns.set_style('whitegrid')

#그래프 객체 생성
fig = plt.figure(figsize=(15,10))
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

#박스플롯
sns.boxplot(x = 'alive', y = 'age', data = titanic, ax = ax1)

#박스플롯 그래프 -hue 변수추가
sns.boxplot(x = 'alive',y = 'age',hue = 'sex', data = titanic, ax =ax2)

#바이올린 그래프
sns.violinplot(x = 'alive', y= 'age',data = titanic, ax = ax3)

#바이올린 그래프 - hue 변수추가
sns.violinplot(x = 'alive', y = 'age',hue = 'sex', data = titanic , ax = ax4)

plt.show()