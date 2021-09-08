import os

fPath = '/Users/dixon/Documents/GitHub/Python-Projects/Database_Assignment/Files/'

lDir = os.listdir(fPath)

for files in lDir:
    if files.endswith('.txt'):
        files_txt = files
        print(files_txt)


import sqlite3

conn = sqlite3.connect('db_Assignment.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_assignment( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName TEXT \
        )")
    conn.commit()
conn.close()


conn = sqlite3.connect('db_Assignment.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_assignment(col_fileName) VALUES (?)", (files_txt))
    conn.commit()
conn.close()


