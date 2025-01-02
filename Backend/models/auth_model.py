from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float
from app.extensions import db

class AuthToken(db.model): #declares a pyton class name suthtoken in the context of sql achemy it represents a table in the database
# db.model: indicates this class inherits from dm.Model, which is the base class for all the models on flask sqlalchemy
__tablename__ = 'auth_tokens'
# __tablename__: specifies the name of the table in the database
id = Column(Integer, primary_key=True)
#id: a unique identifier for each token
#
# primary-key = True make this columns as the primary key meaning each record is the table must have aunque id

user_id = Column(Integer, db.ForeignKey('users.id'), nullable = False)
#user_id = stres the id of the user associated with this column
#auth_tokens = table to the id column i the users table

token = Column(String(500), nullable=False)
expires_at = Column(Datetime, nullable = False)
is_active = Column(Boolean, default = True)
created_at = Column(DateTime, default=datetime.utcnow) 





