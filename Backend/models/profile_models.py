from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float # type: ignore
from app.extensions import db # type: ignore

class UserProfile(db.Model):
    __tablename__ = 'user_profiles'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id')) # type: ignore
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone_number = Column(String(20), nullable=False)
    address = Column(String(200), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    profile_picture = Column(String(255))