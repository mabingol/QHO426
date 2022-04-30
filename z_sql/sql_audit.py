import sqlite3
db = sqlite3.connect('newdatabase.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS AUDIT_LOG (audit_log_no INTEGER PRIMARY KEY AUTOINCREMENT , table_changed TEXT, when_changed TEXT, change_type TEXT, row_changed INTEGER, old_value TEXT, new_value TEXT)")
db.commit()