import sqlite3
db = sqlite3.connect('teaching4.db')
cursor = db.cursor()

sql_query = "SELECT * \
             FROM price"
cursor.execute(sql_query)
rows = cursor.fetchall()
for row in rows:
    print(row)
db.close()