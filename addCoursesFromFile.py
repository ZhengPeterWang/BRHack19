import os
import sqlite3   # Enable control of an SQLite database
import sys
import json

with open('CS.json', 'r') as f:
    fileDict = json.load(f)
classes = fileDict["data"]["classes"]
data = []
for class in classes:
    for section in classes["enrollGroups"]["classSections"]:
        for meeting in section["meetings"]:
            data.append((class["ssrComponent"], section["classId"], class["titleLong"], )
examples = [(2, "def"), (3, "ghi"), (4, "jkl")]
cur.executemany("INSERT INTO samples VALUES (?, ?)", examples)
