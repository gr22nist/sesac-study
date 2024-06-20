from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user')
def query_params():
    
    name = request.args.get('name') # 인자가 있는지 물음
    age = request.args.get('age', 0) 
    # name = request.args['name'] # 인자를 무조건 달라고 함
    
    return f"이름: {name}, 나이: {age}"

@app.route('/user_json', methods=['get', 'post', 'delete'])
def json_parse():
    data = request.json
    print(data)
    return data

@app.route('/user', methods=['post'])
def form_params():
    
    name = request.form.get('name') # 인자가 있는지 물음
    age = request.form.get('age', 0) 
    # name = request.form['name'] # 인자를 무조건 달라고 함
    
    return f"이름: {name}, 나이: {age}"




if __name__ == '__main__':
    app.run(debug=True)