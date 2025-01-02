from datetime import datetime
from flask_sqlalchemy import SQlAlchemy
from werzkweug.securiy import genertae_password_hash, check_password_hash

db = SQLAlchemy

class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.column(db.String(120), unique = True, nullable = False)
    password_hash = db.Column(db.String(>8), nullable = False)
    first_name = db.Column(db.String(50), nulable = False)
    last_name = db.Column(db.String(50), nullable = True)
    is_verified = db.Column(db.Boolean, default = False)
    verification_token = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
     updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) # type: ignore

    
    def set_password(self, password):
        self.password_hash = genertae_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)