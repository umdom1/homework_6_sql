import sqlalchemy as bd
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()


class Publisher(Base):
    __tablename__ = "publisher"

    id_publisher = bd.Column(bd.Integer, primary_key=True)
    name_publisher = bd.Column(bd.String(40), nullable=False)


class Book(Base):
    __tablename__ = "book"

    id_book = bd.Column(bd.Integer, primary_key=True)
    title = bd.Column(bd.Text, nullable=False)
    id_publisher = bd.Column(bd.Integer, bd.ForeignKey('publisher.id_publisher'), nullable=False)

    publisher = relationship(Publisher, backref='book')


class Shop(Base):
    __tablename__ = "shop"

    id_shop = bd.Column(bd.Integer, primary_key=True)
    name_shop = bd.Column(bd.String(40), nullable=False)


class Stock(Base):
    __tablename__ = "stock"

    id_stock = bd.Column(bd.Integer, primary_key=True)
    id_book = bd.Column(bd.Integer, bd.ForeignKey('book.id_book'), nullable=False)
    id_shop = bd.Column(bd.Integer, bd.ForeignKey('shop.id_shop'), nullable=False)
    count_stock = bd.Column(bd.Integer, nullable=False)

    stock_1 = relationship(Book, backref='book')
    stock_2 = relationship(Shop, backref='shop')


class Sale(Base):
    __tablename__ = "sale"

    id_sale = bd.Column(bd.Integer, primary_key=True)
    price = bd.Column(bd.Integer, nullable=False)
    data_sale = bd.Column(bd.Date, nullable=False)
    id_stock = bd.Column(bd.Integer, bd.ForeignKey('stock.id_stock'), nullable=False)
    count_sale = bd.Column(bd.Integer, nullable=False)

    sale_1 = relationship(Stock, backref='stock')