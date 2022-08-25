import sqlite3

db = sqlite3.connect('newterm2.db')
cursor = db.cursor()

sql_query = "SELECT  IFNULL(m.ename, 'No Manager'), e.ename\
             FROM emp e \
                  LEFT OUTER JOIN emp m ON e.mgr = m.empno\
                  ORDER BY m.ename, e.ename"                                                                                                     #your query
cursor.execute(sql_query)
all_emp_rows = cursor.fetchall()

print("{0:15}\t{1:40}".format("Manager Name",
                              "Names of the employees they manage"))
last_mgr_name = ""
for emp_row in all_emp_rows:
    mgr_name = emp_row[0]
    emp_name = emp_row[1]
    if mgr_name != last_mgr_name:
        print("\n{0:15}\t{1:40}".format(mgr_name, emp_name))
        last_mgr_name = mgr_name
    else:
        print("{0:15}\t{1:40}".format("", emp_name))

##########

db.close()
