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

def main():
    # 테이블 생성
    create_table()
    # 데이터 삽입
    insert_users('Alice', 30)
    insert_users('Bob', 25)
    insert_users('Chris', 35)
    # 데이터 조회
    print('-----데이터 조회 시작-----')
    users = fetch_users()
    for user in users:
        print(user)
    print('-----데이터 조회 끝-----')
    # 데이터 수정
    update_users('Alice', 25)
    # 데이터 조회
    print('-----엘리스 수정 후, 데이터 조회 시작-----')
    users = fetch_users()
    for user in users:
        print(user)
    print('-----데이터 조회 끝-----')
    # 데이터 삭제
    delete_users('Bob')
    # 데이터 조회
    print('-----밥 삭제 후, 데이터 조회 시작-----')
    users = fetch_users()
    for user in users:
        print(user)
    print('-----데이터 조회 끝-----')


if __name__ == "__main__":
    main()