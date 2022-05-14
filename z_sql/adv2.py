import sqlite3
db = sqlite3.connect('c:\sqlite\teaching2.db')
cursor = db.cursor()
table_name = input("Enter the name of the table you want to describe: ")
all_cols = cursor.execute("PRAGMA table_info("+table_name+")").fetchall()
