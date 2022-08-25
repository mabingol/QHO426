import sqlite3
db = sqlite3.connect('teaching4.db')
cursor = db.cursor()

cursor.execute("PRAGMA foreign_keys=ON")
dept_name = input("Enter the new department you want to change:  ")
sql_query = "SELECT deptno \
             FROM dept \
             WHERE dname = UPPER(?)"
cursor.execute(sql_query, (dept_name,))
dept_row = cursor.fetchone()

if dept_row:
  new_locn = input("Enter the new location for the department:  ")
  sql_update = "UPDATE dept \
                SET location = UPPER(?) \
                WHERE dname = UPPER(?)"
  cursor.execute(sql_update, (new_locn, dept_name))
  print("Department location is updated")
  db.commit()
else:
  print("Department not found in the DB")



sql_query = "SELECT * \
             FROM dept"
cursor.execute(sql_query)
rows = cursor.fetchall()
for row in rows:
    print(row)
db.close()
