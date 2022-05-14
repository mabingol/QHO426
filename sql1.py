import sqlite3
db = sqlite3.connect('newdatabase.db')
cursor = db.cursor()

"""
sql_query = "SELECT empno, ename, deptno \
              FROM emp" 		# define the query
cursor.execute(sql_query)
emp_row = cursor.fetchone()
all_emp_rows = cursor.fetchall()
print(emp_row)
print('{0}, {1}, {2}'. format(emp_row[0], emp_row[1], emp_row[2]))
#print(all_emp_rows)


sql_query = "SELECT empno, ename, deptno \
		        FROM emp"
cursor.execute(sql_query)
all_emp_rows=cursor.fetchall()
for emp_row in all_emp_rows:
	empno = emp_row[0]
	ename = emp_row[1]
	deptno = emp_row[2]
print("{0},{1},{2}".format(empno, ename, deptno))
"""

sql_query = "SELECT empno, ename, monthly_sal \
		        FROM emp"
cursor.execute(sql_query)
all_emp_rows=cursor.fetchall()
print("{0:5} {1:9} {2:10}".format('Empno','Emp_Name','Monthly Salary'))
for emp_row in all_emp_rows:
	empno = emp_row[0]
	ename = emp_row[1]
	monthly_sal = emp_row[2]
print("{0:5} {1:9} £{2:10.2f}".format(empno, ename, monthly_sal))

"""
empname = input("Enter an employee name to display: ")
sql_query = "SELECT empno, ename, monthly_sal \
		        FROM emp \
		        WHERE UPPER(ename)=UPPER(?)"
cursor.execute(sql_query, (empname,))
emp_row = cursor.fetchone()
if emp_row:
	print(emp_row)
else:
	print("No employee found with that name")



dept = input("Enter a deptno: ")
salary= int(input("Enter a minimum monthly salary: "))
sql_query="SELECT ename, deptno, monthly_sal \
                   FROM emp \
                   WHERE deptno=? \
                   AND monthly_sal>=?"
cursor.execute(sql_query,(dept,salary))
all_emp_rows = cursor.fetchall()
for emp_row in all_emp_rows:
    empname = emp_row[0]
    deptno = emp_row[1]
    monthly_sal = emp_row[2]
    print("{0}\t{1}\t{2}".format(empname, deptno, monthly_sal))
"""

db.close()