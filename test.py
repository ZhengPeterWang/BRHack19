import os
import sqlite3  # Enable control of an SQLite database
import sys
import json

con = sqlite3.connect("database.db")
cur = con.cursor()

cur.execute("SELECT * FROM classList")
res = cur.fetchall()
print("I am here!")
for i in res:
    print(i)

