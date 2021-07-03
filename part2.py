import pandas as pd

#파일결로
# file_path = 'C:/Users/tls14/Desktop/read_csv_sample.csv'
#
# df1= pd.read_csv(file_path)
# print(df1)
# print('\n')
#
# df2 = pd.read_csv(file_path,header=None)
# print(df2)
# print('\n')
#
# df3 = pd.read_csv(file_path,index_col=None)
# print(df3)
# print('\n')
#
# df4 = pd.read_csv(file_path,index_col= 'c0')
# print(df4)
#

# df1= pd.read_excel('D:/5674-833_4th/part2/남북한발전전력량.xlsx',engine= 'openpyxl')
# df2= pd.read_excel('D:/5674-833_4th/part2/남북한발전전력량.xlsx',engine= 'openpyxl',header=None)
#
# print(df1)
# print('\n')
# print(df2)

# df = pd.read_json('D:/5674-833_4th/part2/read_json_sample.json')
# print(df)
# print('\n')
# print(df.index)

# url = 'D:/5674-833_4th/part2/sample.html'
#
# table = pd.read_html(url)
#
# print(len(table))
# print('\n')
#
# for i in range(len(table)):
#     print("tables[%s]" %i)
#     print(table[i])
#     print('\n')
#
# df = table[1]
# df.set_index(['name'],inplace=True)
# print(df)

#웹스크래핑
from bs4 import BeautifulSoup
import requests
import re

url = "https://en.wikipedia.org/wiki/List_of_American_exchange-traded_funds"
resp = requests.get(url)
soup = BeautifulSoup(resp.text,'lxml')
rows = soup.select('div > ul > li')

etfs = {}

for row in rows:
    try :
        etf_name = re.findall('^(.*) \(NYSE',row.text)
        etf_market = re.findall('\((.*)\|',row.text)
        etf_ticker = re.findall('NYSE Arca\|(.*)\)',row.text)

        if(len(etf_ticker)>0) & (len(etf_market)>0) & (len(etf_name))>0:
            etfs[etf_ticker[0]] = [etf_market[0],etf_name[0]]
    except AttributeError as err:
        pass

# print(etfs)

df = pd.DataFrame(etfs)
# print(df)

data = {'name':['jerry','riah','Paul'],
        'algol':["A","A+","B"],
        'basic':["C","b","B+"],
        'c++':["B+","C","C+"]


        }

data2 = {
    'c0':[1,2,3],
    'c1':[4,5,6,],
    'c2':[7,8,9],
    'c3':[10,11,12],
    'c4':[13,14,15]


}

df =pd.DataFrame(data)
df.set_index('name',inplace=True)
print(df)

print('\n')

df2= pd.DataFrame(data2)
df2.set_index('c0',inplace=True)
print(df2)

writer = pd.ExcelWriter("D:/5674-833_4th/df_excelwriter.xlsx")
df.to_excel(writer,sheet_name='sheet1')
df2.to_excel(writer,sheet_name='sheet2')
writer.save()

