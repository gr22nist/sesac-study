import sqlite3

# 사용자 DB
DATABASE = 'users.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # 행을 sqlite3.Row 라는 객체 타입으로 반환
                                    # 설정하면 각 Row의 결과가 Dict 유형으로 반환됨
    return conn

def get_query(query, params):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(query, params)
    result = cur.fetchall()
    conn.close()
    return result


def execute_query(query):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    conn.close()


def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL)
    ''')

    cur.execute("SELECT COUNT(*) AS count FROM users")
    count = cur.fetchone()['count']
    # count = cur.fetchone()[0] # 이건 Row 타입이 아닌 기본값(튜플)로 반납될 때

    if count == 0:
        cur.execute('INSERT INTO users (username, password) VALUES (?, ?)', ('user1', 'password1'))
        cur.execute('INSERT INTO users (username, password) VALUES (?, ?)', ('user2', 'password2'))
        conn.commit()
    
    cur.execute('SELECT * FROM users')
    rows = cur.fetchall()

    print('-' * 30)
    for row in rows:
        print(row['id'], row['username'], row['password'])
    print('-' * 30)

    conn.close()