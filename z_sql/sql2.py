import sqlite3
#db = sqlite3.connect('C:\sqlite\newdatabase.db')
db = sqlite3.connect('newdatabase.db')
cursor = db.cursor()

sql_query = "SELECT ename, name \
             FROM customer c \
             INNER JOIN emp e ON c.repid = e.empno \
             ORDER BY ename"
cursor.execute(sql_query)
all_rows = cursor.fetchall()
print('RepName','CustName',)
for row in all_rows:
  repname = row[0] 
  custname = row[1]
  print("{0}\t{1}".format(repname, custname))

db.close()
