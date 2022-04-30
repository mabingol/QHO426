import sqlite3
db = sqlite3.connect('newdatabase.db')
cursor = db.cursor()
prod_desc = input("Enter the new product description: ")
sql_insert = "INSERT INTO product(descrip) \
		      VALUES (?)"
cursor.execute(sql_insert,(prod_desc,))
print ("Inserted new product record")
db.commit()