"""
import sqlite3
db = sqlite3.connect('newterm2.db')
cursor = db.cursor()
sql_query = "SELECT custid, area, name \
             FROM customer"  #your query
cursor.execute(sql_query)
##Your program comes here##
all_cust_rows = cursor.fetchall()
for cust_row in all_cust_rows:
  print(cust_row)
##########

db.close()

"""
#####################

import sqlite3
db = sqlite3.connect('newterm2.db')
cursor = db.cursor()
sql_query = "SELECT custid, area, name \
             FROM customer"  #your query
cursor.execute(sql_query)
##Your program comes here##
all_cust_rows = cursor.fetchall()
for cust_row in all_cust_rows:
  cust_id = cust_row[0]
  cust_area = cust_row[1]
  cust_name = cust_row[2]
  print("{0} \t{1} \t{2}".format(cust_id,cust_area,cust_name))
##########

db.close()
