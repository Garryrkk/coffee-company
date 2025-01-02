from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user_model import User
# Import other models here

def init_models(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
