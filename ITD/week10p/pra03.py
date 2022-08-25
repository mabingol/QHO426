import sqlite3
import datetime
db = sqlite3.connect('teaching4.db')
cursor = db.cursor()

"""
cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("SELECT seq+1 \
                FROM sqlite_sequence \
                WHERE name='product'")
seq_row = cursor.fetchone()
next_prodid = seq_row[0]

prod_desc = input("Enter the new product description: ")
std_price = float(input("Enter the standard price for the new product: "))
min_price = float(input("Enter the minimum price for the new product: "))

if min_price > std_price:
  print("The minimum price cannot be more than the standard price")
else:
  sql_insert = "INSERT INTO product(descrip) \
              VALUES (?)"
  cursor.execute(sql_insert, (prod_desc,))

  curr_date = datetime.date.today().strftime("%Y-%m-%d")

  sql_insert = "INSERT INTO price (prodid, startdate, stdprice, \
              minprice, enddate) \
              VALUES (?, ?, ?, ?, ?)"
  cursor.execute(sql_insert, (next_prodid, curr_date, std_price, min_price, None))
  print("Inserted new product and price record with prodid=", next_prodid)

  db.commit()
  
"""

sql_query = "SELECT * \
             FROM price"
cursor.execute(sql_query)
rows = cursor.fetchall()
for row in rows:
    print(row)
db.close()
