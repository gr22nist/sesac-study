from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {'name': 'Alice', 'age': 25, 'phone': '010-1234-5678'},
    {'name': 'Alice', 'age': 30, 'phone': '010-7423-5457'},
    {'name': 'Bobby', 'age': 30, 'phone': '010-3224-7898'},
    {'name': 'Chris', 'age': 35, 'phone': '010-9876-5678'}
]

@app.route('/')
def home():
    return jsonify(users)

@app.route('/search')
def search():
    
    name_query = request.args.get('name')
    print(name_query)
    age_query = request.args.get('age')
    phone_query = request.args.get('phone')
    result = users
    # 위의 user 안에 이 user가 있는지 찾아서 있으면 해당 사용자를 반납
    # for u in users:
    #     if u['name'].lower() == name_query.lower():
    #         users = u

    # 미션 1. users에서 query 구문이 name인 사람을 찾아서 출력
    if name_query:
        result = [u for u in users if name_query.lower() in u['name'].lower()]
    
        return jsonify(result)
    # 미션 2. 나이도 검색 age
    # if age_query:
    #     try:
    #         age_query = int(age_query)
    #         result = [u for u in result if age_query == u['age']]
    #     except ValueError:
    #         return jsonify({'error': 'Age parameter must be integer'}), 400
    
    # 미션 3. 전화번호 끝 4자리 검색 phone
    
    if phone_query:
        result = [u for u in result if phone_query == u['phone'][-4:]]
    
    if result:
        return jsonify(result)
    else:
        return jsonify({'error': 'Not found users'}), 404
    # 결과 값이 있을때는 지금처럼 응답과 200을 보내고
    # 결과 값이 없을때는 응답값에 404를 보낸다.

if __name__ == "__main__":
    app.run(debug=True)
    
