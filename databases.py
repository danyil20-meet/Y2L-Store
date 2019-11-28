from model import Base, Product, Cart


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(name, price, link, description):
    new_product = Product(
        name = name,
        price = price,
        pictureLink = link,
        description = description)

    session.add(new_product)
    session.commit()

def query_by_id(product_id):
    return session.query(Product).filter_by(id = product.id)

def edit_by_id(product_id, name, price, link, description):
    product_object = session.query(Product).filter_by(id = product_id)

    product_object.name = name
    product_object.price = price
    product_object.pictureLink = link
    product_object.description = description

    session.commit()

def delete_by_id(product_id):
    product_object = session.query(Product).filter_by(id = product_id).delete()
    session.commit()

def query_all():
   return session.query(Product).all()


def add_to_cart(productID):
    new_cart = Cart(
        productID = productID)

    session.add(new_cart)
    session.commit()
    
add_product("Name", 000, "https://bit.ly/33apKy6", "Some Description")
products = session.query(Product).all()



    
    
