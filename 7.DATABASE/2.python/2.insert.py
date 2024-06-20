import sqlite3

# DB에 연결하기

conn = sqlite3.connect('example.db')

# 커서를 통한 데이터 입출력 포인터 가져오기

cur = conn.cursor()

cur.execute('SELECT COUNT(*) FROM users')
count = cur.fetchone()[0]
print(count)


# 커서를 통해 명렁어 보내기
if count == 0:
    cur.execute('INSERT INTO users (name, age) VALUES ("Alice", 30)')

    cur.execute('INSERT INTO users (name, age) VALUES (?, ?)', ("Bob", 25))
    
    conn.commit()
else:
    print('데이터가 이미 있습니다')



# 연결 닫기
conn.close()