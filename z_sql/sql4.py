import sqlite3
db = sqlite3.connect('newdatabase.db')
cursor = db.cursor()


sql_query = "SELECT * \
              FROM price" 	
cursor.execute(sql_query)
all_price_rows = cursor.fetchall()
print(all_price_rows)

print("{0:5} {1:10} {2:25} {3:36} {4:46}".format('Prodid','StartDate', 'StdPrice', 'MinPrice', 'EndDate'))
for price_row in all_price_rows:
	prodid = price_row[0]
	startdate = price_row[1]
  stdprice = price_row[2]
  minprice = price_row[3]
  enddate = price_row[4]
	print("{0:5} {1:10} {2:25} {3:36} {4:46}".format(prodid, startdate, stdprice, minprice, enddate))