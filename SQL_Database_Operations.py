'''
import sqlite3
connection = sqlite3.connect('demo.db')
cursor = connection.cursor()
'''
#新增stocks資料表
'''
cursor.execute(
        (多行註解)
        CREATE TABLE stocks (
                id INT PRIMARY KEY NOT NULL,
                company_name TEXT NOT NULL,
                price INT NOT NULL
        );
        (多行註解)
)
'''

#新增股票資料
'''
cursor.execute(
        (多行註解)
        INSERT INTO stocks (id, company_name, price)
        VALUES (2330, '台積電', 220);
        (多行註解)
)
cursor.execute(
        (多行註解)
        INSERT INTO stocks (id, company_name, price)
        VALUES (2317, '鴻海', 82);
        (多行註解)
)
'''

#更新資料
'''
cursor.execute(
        (多行註解)
        UPDATE stocks
        SET company_name = '台雞店'
        WHERE id=2330;
        (多行註解)
)
'''
'''
#移除資料
cursor.execute(
        (多行註解)
        DELETE FROM stocks 
        WHERE id=2330;
        (多行註解)
)

#查詢資料
rows = cursor.execute(
        (多行註解)
        SELECT *
        FROM stocks;
        (多行註解)
)

#將查到的資料用for印出，row[0]為第一個欄位
for row in rows:
        print(f'id:{row[0]}, company_name:{row[1]}, price:{row[2]}')

connection.commit()
connection.close()
'''

#HW10
'''
參考課程範例建立一個 SQLite 資料庫 stock_db.db 和資料表 stocks,
將stock.csv資料的 證券代號（id）、證券名稱（name）、收盤價（closing_price），
存入建立的 SQLite 資料庫中。
資料表 stocks 欄位為 id（主鍵 PRIMARY KEY）, 
name, closing_price 類別分別為 文字、文字、數字，不為空值。
並使用 Python + SQLite 套件進行查詢收盤價格（closing_price）大於 30 者，印出所查詢的資料。
'''
import pandas as pd
df = pd.read_csv('stock.csv')
import sqlite3
connection = sqlite3.connect('stock_db.db')
cursor = connection.cursor()
cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS stocks (
                id TEXT PRIMARY KEY NOT NULL,
                name TEXT NOT NULL,
                closing_price INT NOT NULL
        );
        '''
)
for index,row in df.iterrows():
    cursor.execute(
        '''
        INSERT INTO stocks (id,name,closing_price)
        VALUES ('{}','{}','{}');
        '''.format(row['證券代號'],row['證券名稱'],row['收盤價'])
    )

rows = cursor.execute(
        '''
        SELECT * FROM stocks 
        WHERE closing_price > 30;
        '''
)
for row in rows:
        print(f'id:{row[0]}, company_name:{row[1]}, price:{row[2]}')

connection.commit()
connection.close()