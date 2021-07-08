import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('classic')

df = pd.read_csv('D:/5674-833_4th/part4/auto-mpg.csv',header=None)

#열이름 지정
df.columns = ['mpg','cylinder','displacement','horsepower','weight',
              'acceleration','model year','origin','name']
df['mpg'].plot(kind = 'hist',bins =10, color = 'coral',figsize =(10,5))

plt.title('histogram')
plt.xlabel('mpg')
plt.show()
