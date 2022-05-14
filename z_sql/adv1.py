import sqlite3
import hashlib

def _encrypt_password(password):
  encrypted_pass = hashlib.sha1(password.encode('utf-8')).hexdigest()
  return encrypted_pass

#db = sqlite3.connect('teaching1.db')
db = sqlite3.connect('C:\sqlite\teaching3.db')
db.create_function('encrypt', 1, _encrypt_password)
cursor = db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY    		  AUTOINCREMENT, email TEXT, password TEXT) """)
email = input("Enter the email address of the new user: ")
pwd = input("Enter the new password: ")
sql_insert = "INSERT INTO users(email, password) \
                   VALUES (?,encrypt(?))"
cursor.execute(sql_insert,(email,pwd))
db.commit()
db.close()