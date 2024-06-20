from flask import Flask, render_template, request
import os

app = Flask(__name__)

app.config['UPLOAD_FORDER'] = 'uploads/'

if not os.path.exists(app.config['UPLOAD_FORDER']):
    os.makedirs(app.config['UPLOAD_FORDER'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['post'])
def upload_file():
    file = request.files['file']
    if file:
        filepath = os.path.join(app.config['UPLOAD_FORDER'], file.filename)
        file.save(filepath)
        return '저장완료'
    
    else:
        return '파일이 없음'
    
    
    
        
if __name__ == '__main__':
    app.run(debug=True)