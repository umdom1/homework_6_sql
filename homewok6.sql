CREATe TABLE If NOT EXISTS publisher
(
id_publisher SERIAL PRIMARY KEY,
name_publisher varchar(50) NOT NULL
);

CREATe TABLE If NOT EXISTS book
(
id_book SERIAL PRIMARY KEY,
title varchar(255) NOT NULL,
id_publisher integer REFERENCES publisher(id_publisher) NOT NULL
);
 
CREATe TABLE If NOT EXISTS shop
(
id_shop SERIAL PRIMARY KEY,
name_shop varchar(50) NOT NULL
); 
 
 
 CREATE TABLE IF NOT EXISTS stock
(
id_stock SERIAL PRIMARY KEY,
id_book integer REFERENCES book(id_book) NOT NULL,
id_shop integer REFERENCES shop(id_shop) not NULL  
);

CREATe TABLE If NOT EXISTS sale
(
id_sale SERIAL PRIMARY KEY,
price integer NOT NULL,
date_sale date NOT NULL,
quantity integer NOT NULL,
id_stock integer REFERENCES stock(id_stock) NOT NULL
); 



--INSERT

INSERT INTO book 
VALUES  (1,'Капитанская дочка',1),
	(2,'Руслан и Людмила', 1),
        	(3,'Идиот', 2),
        	(4,'Братья Карамазовы', 2),
        	(5,'Евгений Онегин ', 1);
        
INSERT INTO publisher 
VALUES  (1,'Пушкин А.С.'),
	(2,'Достоевский Ф.М.');



INSERT INTO shop
VALUES  (1,'Буквоед'),
	(2,'Книжный дом'),
	(3,'Лабиринт');
        
INSERT INTO stock 
VALUES  (1,1,1),
	(2,2,1),
	(3,1,3),
        	(4,5,2),
        	(5,3,2),
        	(6,4,1);
        

INSERT INTO sale
VALUES  (1,'600', '09-11-2022',3,1),
	(2,'500', '08-11-2022',3,2),
	(3,'580', '05-11-2022',2,3),
       	(4,'490', '02-11-2022',2,4),
        	(5,'600', '26-10-2022',2,1),
        	(6,'700', '26-10-2022',2,5),
        	(7,'750', '26-10-2022',7,6);

-- SELECT


SELECT price, date_sale, title, name_publisher, name_shop
from sale
INNER JOIN stock on sale.id_stock = stock.id_stock
INNER JOIN book ON stock.id_book = book.id_book
INNER JOIN publisher ON book.id_publisher = publisher.id_publisher
INNER JOIN shop ON stock.id_shop = shop.id_shop
WHERE name_publisher = "Пушкин А.С."



