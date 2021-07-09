import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('default')

df =pd.read_csv('D:/5674-833_4th/part4/auto-mpg.csv',header = None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleraiton','model_year','origin','name']

print(df['cylinders'])


df.plot(kind = 'scatter',x = 'weight',y = 'mpg', c= 'coral',s = 10,figsize = (10,5))
plt.title('Scatter Plot - mpg vs wieght')
plt.show()