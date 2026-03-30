def transform_user_logs(user_logs, store_id):
    transformed = []
    for row in user_logs:
        transformed.append({
            'store_id': store_id,
            'user_id': row['user_id'],
            'action_type': row['action_type'],
            'product_id': row.get('product_id'),
            'amount': row.get('amount', 0),
            'datetime': row['datetime']
        })
    return transformed

def transform_users(user_info):
    transformed = []
    for row in user_info:
        transformed.append({
            'user_id': row['user_id'],
            'name': row['name'],
            'email': row['email'],
            'signup_date': row['signup_date'].date(),
            'country': row['country']
        })
    return transformed

def transform_products(products):
    transformed = []
    for row in products:
        transformed.append({
            'product_id': row['product_id'],
            'name': row['name'],
            'category': row['category'],
            'price': row['price']
        })
    return transformed
