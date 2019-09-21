import os
import sqlite3  # Enable control of an SQLite database
import sys
import json

con = sqlite3.connect("database.db")
cur = con.cursor()

with open("CS.json", "r") as f:
    fileDict = json.load(f)
    classes = fileDict["data"]["classes"]
    data = []
    for cl in classes:
        for egroup in cl["enrollGroups"]:
            for section in egroup["classSections"]:
                for meeting in section["meetings"]:
                    pat = meeting["pattern"]
                    day = (
                        int("M" in pat),
                        int("T" in pat),
                        int("W" in pat),
                        int("R" in pat),
                        int("F" in pat),
                    )
                data.append(
                    (
                        section["ssrComponent"],
                        section["classNbr"],
                        cl["titleLong"],
                        day[0],
                        day[1],
                        day[2],
                        day[3],
                        day[4],
                        meeting["timeStart"],
                        meeting["timeEnd"],
                        cl["crseId"],
                    )
                )
    cur.executemany(
        "INSERT INTO classList  (ssrComponent, classID, name, mon, tue, wed, thu, fri, timeStart, timeEnd, courseID) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        data,
    )
con.commit()
con.close()
