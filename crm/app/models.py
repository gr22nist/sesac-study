from . import db

class User(db.Model):
    Id = db.Column(db.Text, primary_key=True)
    Name = db.Column(db.Text, nullable=False)
    Gender = db.Column(db.Text, nullable=False)
    Birthdate = db.Column(db.Text, nullable=False)
    Age = db.Column(db.Integer, nullable=False)
    Address = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return f"<User {self.Name}>"

class Store(db.Model):
    Id = db.Column(db.Text, primary_key=True)
    Name = db.Column(db.Text, nullable=False)
    Type = db.Column(db.Text, nullable=False)
    Address = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return f"<Store {self.Name}>"

class Item(db.Model):
    Id = db.Column(db.Text, primary_key=True)
    Type = db.Column(db.Text, nullable=False)
    Name = db.Column(db.Text, nullable=False)
    UnitPrice = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f"<Item {self.Name}>"

class Order(db.Model):
    Id = db.Column(db.Text, primary_key=True)
    OrderAt = db.Column(db.DateTime, nullable=False)
    StoreId = db.Column(db.Text, db.ForeignKey('store.Id'), nullable=False)
    UserId = db.Column(db.Text, db.ForeignKey('user.Id'), nullable=False)
    store = db.relationship('Store', backref=db.backref('orders'))
    user = db.relationship('User', backref=db.backref('orders'))
    #양방향 참조 설정 backref
    
    def __repr__(self):
        return f"<Order {self.Id}>"

class OrderItem(db.Model):
    Id = db.Column(db.Text, primary_key=True)
    OrderId = db.Column(db.Text, db.ForeignKey('order.Id'), nullable=False)
    ItemId = db.Column(db.Text, db.ForeignKey('item.Id'), nullable=False)
    order = db.relationship('Order', backref=db.backref('order_items'))
    item = db.relationship('Item', backref=db.backref('order_items'))
    
    def __repr__(self):
        return f"<OrderItem {self.Id}>"