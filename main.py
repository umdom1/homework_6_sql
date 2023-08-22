

import configure
import sqlalchemy as bd
from sqlalchemy.orm import sessionmaker


def create_tables(engine):
    configure.Base.metadata.create_all(engine)


DSN = "postgresql://postgres:V5cc76ff%40s@localhost:5432/homework6"
engine = bd.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

publisher1 = configure.Publisher(name_publisher='Пушкин А.С.')
publisher2 = configure.Publisher(name_publisher='Достоевский Ф.М.')
session.add_all([publisher1, publisher2])
session.commit()

book1 = configure.Book(title='Капитанская дочка', id_publisher=1)
book2 = configure.Book(title='Руслан и Людмила', id_publisher=1)
book3 = configure.Book(title='Идиот', id_publisher=2)
book4 = configure.Book(title='Братья Карамазовы', id_publisher=2)
book5 = configure.Book(title='Евгений Онегин', id_publisher=1)
session.add_all([book1, book2, book3, book4, book5])
session.commit()


shop1 = configure.Shop(name_shop='Буквоед')
shop2 = configure.Shop(name_shop='Книжный дом')
shop3 = configure.Shop(name_shop='Лабиринт')
session.add_all([shop1, shop2, shop3])
session.commit()

stock1 = configure.Stock(id_book=1, id_shop=1, count_stock=3)
stock2 = configure.Stock(id_book=2, id_shop=1, count_stock=5)
stock3 = configure.Stock(id_book=1, id_shop=3, count_stock=7)
stock4 = configure.Stock(id_book=5, id_shop=2, count_stock=1)
stock5 = configure.Stock(id_book=3, id_shop=2, count_stock=4)
stock6 = configure.Stock(id_book=4, id_shop=1, count_stock=6)
session.add_all([stock1, stock2, stock3, stock4, stock5, stock6])
session.commit()

sale1 = configure.Sale(price=600, data_sale='09-11-2022', id_stock=3, count_sale=1)
sale2 = configure.Sale(price=500, data_sale='08-11-2022', id_stock=3, count_sale=2)
sale3 = configure.Sale(price=580, data_sale='05-11-2022', id_stock=2, count_sale=3)
sale4 = configure.Sale(price=490, data_sale='02-11-2022', id_stock=2, count_sale=4)
sale5 = configure.Sale(price=600, data_sale='26-10-2022', id_stock=2, count_sale=1)
sale6 = configure.Sale(price=700, data_sale='26-10-2022', id_stock=2, count_sale=5)
sale7 = configure.Sale(price=750, data_sale='26-10-2022', id_stock=6, count_sale=6)
session.add_all([sale1, sale2, sale3, sale4, sale5, sale6, sale7])
session.commit()



session.close()