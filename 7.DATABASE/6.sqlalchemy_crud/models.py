from flask_sqlalchemy import SQLAlchemy
# from app import app


db = SQLAlchemy()

# 클래스를 통한 db 설정

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=True)
    
    def __repr__(self):
        return f'사용자: {self.name}'