import sqlite3

conn = sqlite3.connect('example.db')
cur = conn.cursor()

cur.execute('UPDATE users SET age = ? WHERE name = ?')

conn.commit()
conn.close()