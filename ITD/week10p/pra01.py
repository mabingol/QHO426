import sqlite3
db = sqlite3.connect('teaching4.db')
cursor = db.cursor()

"""
prod_desc = input("Enter the new product description: ")
sql_insert = "INSERT INTO product(descrip) \
              VALUES (?)"
cursor.execute(sql_insert, (prod_desc,))
print("New product inserted")
db.commit()
"""

sql_query = "SELECT * \
             FROM price"
cursor.execute(sql_query)
rows = cursor.fetchall()
for row in rows:
    print(row)
db.close()
