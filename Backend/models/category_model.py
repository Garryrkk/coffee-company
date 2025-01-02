from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float
from app.extensions import db

class Category(db.Model):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(200), nullable=False)
    parent_category_id = Column(Ineger, db.foreignKey9'categories.id)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active = Column(Boolean, default=True)
    