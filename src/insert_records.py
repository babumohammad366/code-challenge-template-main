import os
import sqlite3
from datetime import datetime

# INPUT_FILES 
WEATHER_DATA_DIR = "../wx_data"
YIELD_DATA_DIR = "../yld_data"

#Connecting to sqlite
conn = sqlite3.connect('./test.db')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

def get_all_files(directory):
   files = []
   for filename in os.listdir(directory):
       if filename.endswith(".txt"): 
            files.append(os.path.join(directory, filename))
   return files

files = get_all_files(WEATHER_DATA_DIR)

def insert_to_weather(file_path):
   with open(file_path, "r") as fb_obj:
      lines = fb_obj.readlines()

   records = []
   region = file_path.split("/")[-1].split(".")[0]
   for line in lines:
      row = line.split("\t")
      record_date = datetime.strptime(row[0], '%Y%m%d')
      records.append((region, record_date, row[1], row[2], row[3]))
   cursor.executemany('INSERT OR IGNORE INTO WEATHER_DATA VALUES(?,?,?,?,?) ;',records);


[ insert_to_weather(file_path) for file_path in files ] 


files = get_all_files(YIELD_DATA_DIR)
def insert_to_yield(file_path):
   with open(file_path, "r") as fb_obj:
      lines = fb_obj.readlines()

   records = []
   region = file_path.split("/")[-1].split(".")[0]
   for line in lines:
      row = line.split("\t")
      records.append((region, row[0], row[1]))
   cursor.executemany('INSERT OR IGNORE INTO YIELD VALUES(?,?,?) ;',records);


[ insert_to_yield(file_path) for file_path in files ]

# Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()