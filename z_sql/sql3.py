import sqlite3
import datetime
db = sqlite3.connect('newdatabase.db')
cursor = db.cursor()
cursor.execute("PRAGMA foreign_keys=ON")
cursor.execute("SELECT seq+1 \
		          FROM sqlite_sequence \
		          WHERE name='product'")
seq_row = cursor.fetchone()
next_prodid = seq_row[0]

###########################

prod_desc = input("Enter the new product description: ")
sql_insert = "INSERT INTO product(descrip) \
      		    VALUES (?)"
cursor.execute(sql_insert,(prod_desc,))
curr_date = datetime.date.today().strftime("%Y-%m-%d")
sql_insert = "INSERT INTO price (prodid, startdate, stdprice, minprice, enddate) \
      		     VALUES (?, ?, ?, ?, ?)"
cursor.execute(sql_insert,(next_prodid,curr_date,30.7,25.3,None))
print ("Inserted new product and price with prodid= \n",next_prodid)
#db.rollback()
db.commit()
#cursor.execute("COMMIT") 

sql_query = "SELECT * \
              FROM product"
cursor.execute(sql_query)
all_product_rows = cursor.fetchall()
#print(all_product_rows)

print ("This is PRODUCT TABLE \n")

print("{0:5} {1:9}".format('Prodid','Product Description'))
for prod_row in all_product_rows:
	prodno = prod_row[0]
	description = prod_row[1]
	print("{0:5} {1:9}".format(prodno, description))

print ("This is PRICE TABLE \n")
sql_query = "SELECT * \
              FROM price" 	
cursor.execute(sql_query)
all_price_rows = cursor.fetchall()
print(all_price_rows)
