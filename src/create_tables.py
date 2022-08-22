import sqlite3

#Connecting to sqlite
conn = sqlite3.connect('./test.db')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

with open('sql/tables_ddl.sql', "r") as fb_obj:

#Creating table as per requirement
   sql_script = fb_obj.read()

   for sql in sql_script.split(";"):
      cursor.execute(sql)

print("Table created successfully........")

# Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()