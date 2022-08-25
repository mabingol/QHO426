import sqlite3

db = sqlite3.connect('teaching4.db')
cursor = db.cursor()


cursor.execute("PRAGMA foreign_keys=ON")

dept_name = input("Enter the new department name:  ")
dept_locn = input("Enter the location for the new department:  ")
sql_insert = "INSERT INTO dept(dname,location) \
              VALUES (UPPER(?),UPPER(?))"

cursor.execute(sql_insert, (dept_name, dept_locn))
print("Inserted new department")
db.commit()


sql_query = "SELECT * \
             FROM dept"
cursor.execute(sql_query)
rows = cursor.fetchall()
for row in rows:
    print(row)
db.close()
