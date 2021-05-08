import sqlite3

def insert_varible_into_table(dev_id, name, email, join_date):

    sqlite_connection = sqlite3.connect(':memory:')

    cursor = sqlite_connection.cursor()
    print("Подключен к SQLite")

    sqlite_connection = sqlite3.connect(':memory:')
    sqlite_create_table_query = '''CREATE TABLE sqlitedb_developers (
                                    id TEXT,
                                    name TEXT,
                                    email TEXT,
                                    joining_date TEXT);'''

    cursor = sqlite_connection.cursor()
    print("База данных подключена к SQLite")
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    print("Таблица SQLite создана")

    sqlite_insert_with_param = """INSERT INTO sqlitedb_developers
                                  (id, name, email, joining_date)
                                  VALUES (?, ?, ?, ?);"""

    data_tuple = (dev_id, name, email, join_date)
    cursor.execute(sqlite_insert_with_param, data_tuple)
    sqlite_connection.commit()
    print("Переменные Python успешно вставлены в таблицу sqlitedb_developers")
    print(cursor.execute("SELECT * FROM sqlitedb_developers"))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()

name = 'coderoad'
url = 'https://coderoad.ru/4979542/Python'
date = '021-04-27'
tags = {0: 'a 65', 1: 'iframe 2', 2: 'span 1', 3: 'h5 2', 4: 'button 6', 5: 'form 1', 6: 'hr 7', 7: 'h3 1', 8: 'p 20', 9: 'script 19', 10: 'ins 2', 11: 'small 11', 12: 'code 5', 13: 'div 48', 14: 'body 1', 15: 'pre 4', 16: 'h4 1', 17: 'h1 1', 18: 'b 5', 19: 'nav 4', 20: 'style 2', 21: 'li 42', 22: 'title 1', 23: 'ul 8', 24: 'input 1', 25: 'html 1', 26: 'br 32', 27: 'head 1', 28: 'link 5', 29: 'meta 4', 30: 'i 21'}



insert_varible_into_table(name, url, date, str(tags))
