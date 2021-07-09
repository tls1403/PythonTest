import seaborn as sns
import matplotlib.pyplot as plt

plt.rc("font",family = "Malgun Gothic")
sns.set(font = "Malgun Gothic",
        rc = {"axes.unicode_minus":False},
        style = "darkgrid")

plt.rcParams['axes.unicode_minus'] = False

titanic = sns.load_dataset('titanic')

table = titanic.pivot_table(index=['sex'],columns=['class'],aggfunc='size')  #aggfunc = 'size' 옵션은 데이터 값의 크기를 기준으로 집계한다는 뜻이다.

#히트맵 그리기
sns.heatmap(table, #데이터프래임
            annot = True, fmt = 'd', #데이터 값 표시여부, 정수형 포맷
            cmap = 'YlGnBu', #컬러 맵
            linewidth = 5, #구분선
            cbar= True) #컬러바 표시여부

plt.show()