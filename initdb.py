import sqlite3
conn = sqlite3.connect('myDB.db')
cur = conn.cursor()
req = "CREATE TABLE code(uid CHAR(15) PRIMARY KEY, code text,language text)"
cur.execute(req)
conn.commit()
req = "CREATE TABLE user(id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, ip text,navigator text,lastCommit DATETIME)"
cur.execute(req)
conn.commit()
conn.close()