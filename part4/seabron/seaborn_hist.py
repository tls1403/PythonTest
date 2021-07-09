import seaborn as sns
import matplotlib.pyplot as plt

plt.rc("font",family = "Malgun Gothic")
sns.set(font = "Malgun Gothic",
        rc = {"axes.unicode_minus":False},
        style = "darkgrid")


plt.style.use('seaborn-poster')
plt.rcParams['axes.unicode_minus'] = False

titanic = sns.load_dataset('titanic')

#스타일 테마 설정(darkgrid, whitegrid, dark, whitem ticks 중에)
# sns.set_style('darkgrid')

fig = plt.figure(figsize=(15,5))
ax1 = fig.add_subplot(1,3,1)
ax2 = fig.add_subplot(1,3,2)
ax3 = fig.add_subplot(1,3,3)

#displot
sns.distplot(titanic['fare'],ax = ax1)

#kdeplot
sns.kdeplot(x = 'fare',data = titanic, ax = ax2)

#histplo
sns.histplot(x = 'fare',data= titanic,ax = ax3)

#차트제목표시

ax1.set_title('titanic fare - hist/ked')
ax2.set_title('titanic fare - kde')
ax3.set_title('titanic fare - hist')

plt.show()
