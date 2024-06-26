from flask import Flask, render_template
import csv
import math

app = Flask(__name__)

csv_data = []

def load_csv_data(filename):
    with open(filename, newline='', encoding='utf8') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            csv_data.append(row)

@app.route('/')
@app.route('/<int:page>')
def index(page=1):
    per_page = 10 # 한 페이지에 보여줄 항목 수

    start_index = (page - 1) * per_page
    end_index = page * per_page

    headers = csv_data[0]
    print(headers)

    total_pages = math.ceil(len(csv_data) / per_page)

    current_pages = csv_data[start_index:end_index]

    return render_template('index.html', headers=headers, users=current_pages, total_pages=total_pages)


if __name__ == '__main__':
    load_csv_data('./user.csv')
    # print(csv_data)
    app.run(debug=True)

# 1. 이 파일에 flask 기본 틀을 추가한다.
# 2. / 에 접속 시 이 사용자의 데이터를 보여준다.