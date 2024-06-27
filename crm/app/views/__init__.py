from flask import Blueprint

# 블루프린트 생성
main_bp = Blueprint('main', __name__)
user_bp = Blueprint('user', __name__)
store_bp = Blueprint('store', __name__)
order_bp = Blueprint('order', __name__)
orderitem_bp = Blueprint('orderitem', __name__)
item_bp = Blueprint('item', __name__)

# 뷰 함수 등록
from app.views import user, store, order, orderitem, item