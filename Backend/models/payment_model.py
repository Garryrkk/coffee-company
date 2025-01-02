from datetime import datetime
from . import db

class Pyment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.column(db.integer, db.ForeignKey('user.id'), nullable = False)
    amount = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.String(50))
    transaction_id = db.Column(db.String(100))
    status = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
