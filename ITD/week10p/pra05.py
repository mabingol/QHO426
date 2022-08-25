import sqlite3
db = sqlite3.connect('teaching4.db')
cursor = db.cursor()
# enable foreign key constraints
cursor.execute("PRAGMA foreign_keys=ON")
# start of code where exception needs to be handled

try:
    # check if employee entered exists in the database
  emp_name = input("Enter the name of the employee to delete ")
  sql_query = "SELECT empno \
                FROM emp \
                WHERE UPPER(ename)=UPPER(?)"
  cursor.execute(sql_query,(emp_name,))
  emp_row = cursor.fetchone()
   # if employee exists then try to delete them
  if emp_row:
    empno = emp_row[0]
    sql_delete = "DELETE FROM emp WHERE empno=(?)"
    cursor.execute(sql_delete,(empno,))
    # commit the changes
    db.commit()
    print("Employee ",emp_name, "deleted successfully")
  else:
    print ("Employee entered not found in database")
except db.Error:
  print ("Employee cannot be deleted as they are a manager or sales rep")


"""
sql_query = "SELECT * \
             FROM emp"
cursor.execute(sql_query)
rows = cursor.fetchall()
for row in rows:
    print(row)
db.close()
"""