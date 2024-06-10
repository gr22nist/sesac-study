from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {'name': 'Alice', 'age': 25, 'phone': '010-1234-5678'},
    {'name': 'Bobby', 'age': 30, 'phone': '010-3224-7898'},
    {'name': 'Chis', 'age': 35, 'phone': '010-9876-5432'}
]

@app.route('/')
def home():
    return jsonify(users)

@app.route('/search')
def search(name):
    query = request.args.get('q')
    page = request.args.get('page', default=1, type=int)
    # print(query, page)
    
    # 미션 1. users에서 query 구문이 name인 사람을 찾아서 출력
    for u in users:
        if u['name'].lower() == name.lower():
            user = u
    # 미션 2. 나이도 검색 age
    # 미션 3. 전화번호 끝 4자리 검색  phone
    
    return f"검색중: {query} on 페이지 {page}...", 200


if __name__ == "__main__":
    app.run(debug=True)
    
