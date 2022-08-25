import sqlite3

db = sqlite3.connect('newterm2.db')
cursor = db.cursor()

custid = input("Enter the id for the customer you want to display:  ")

sql_query = "SELECT name, creditlimit \
             FROM customer \
             WHERE custid = ?"                        #your query
cursor.execute(sql_query, (custid, ))
##Your program comes here##
cust_row = cursor.fetchone()
#if a row was returned, print the details
if cust_row:
    cust_name = cust_row[0]
    credit_limit = cust_row[1]
    print("Customer {0} has a credit limit of £{1:.2f}".format(
        cust_name, credit_limit))
#if the customer number is not found
else:
    print("No customer found with that id")

##########

db.close()
