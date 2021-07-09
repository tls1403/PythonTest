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

#그래프 객체 생성(figure에 2개의 서브 플롯 생성)
fig = plt.figure(figsize=(15,5))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

#그래프 그리기(선형
sns.regplot(x = 'age',
            y = 'fare',
            data = titanic,
            ax = ax1).set_title('회귀선 0')

sns.regplot(x = 'age',
            y = 'fare',
            data = titanic,
            ax = ax2,
            color = 'orange',
            fit_reg = False).set_title('회귀선 X')#회귀선 미표시


plt.show()