from app import db, app
from models import Product

def seed_data():
    with app.app_context():

        print('Deleting existing products...')
        Product.query.delete()

        print('Creating products...')

        seller_id = 1  # Set the seller_id to 1 for all products

        bread = Product(name='long bread', price=120, description='hot-dog buns', image_url='https://staticcookist.akamaized.net/wp-content/uploads/sites/22/2022/06/hot-dog-buns.jpeg', quantity_available=100, seller_id=seller_id)
        bread1 = Product(name='Round bread ', price=120, description='warm round bread', image_url='https://i.pinimg.com/564x/f1/6c/96/f16c96dce096b4d93841d977dcf29771.jpg', quantity_available=80, seller_id=seller_id)
        cake = Product(name='Cakes', price=699, description='freshly baked caked', image_url='https://i.pinimg.com/564x/d4/dc/ed/d4dced1af80b34bcd85313bab51a4202.jpg', quantity_available=120, seller_id=seller_id)
        

        Foul = Product(name='Beans(Foul)', price=500, description='Fava Beans', image_url='https://i.pinimg.com/564x/1d/67/7d/1d677d1f130a9b93b2ee2810a23544cc.jpg', quantity_available=110, seller_id=seller_id)
        Peanut = Product(name='Peanut', price=1000, description='Smooth homemade peanut butter', image_url='https://i.pinimg.com/564x/95/8a/29/958a2983e1761003acf6fb8ee58ab336.jpg', quantity_available=95, seller_id=seller_id)
        Custard = Product(name='Custard', price=1299, description='Zesta custard powder', image_url='https://www.topserveltd.co.ke/_next/image?url=https%3A%2F%2Fapp.topserveltd.co.ke%2Fimage%2Fcatalog%2Fproducts%2FZESTA-CUSTARD-POWDER-250G.jpg&w=1200&q=75 ', quantity_available=125, seller_id=seller_id)
        laptop4 = Product(name='Lenovo ThinkPad X1 Carbon', price=1399, description='Lenovo ThinkPad X1 Carbon Gen 9, Intel Core i5, 256GB SSD', image_url='https://i.pinimg.com/564x/d7/10/f1/d710f17efbfcaa72651a2c6930c5e0ad.jpg', quantity_available=105, seller_id=seller_id)
        
        Macaroni = Product(name='Macaroni', price=800, description='Macaroni', image_url='https://i.pinimg.com/564x/a0/52/ad/a052ad03995f0e5ef18775ce18f19503.jpg', quantity_available=95, seller_id=seller_id)

       
        products = [bread,bread1,cake,Foul,Peanut,Custard,Macaroni]

        db.session.add_all(products)
        db.session.commit()

        print('Successfully created products')

if __name__ == '__main__':
    seed_data()
