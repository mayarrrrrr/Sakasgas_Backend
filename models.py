from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin


db= SQLAlchemy()

class User(db.Model, SerializerMixin):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String, nullable=False)  # 'admin/shop' or 'client/customer'

    products = db.relationship('Product', backref='seller', lazy=True, cascade="all, delete-orphan")
    orders = db.relationship('Order', backref='user', lazy=True, cascade="all, delete-orphan")

    serialize_rules = ('-order.user', '-order.product',)


    @validates('password')
    def validate_password(self, key, password):
        if len(password) < 8:
            raise ValueError('Password must be more than 8 characters.')
        return password
    
    @validates('email')
    def validate_email(self, key, email):
        if not email.endswith("@gmail.com"):
            raise ValueError("Email is not valid. It should end with @gmail.com")
        return email


    def __repr__(self):
        return f'<User {self.email} of role {self.role}>'


class Product(db.Model, SerializerMixin):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String, nullable=False)
    quantity_available = db.Column(db.Integer, nullable=False)

    seller_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    orders = db.relationship('OrderItem', backref='product', lazy=True, cascade="all, delete-orphan")

    serialize_rules = ('-orders.product', '-orders.user',)

    def __repr__(self):
        return f'<Product {self.name} from seller {self.seller_id}>'


class Order(db.Model, SerializerMixin):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String, nullable=False)  # e.g., 'pending', 'shipped', 'delivered'

    order_items = db.relationship('OrderItem', backref='order', lazy=True, cascade="all, delete-orphan")

    #serialize_rules = ('-user.orders', '-product.orders',)

    def __repr__(self):
        return f'<Order {self.id}>'


class OrderItem(db.Model, SerializerMixin):

    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)

    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

    #serialize_rules = ('-order.order_items', '-product.orders',)

    def __repr__(self):
        return f'<OrderItem {self.id}>'
    

