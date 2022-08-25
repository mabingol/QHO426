import sqlite3
db = sqlite3.connect('teaching4.db')
cursor = db.cursor()

cursor.execute("PRAGMA foreign_keys=ON") #Important for FK check

dept_name = input("Enter the name of the department you want to delete:  ")
dept_locn = input("Enter the name of the department location you want to delete:  ")
sql_query = "SELECT deptno \
             FROM dept \
             WHERE dname = UPPER(?) AND location = UPPER(?)"
cursor.execute(sql_query, (dept_name,dept_locn))
dept_row = cursor.fetchone()
if dept_row:
  # if the dept name enterd is a valid dept, then delete the row
  try:
    sql_delete = "DELETE FROM dept \
                  WHERE dname = UPPER(?) AND location = UPPER(?)"
    cursor.execute(sql_delete, (dept_name,dept_locn))
    print("Department is deleted")
    db.commit()
  except db.Error:
    print("Cannot delete department as it has employees")
else:
    print("Department not found in the DB")