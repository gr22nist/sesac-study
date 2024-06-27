from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 데이터베이스 객체 생성
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # 애플리케이션 설정
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crm.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 확장 초기화
    db.init_app(app)

    # 블루프린트 등록
    from app.views import user_bp, store_bp, order_bp, orderitem_bp, item_bp
    app.register_blueprint(user_bp, url_prefix='/users')
    app.register_blueprint(store_bp, url_prefix='/stores')
    app.register_blueprint(order_bp, url_prefix='/orders')
    app.register_blueprint(orderitem_bp, url_prefix='/orderitems')
    app.register_blueprint(item_bp, url_prefix='/items')

    return app

# 모델을 가져와야 db가 작동함
from app import models