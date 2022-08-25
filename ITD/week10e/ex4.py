import sqlite3
import datetime
db = sqlite3.connect('teaching4.db')
cursor = db.cursor()

cursor.execute("PRAGMA foreign_keys=ON") #Important for FK check

prod_id = input("Enter the product id of the product that you want to set a new price:  ")
sql_query = "SELECT stdprice \
             FROM price \
             WHERE prodid = ?"
cursor.execute(sql_query, (prod_id,))
price_row = cursor.fetchone()
if price_row:
  current_price = price_row[0]
  print("Current price for prodid", prod_id, " is", current_price)
  new_price = float(input("Enter the new price: "))
  now = datetime.datetime.now()
  todays_date = now.strftime("%Y-%m-%d")
  try:
    sql_update = "UPDATE price \
                  SET enddate = ? \
                  WHERE prodid = ? \
                  AND enddate is NULL"
    cursor.execute(sql_update, (todays_date, prod_id))
    sql_insert = "INSERT INTO price \
                  VALUES (?,?,?,?,?)"
    cursor.execute(sql_insert, (prod_id, todays_date, new_price, new_price-3.0,None))
    print("The price has been updated")
    db.commit()
  except db.Error:
    print("Rolling back the changes as smthg went wrong")
    db.rollback()
else:
  print("The item is not found in DB")