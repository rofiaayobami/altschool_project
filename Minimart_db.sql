CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT
);

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name TEXT,
    price NUMERIC
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    product_id INT REFERENCES products(product_id),
    quantity INT,
    order_date TIMESTAMP DEFAULT NOW()
);

ALTER TABLE products ADD COLUMN stock INT DEFAULT 0;


INSERT INTO customers (name, email) VALUES ('mubby', 'mubby@yahoo.com'), ('john', 'john@gmail.com'), ('rofiat', 'rofiat@yahoo.com'), ('aishat', 'aishat@gmail.com'), ('rodiat', 'rodiat@gamil.com');

INSERT INTO products (name, price) VALUES ('bodyspray', 12.5), ('Notebook', 5.0), ('nivea', 30.5), ('waterbottle', 15.0), ('chivita', 10.0);

INSERT INTO orders (customer_id, product_id, quantity) VALUES (1, 1, 4), (2, 2, 3),(3, 3, 1), (4, 4, 2), (5, 5, 3) ;


SELECT * 	
From orders as o 
join customers as c on o.customer_id = c.customer_id
join products as p on o.product_id = p.product_id
where c.name = 'rofiat';

SELECT COUNT(*) FROM orders;

SELECT SUM(p.price * o.quantity) AS total_revenue
FROM orders 
JOIN products as p ON o.product_id = p.product_id;

SELECT o.order_id, c.name AS customer, p.name AS product, o.quantity
FROM orders as o 
INNER JOIN customers as c ON o.customer_id = c.customer_id
INNER JOIN products as p ON o.product_id = p.product_id;

SELECT p.name AS product, o.order_id, o.quantity
FROM products as p
LEFT JOIN orders as o ON p.product_id = o.product_id;




