from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, User
import os

app = Flask(__name__)

DATABASE_NAME = 'example.db'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DATABASE_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

# 해당 모듈을 불러온 후에 초기화 함수를 통해 db = flask 연결
db.init_app(app)


@app.route('/')
def index():
    users = User.query.all()
    print(users)
    return render_template('index.html', users=users)

@app.route('/add_user', methods=['post'])
def add_user():
    # name = request.args.get('name')
    # age = request.args.get('age')
    # post 방식: body 안에 데이터가 담겨온다
    name = request.form.get('name')
    age = request.form.get('age')
    print(f'입력값은 {name}, {age}')
    
    new_user = User(name=name, age=int(age))
    
    if int(age) < 0:
        flash('나이는 음수일 수 없습니다')
        return redirect(url_for('index'))
    
    if int(age) > 100:
        flash('나이는 100살 이상일 수 없습니다')
        return redirect(url_for('index'))
        
    db.session.add(new_user)
    db.session.commit()
    flash(f'사용자({name})가 추가 되었습니다')
        
    return redirect(url_for('index'))

@app.route('/delete_user/<id>')
def delete_user(id):
    print(f"삭제할 사용자 아이디는 {id}")
    
    user = db.session.get(User, id)
    
    if user:
        db.session.delete(user)
        db.session.commit()
        print(f"사용자 {user.name} 삭제 완료 ")
        flash(f'사용자({user.name})가 삭제 되었습니다')
    
    else:
        print(f"사용자가 없습니다")
        flash(f'사용자가 없습니다')    
    return redirect(url_for('index'))

@app.route('/edit_user/<id>')
def edit_user(id):
    print(f"수정할 사용자 아이디는 {id}")
    
    user = db.session.get(User, id)
    
    return render_template('edit_user.html', user=user)

@app.route('/update_user/<id>', methods=['post'])
def update_user(id):

    user = db.session.get(User, id)
    
    name = request.form.get('name')
    age = request.form.get('age')
    
    user.name = name
    user.age = int(age)
    
    if int(age) < 0:
        flash('나이는 음수일 수 없습니다')
        return redirect(url_for('edit_user', id=id))

    if int(age) > 100:
        flash('나이는 100살 이상일 수 없습니다')
        return redirect(url_for('edit_user', id=id))
       
    if not name or not age:
        flash(f'이름과 나이는 빈 칸 일 수 없습니다')
        
        return redirect(url_for('edit_user', id=id))
    
    db.session.commit()
        
    return redirect(url_for('index'))

if __name__ == "__main__":
    with app.app_context():
        db_path = os.path.join(app.instance_path, DATABASE_NAME)
        if not os.path.exists(db_path):       
            db.create_all()
            print('DB에 없음, 추가중')
            
        if not User.query.first():
            print('사용자가 없음, 추가 바람')
        
            user1 = User(name='Alice', age=30)
            user2 = User(name='Bobbu', age=33)
            user3 = User(name='Chris', age=35)
        
            db.session.add(user1) # db와 통신하는 방식을 session 으로 정함
            db.session.add(user2) 
            db.session.add(user3)
            db.session.commit()
        
    app.run(debug=True)
    