import sqlite3

conn = sqlite3.connect("gifs.db")

cursor = conn.execute("SELECT * FROM gifs")

for row in cursor:
    print(row)

conn.close()