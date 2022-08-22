import sqlite3

#Connecting to sqlite
conn = sqlite3.connect('./test.db')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

with open('sql/matrics.sql', "r") as fb_obj:

#Creating table as per requirement
   sql_script = fb_obj.read()
   
   for sql in sql_script.split(";"):
      print(sql)
      cursor.execute(sql)

print("Matrics Table generated successfully........")

# Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()