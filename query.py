import os
import sqlite3  # Enable control of an SQLite database
import sys
import json

con = sqlite3.connect("database.db")
cur = con.cursor()

with open("selectiveList.json", "r") as f:
    fileDict = json.load(f)
    classNbr = fileDict["classNbr"]
cur.executemany("INSERT INTO sellist (classNbr) VALUES (?) ", classNbr)

cur.execute(
    "CREATE TABLE result AS \
    SELECT * FROM database INNER JOIN sellist ON sellist.classNbr == database.classNbr"
)

res = cur.execute(
    "SELECT * FROM database WHERE (classNbr NOT IN (SELECT classNbr FROM result)) \
    AND NOT EXISTS (SELECT * FROM result WHERE result.starttime <= database.endtime \
    AND result.endtime >= database.starttime \
    AND (result.mon == database.mon OR result.tue == database.tue OR result.wed == database.wed OR \
    result.thu == database.thu OR result.fri == database.fri))"
)

con.commit()
con.close()
