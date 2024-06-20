import sqlite3

my_db = 'example.db'

def connect_db():
    return sqlite3.connect(my_db)

def create_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL
                )      
                ''')
    conn.commit()
    conn.close()

def insert_users(name, age):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
    conn.commit()
    conn.close()

def fetch_users():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users')
    rows = cur.fetchall()
    conn.close()
    return rows

def update_users(name, new_age):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('UPDATE users SET age = ? WHERE name = ?', (new_age, name))
    conn.commit()
    conn.close()

def delete_users(name):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('DELETE FROM users WHERE name = ?', (name,))
    conn.close()