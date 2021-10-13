import sqlite3

con = sqlite3.connect("db/hr.db")

print("DB connected")

with con:
    c = con.cursor()

    for row in c.execute("SELECT * FROM SRHR"):
        print(row)
