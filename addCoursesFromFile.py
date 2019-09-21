
import os
import sqlite3   # Enable control of an SQLite database
import sys
import json
con = sqlite3.connect("database.db")
cur = con.cursor()

with open('CS.json', 'r') as f:
    fileDict = json.load(f)
    classes = fileDict["data"]["classes"]
    data = []
    for cl in classes:
        for section in cl["enrollGroups"]["classSections"]:
            for meeting in section["meetings"]:
                data.append((cl["ssrComponent"], section["classId"], cl["titleLong"], meeting["pattern"], meeting["timeStart"], meeting["timeEnd"], cl["crseId"] )
cur.executemany("INSERT INTO database VALUES (?, ?, ?, ?, ?, ?, ?)", data)


