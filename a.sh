#!/bin/bash
rm database.db
python3 init_db.py
python3 addCoursesFromFile.py
python3 query.py
