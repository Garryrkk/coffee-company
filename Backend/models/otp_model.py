from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float
from app.extensions import db

class OTP(db.Model):
    __tablename__ = 'otp'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    otp = Column(String(10), nullable=False)
    purpose = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)
    is_used = Column(Boolean, default=False)
    is_expired = Column(Boolean, default=False)
    def __repr__(self):
        return '<OTP %r>' % self.otp