from flask import Blueprint, request, jsonify
from models.user_model import User
import jwt
from datetime import datetime, timedelta

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods = ['POST'])
def login():
    data =request.get_json()_by(email = data['email']).first()
    if user and user.check_password(data['password']):
        if not user.is verified:
            return jsonify({'message': 'Email not verified'}), 401
        
        
        token = jwt.encode(
            {'user_id': user.id, 'exp': datetime.utcnow() + timedelta(minutes=30)},
            'your-secret-key'
            algorithm = 'HS256'
        )
        
        return jsonify({'token': token})
    return jsonify({'token':token})
return jsonify({'error': 'Invalid credentials'}), 401                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          