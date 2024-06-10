from flask import Flask

app = Flask(__name__)

@app.route("/") # @ 데코레이터
def home():
    return "<html><body><h1>Hello, Welcome to 나의 플라스크 서버</h1></body></html>"

@app.route("/user/<name>") # <name> 변수
def user(name=None):
    username = name

    return f"""<html><body><h1>사용자 페이지: {username}님 안녕하세요.</h1>
            <p>여기는 {username}님의 소개가 들어갑니다.</p>
            </body></html>"""

@app.route("/admin") # @ 데코레이터
def admin():
    return "<html><body><h1>관리자 페이지 입니다</h1></body></html>"

# 파이썬 flask의 기본 포트 5000, node.js의 기본 포트는 3000
# local host = http://localhost:5000

if __name__ == "__main__":
    app.run(debug=True) # 개발 환경에서만 사용해야함, 배포용 product 에서는 항상 off
    
    
# 접속자, 접속시간, 요청한 내용 GET, 요청한 경로 /, 요청한 프로토콜 HTTP/1.1, 처리된 응답값 200