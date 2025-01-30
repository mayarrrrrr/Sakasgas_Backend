from app import db, app
from models import Product

def seed_data():
    with app.app_context():

        print('Deleting existing products...')
        Product.query.delete()

        print('Creating products...')

        seller_id = 1  # Set the seller_id to 1 for all products

        MpishiOla = Product(name='Mpishi Ola', price=1300, description='Mpishi Ola gas', image_url='https://gobeba.com/wp-content/uploads/2019/03/IMG_0175-1.jpg', quantity_available=100, seller_id=seller_id)
        
        Mwanga = Product(name='Mwanga', price=1300, description='Mwanga gas', image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQU6qHYwlYh9UW_pAtSlHUYwRXMCLyct90PnA&s', quantity_available=80, seller_id=seller_id)
        
        Rahajiji = Product(name='Raha jiji', price=1300, description='Raha jiji gas', image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_ODESFsOOKYlbmOkRlExLseduwLVdZVWp3ZflY0W864vPMLuRJJIQz1SapQiBn6iDlBI&usqp=CAU', quantity_available=120, seller_id=seller_id)
        

        Hashi = Product(name='Hashi', price=1300, description='Hashi gas', image_url='https://gobeba.com/wp-content/uploads/2020/02/IMG_0190.jpg', quantity_available=110, seller_id=seller_id)
        
        Topgas = Product(name='Top gas', price=1300, description='Top gas', image_url='https://sokopema.com/wp-content/uploads/2024/10/131.png', quantity_available=95, seller_id=seller_id)
        
        NationalOil = Product(name='National Oil', price=1300, description='National Oil gas', image_url='https://mamagas.co.ke/wp-content/uploads/2022/10/national-300x225.jpeg ', quantity_available=125, seller_id=seller_id)
        
        Afrigas = Product(name='Afri gas', price=1300, description='Afri gas', image_url='https://gobeba.com/wp-content/uploads/2019/03/IMG_0170.jpg', quantity_available=95, seller_id=seller_id)

       
        products = [MpishiOla,Mwanga,Rahajiji,Hashi,Topgas,NationalOil,Afrigas]

        db.session.add_all(products)
        db.session.commit()

        print('Successfully created products')

if __name__ == '__main__':
    seed_data()
