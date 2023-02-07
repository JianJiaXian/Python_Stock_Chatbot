#Series
import pandas as pd
serie=pd.Series(['apple','kiwi','orange'])
print(serie)
'''
0     apple
1      kiwi
2    orange
'''
#自定義index
ranking=[3,2,1]
serie = pd.Series(ranking, index=serie)
print(serie)
'''
apple     3
kiwi      2
orange    1
'''

#DataFrame
movies = {
    '名稱': ['名偵探柯南', '復仇者聯盟', '那些年'],
    '票房金額（新台幣）': [1452324, 2324739, 1416601],
    '類別': ['動畫', '動作', '文藝']
}
df = pd.DataFrame(movies)
print(df)
'''
      名稱  票房金額（新台幣）  類別
0  名偵探柯南    1452324  動畫
1  復仇者聯盟    2324739  動作
2    那些年    1416601  文藝
'''
#自定義index
df1 = pd.DataFrame(movies, index=movies['名稱'])
print(df1)
'''
          名稱  票房金額（新台幣）  類別
名偵探柯南  名偵探柯南    1452324  動畫
復仇者聯盟  復仇者聯盟    2324739  動作
那些年      那些年    1416601  文藝
'''
#自定義column順序
df2 = pd.DataFrame(movies, columns=['類別', '票房金額（新台幣）'])
print(df2)
'''
   類別  票房金額（新台幣）
0  動畫    1452324
1  動作    2324739
2  文藝    141660
'''
#取值
for index, row in df.iterrows():
    print(row['名稱'],row['類別'])
'''
名偵探柯南 動畫
復仇者聯盟 動作
那些年 文藝
'''

#loc
print(df.loc[0:1, '名稱':'類別'])
''''
0  名偵探柯南    1452324  動畫
1  復仇者聯盟    2324739  動作
'''

#條件
print(df[df['票房金額（新台幣）'] > 2000000])
'''
     名稱  票房金額（新台幣）  類別
1  復仇者聯盟    2324739  動作
'''

#csv
df=pd.read_csv('./performance.csv',encoding='utf-8')
print(df.head(3))
'''
     id revenue_date  final_price  year_revenue
0  2330      2022/12        448.5       22639.0
1  2330      2022/11        490.0       20713.0
2  2330      2022/10        390.0       18486.0
'''


#info
stock_list = ['2031', '2341', '2342', '2345']
volumes = [23341, 412221, 41907, 3115987]
prices = [23, 41, 41, 3]
#長條圖
import matplotlib.pyplot as plt
'''
plt.bar(stock_list, volumes)
plt.savefig('plot.png')
plt.show()
'''

#折線圖
'''
plt.plot(stock_list, prices)
plt.show()
'''

#圓餅圖
'''
plt.pie(volumes, labels=stock_list)
plt.show()
'''

#stock sample
'''
from matplotlib.font_manager import FontProperties
import pandas as pd
import matplotlib.pyplot as plt
myfont = FontProperties(fname=r'./NotoSansCJK-Black.ttc')
df = pd.read_csv('performance.csv')
data = df.loc[:4, ['revenue_date', 'year_revenue']]
data = data.set_index('revenue_date')
print('data', data)
fig = data.plot(kind='line').get_figure()
plt.title('stock performance(股市表現)',fontproperties=myfont)
plt.show()
'''

#HW9
'''
請下載政府開放資訊網站的 盤後資訊 > 個股日成交資訊檔案(https://data.gov.tw/dataset/11549)，
儲存成 stock_data.csv 
然後使用 DataFrame 物件的 read_csv 方法讀入
並取出 第 2-7 筆資料的 
證券代號,證券名稱,收盤價,成交筆數 值。
然後使用 DataFrame 物件的 read_csv 方法讀入
並取出前 6 筆資料的 證券代號, 收盤價值繪製折線圖
（X 軸為證券代號，Y 軸為 收盤價）。
'''
import csv
import urllib.request
from matplotlib.font_manager import FontProperties
url='https://www.twse.com.tw/exchangeReport/STOCK_DAY_ALL?response=open_data'
myfont = FontProperties(fname=r'./NotoSansCJK-Black.ttc')
urllib.request.urlretrieve(url, './stock.csv')
df = pd.read_csv('stock.csv')
print(df.head())
data1 = df.loc[2:7, ['證券代號', '證券名稱','收盤價','成交筆數']]
print(data1)
data2 = df.loc[2:7, ['證券代號', '收盤價']]
data2 = data2.set_index('證券代號')
fig = data2.plot(kind='line').get_figure()
plt.title('個股日收盤價',fontproperties=myfont)
plt.xlabel('證券代號', fontproperties=myfont)
plt.ylabel('收盤價', fontproperties=myfont)
plt.show()
