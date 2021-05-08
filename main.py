import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tld import get_fld
from datetime import datetime
import sqlite3
import logging

root = Tk()
root.geometry('400x700')
P = ttk.Progressbar()
P.pack()
process = 0
def update():
    global process
    process += 10
    P['value'] = process
    if P['value'] >= P['maximum']:
        L['text'] = "The Process is done!"
        return
    root.after(300, update)

def load():
    url = entry1.get()
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    tags = []
    for tag in soup.find_all(True):
        tags.append(tag.name)
    tags = set(tags)
    array = []
    for tag in tags:
        redditAll = soup.find_all(tag)
        collect_tags = tag + " " + str(len(redditAll))
        array.append(collect_tags)
    for item in array:
        label['text'] += "\n" + item
    domen = get_fld(url)
    domen = domen.rsplit('.', 2)
    domen_second = domen[0]
    current_datetime = datetime.now().date()
    dict_tags = dict(enumerate(array))

    logging.basicConfig(filename='example.log', encoding='utf-8', format='%(asctime)s %(message)s')
    logging.warning(domen_second)

    def insert_varible_into_table(domen, url, date, tags):
        print("Подключен к SQLite")
        sqlite_connection = sqlite3.connect(':memory:')
        sqlite_create_table_query = '''CREATE TABLE sqlitedb_developers (
                                        domen TEXT,
                                        url TEXT,
                                        date TEXT,
                                        tags TEXT);'''

        cursor = sqlite_connection.cursor()
        print("База данных подключена к SQLite")
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()
        print("Таблица SQLite создана")

        sqlite_insert_with_param = """INSERT INTO sqlitedb_developers
                                      (domen, url, date, tags)
                                      VALUES (?, ?, ?, ?);"""

        data_tuple = (domen, url, date, tags)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqlite_connection.commit()
        print("Переменные Python успешно вставлены в таблицу sqlitedb_developers: ")
        print(cursor.execute("SELECT * FROM sqlitedb_developers"))
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        cursor.close()

    insert_varible_into_table(domen_second, url, current_datetime, str(dict_tags))

def exit():
    root.destroy()

entry1 = Entry(root, width=100)
entry1.pack()
Button(root, text="Load", command=lambda:[load(),update()]).pack()
Button(root, text="Exit", command=exit).pack()
label = tk.Label(root, text="Status: ")
label.place(x=5, y=70)
label = tk.Label(root, text="Tags:")
label.place(x=300, y=70)

L = Label(root)
L.place(x=45, y=70)

root.mainloop()