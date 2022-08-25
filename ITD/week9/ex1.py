import sqlite3
db = sqlite3.connect('newterm2.db')
cursor = db.cursor()
sql_query = "SELECT * \
             FROM product"
cursor.execute(sql_query)
prod_row = cursor.fetchone()
print(prod_row)

db.close()

