from olo import db
from olo import ProductModel

db.create_all()

product_1 = ProductModel(name='Produto Um', description='Uma descrição')
db.session.add(product_1)
db.session.commit()