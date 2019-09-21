import os
import sqlite3   # Enable control of an SQLite database
import sys
import json

with open('CS.json', 'r') as f:
    fileDict = json.load(f)
classes = fileDict["data"]["classes"]
data = []
for c in classes:
    for section in classes["enrollGroups"]["classSections"]:
        for meeting in section["meetings"]:
            data.append((c["ssrComponent"], section["classId"], c["titleLong"], )

cur.executemany("INSERT INTO samples VALUES (?, ?, ?, ?, ?, ?, ?)", data)

