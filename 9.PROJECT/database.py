import sqlite3

DATABASE = './newcrmdb.db'

def get_users():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row # 출력 결과물을 dict 타입으로 변경
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    users2 = [dict(row) for row in users]
    conn.close()

    return users2

def get_users_by_name(name):
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row # 출력 결과물을 dict 타입으로 변경
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE Name LIKE ?", ('%' + name + '%',))
    users = cur.fetchall()
    users2 = [dict(row) for row in users]
    conn.close()

    return users2