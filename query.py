import os
import sqlite3  # Enable control of an SQLite database
import sys
import json
import csv

con = sqlite3.connect("database.db")
cur = con.cursor()

with open("selectiveList.json", "r") as f:
    fileDict = json.load(f)
    nbr = fileDict["classNbr"]
for i in nbr:
    cur.execute("INSERT INTO sellist (classNbr) VALUES (? ) ", (i,))

cur.execute(
    "CREATE TABLE result AS \
    SELECT * FROM classList INNER JOIN sellist ON sellist.classNbr == classList.classID"
)

cur.execute(
    "SELECT * FROM classList WHERE (classID NOT IN (SELECT classNbr FROM result)) \
    AND NOT EXISTS (SELECT * FROM result WHERE result.timeStart <= classList.timeEnd \
    AND result.timeEnd >= classList.timeStart \
    AND (result.mon == classList.mon OR result.tue == classList.tue OR result.wed == classList.wed OR \
    result.thu == classList.thu OR result.fri == classList.fri))"
)

res = cur.fetchall()

con.commit()
con.close()
"""
for i in res:
    print(i)
"""

with open("out.csv", "w") as out:
    csv_out = csv.writer(out)
    csv_out.writerow(
        [
            "sessionName",
            "csrID",
            "courseName",
            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri",
            "startTime",
            "endTime",
            "csrCompleteID",
        ]
    )
    for row in res:
        csv_out.writerow(row)

