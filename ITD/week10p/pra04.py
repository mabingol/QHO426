import sqlite3
db = sqlite3.connect('teaching4.db')
cursor = db.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

"""
job_to_incr = input("Enter the job that you want to increase the monthly salary for: ")
perc_incr = int(input("Enter % salary increase (between 1 and 10): "))
if perc_incr >= 1 and  perc_incr <=10:
  sal_multiplier = 1 + (perc_incr/100)
  sql_update = "UPDATE emp \
                SET monthly_sal = monthly_sal*(?) \
                WHERE job=UPPER(?)"
  cursor.execute(sql_update,(sal_multiplier, job_to_incr))
  db.commit()
  print("All employees with a job of {0} have had their monthly salary increased by {1}%".format(job_to_incr, perc_incr))
else:
  print ("Percentage must be between 1% and 10%")

"""

sql_query = "SELECT * \
             FROM emp"
cursor.execute(sql_query)
rows = cursor.fetchall()
for row in rows:
    print(row)
db.close()
