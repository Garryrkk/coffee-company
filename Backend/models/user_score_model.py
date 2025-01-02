from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float
from app.extensions import db

class Userscore(db.Model):
    __tablename__ = 'userscore'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    total_orders = Column(Integer, default=0)
    total_points = Column(Integer, default=0)
    total_spent = Column(Integer, default = 0)
    loyalty_points = Column(Integer, default = 0)
    score = Column(Integer)
    