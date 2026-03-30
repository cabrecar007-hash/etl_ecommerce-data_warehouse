-- user_logs table
CREATE TABLE user_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    action_type ENUM('login','logout','view','buy','add_to_cart') NOT NULL,
    datetime DATETIME NOT NULL,
    product_id INT NULL,
    amount DECIMAL(10,2) DEFAULT 0
);

-- user_info table
CREATE TABLE user_info (
    user_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    signup_date DATETIME,
    country VARCHAR(50)
);

-- products table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2)
);

-- orders table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    product_id INT,
    quantity INT,
    total_amount DECIMAL(10,2),
    order_date DATETIME
);
