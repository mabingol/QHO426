import sqlite3

def _total_rows(table_name):
  sql_query = "SELECT COUNT(*) FROM {0}".format(table_name)
  cursor.execute(sql_query)
  rows = cursor.fetchall()
  rowcount = rows[0][0]
  return rowcount

db = sqlite3.connect('C:\sqlite\teaching3.db')
cursor = db.cursor()
sql_query = "SELECT tbl_name \
FROM sqlite_master \
WHERE type = 'table' \
ORDER BY tbl_name"
cursor.execute(sql_query)
all_tables = cursor.fetchall()
print("{0:25}\t{1:8}\n".format("Table","Rowcount"))
for table in all_tables:
  table_name = table[0]
  rowcount = _total_rows(table_name)
  print("{0:25}\t{1:8}".format(table_name,rowcount))
  db.close()
