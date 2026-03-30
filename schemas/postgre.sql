--- fact table 

CREATE TABLE fact_user_activity (
    activity_id BIGSERIAL PRIMARY KEY,
    store_id INT,
    user_id INT,
    action_type VARCHAR(20),
    product_id INT,
    amount NUMERIC(10,2),
    datetime TIMESTAMP
);


--- dimension table

CREATE TABLE dim_user (
    user_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    signup_date DATE,
    country VARCHAR(50)
);

CREATE TABLE dim_product (
    product_id INT PRIMARY KEY,
    name VARCHAR(100),
    category VARCHAR(50),
    price NUMERIC(10,2)
);

CREATE TABLE dim_store (
    store_id INT PRIMARY KEY,
    store_name VARCHAR(100)
);

CREATE TABLE dim_action (
    action_type VARCHAR(20) PRIMARY KEY
);
