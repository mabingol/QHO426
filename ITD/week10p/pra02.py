import sqlite3
db = sqlite3.connect('teaching4.db')
cursor = db.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

cust_name = input("Enter the name of the new customer: ")
cust_repid = input("Enter their sales rep id: ")
cust_creditlimit = input("Enter their creditlimit: ")

sql_query = "SELECT empno \
              FROM emp \
              WHERE empno = ? \
              AND job = 'SALESREP'"
cursor.execute(sql_query,(cust_repid,))
emp_row = cursor.fetchone()
if emp_row is not None:
  sql_insert = "INSERT INTO customer(name, repid, creditlimit) \
                VALUES (?,?,?)"
  cursor.execute(sql_insert,(cust_name,cust_repid,cust_creditlimit))
  db.commit()
  print("Customer ",cust_name, "inserted successfully")
else:
  print ("Sales rep id not found in the database")
"""

sql_query = "SELECT * \
             FROM customer"
cursor.execute(sql_query)
rows = cursor.fetchall()
for row in rows:
    print(row)
db.close()
"""