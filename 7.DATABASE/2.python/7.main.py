# from db_crud import create_table, insert.users, fetch.users, delete.users
import db_crud as db

def main():
    # 테이블 생성
    db.create_table()
    # 데이터 삽입
    db.insert_users('Alice', 30)
    db.insert_users('Bob', 25)
    db.insert_users('Chris', 35)
    # 데이터 조회
    print('-----데이터 조회 시작-----')
    users = db.fetch_users()
    for user in users:
        print(user)
    print('-----데이터 조회 끝-----')
    # 데이터 수정
    db.update_users('Alice', 25)
    # 데이터 조회
    print('-----엘리스 수정 후, 데이터 조회 시작-----')
    users = db.fetch_users()
    for user in users:
        print(user)
    print('-----데이터 조회 끝-----')
    # 데이터 삭제
    db.delete_users('Bob')
    # 데이터 조회
    print('-----밥 삭제 후, 데이터 조회 시작-----')
    users = db.fetch_users()
    for user in users:
        print(user)
    print('-----데이터 조회 끝-----')


if __name__ == "__main__":
    main()