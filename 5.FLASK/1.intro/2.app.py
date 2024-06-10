from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello!"

@app.route('/user/<name>') # 기본값은 str으로 처리함
def user(name):
    return f"<h1>Hello, {name}님!</h1>"

@app.route('/user/<int:age>')
def userage(age):
    return f"<h1>Age: {age}</h1>"

@app.route('/user/<float:weight>')
def userweight(weight):
    return f"<h1>weight: {weight}</h1>"

@app.route('/user/<name>/<age>/<weight>')
def usernameageweight(name, age, weight):
    return f"<h1>Hello, {name}님, Age: {age}, weight: {weight}</h1>"

if __name__ == "__main__":
    app.run(debug=True)