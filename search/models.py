from app import db

class Product(db.Model):
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    code = db.Column(db.String(20), unique=True)
    price_nkim = db.Column(db.String(20))
    price_tiki = db.Column(db.String(20))