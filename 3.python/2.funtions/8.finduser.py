users = [   # 딕셔너리 리스트
    {"name": "Alice", "age": 25, "location": "Seoul", "car": "BMW"},
    {"name": "Bob", "age": 30, "location": "Busan", "car": "Mercedes"},
    {"name": "Charlie", "age": 35, "location": "Daegu", "car": "Audi"},
]

# print(users)

def find_user(name):
    #입력 받은 사용자 정보를 출력하시오
    # first_user = user[0]

    for u in users:
        # print(u['name'])
        if u['name'] == name:
            print(u)
            return(u)
        
        else print('찾는 사용자가 없습니다')
                
find_user('alice')