import sqlite3
db = sqlite3.connect('newdatabase.db')
cursor = db.cursor()
sql_update = "UPDATE customer \
	         SET creditlimit=(?) \
	         WHERE custid=(?)"
cursor.execute(sql_update,(new_limit,curr_cust)
sql_insert ="INSERT INTO audit_log (table_changed, when_changed, \
            change_type, row_changed, old_value, new_value) \
            VALUES (?,?,?,?,?,?)"
cursor.execute(sql_insert,('Customer',curr_date_time, \   			        
                           'Update Credit Limit',curr_cust, curr_limit, new_limit))
db.commit()
