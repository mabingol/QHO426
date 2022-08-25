import sqlite3
db = sqlite3.connect('teaching4.db')
cursor = db.cursor()
cursor.execute("PRAGMA foreign_keys=ON")

perc_incr = int(input("Enter % salary increase (between 1 and 10): "))
if perc_incr >= 1 and perc_incr <= 10:
  sal_multiplier = 1 + (perc_incr/100)
  sql_update = "UPDATE emp \
		            SET monthly_sal = monthly_sal(?) \
                WHERE job='SALESREP'"
	cursor.execute(sql_update,(sal_multiplier,))
  db.commit()
	print("Sales rep monthly salary increased by ",perc_incr,"%")
else:
  print ("Percentage must be between 1% and 10%")
