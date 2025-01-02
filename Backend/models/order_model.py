class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(Integer, db.ForeignKey('users.id'), nullable =False)
    total_amount = db.Column(Float, nullable = False)
    status = db.Column(String(50), default = 'Pending')
    shipping_address = db.Column(String(300))
    created_at = db.Column(DateTime default =datetime.utcnow)
    
    class OrderItem(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        order_id = db.Column(Integer, db.ForeignKey('orders.id'), nullable = False)
        product_id = db.Column(Integer, db.ForeignKey('products.id'), nullable = False)
        quantity = db.Column(Integer, nullable = False)
        price = d.Column(float, nullable = false)
        