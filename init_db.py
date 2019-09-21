import os
import sqlite3  # Enable control of an SQLite database
import sys

f = "database.db"

db = sqlite3.connect(f)  # open if f exists, otherwise create
c = db.cursor()  # facilitate db ops

# maybe add selected boolean
q = "CREATE TABLE classList (ssrComponent STRING, classID INTEGER, name STRING, mon INTEGER, tue INTEGER, wed INTEGER, thu INTEGER, fri INTEGER, timeStart INTEGER, timeEnd INTEGER, courseID INTEGER)"
c.execute(q)
c.execute("CREATE TABLE sellist (classNbr INTEGER)")
