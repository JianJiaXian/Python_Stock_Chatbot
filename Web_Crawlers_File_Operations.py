#模擬真實瀏覽器使用情況
import requests
url = 'https://tw.stock.yahoo.com/q/bc?s=2330'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
resp = requests.get(url, headers=headers)
print(resp.text)

#爬的網頁有表單
import requests
# 欲提交的表單資料，使用 dict 結構
payload = {
    '表單name1': '值1',
    '表單name2': '值2',
}
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
resp = requests.post('https://jsonplaceholder.typicode.com/posts', data=payload, headers=headers)
print(resp.text)

#BeautifulSoup模組
import time
import requests
from bs4 import BeautifulSoup
import csv
stocks = [2330, 2308, 2454]
soup = BeautifulSoup(resp.text, 'html.parser')
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
performance_list = []
for stock_id in stocks:
    print(stock_id)
    url = f'https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID={stock_id}'
    resp = requests.get(url, headers=headers)
    resp.encoding = 'utf-8'
    raw_html = resp.text
    soup = BeautifulSoup(raw_html, "html.parser")
    def parse_str_to_float(raw_value):
        return float(raw_value.replace(',', ''))
    for index in range(5, 10):
        print('index', index)
        performance_dict = {}
        performance_dict['id']=stock_id
        performance_dict['revenue_date'] = soup.select(f'#divDetail > table > tr:nth-child({index}) > td:nth-child(1) > nobr')[0].text
        performance_dict['final_price'] = soup.select(f'#divDetail > table > tr:nth-child({index}) > td:nth-child(3) > nobr')[0].text
        performance_dict['year_revenue'] = parse_str_to_float(soup.select(f'#divDetail > table > tr:nth-child({index}) > td:nth-child(11) > nobr')[0].text)
        #print('revenue_date:', revenue_date, 'final_price:', final_price, 'year_revenue', year_revenue)
        performance_list.append(performance_dict)
    print('暫停3秒...')
    time.sleep(3)
with open('performance.csv', 'w',newline="") as output_file:
    headers = ['id','revenue_date', 'final_price', 'year_revenue']
    dict_writer = csv.DictWriter(output_file, headers)
    dict_writer.writeheader()
    dict_writer.writerows(performance_list)