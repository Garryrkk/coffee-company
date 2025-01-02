from flask import Blueprint, request, jsonify
from backend.models.user_model import User, db
from backend.utils.validators import validate_email, validate_password
from werkzeug.security import generate_password_hash

signup_bp = Blueprint('signup', __name__)

@signup_bp.route('/signup', methods=['POST'])
def signup():
    try:
        data = request.get_json()
        
        # Extract user data
        email = data.get('email')
        password = data.get('password')
        name = data.get('name')
        
        # Validate input
        if not all([email, password, name]):
            return jsonify({'error': 'All fields are required'}), 400
            
        # Check if email is valid
        if not validate_email(email):
            return jsonify({'error': 'Invalid email format'}), 400
            
        # Check if user already exists
        if User.query.filter_by(email=email).first():
            return jsonify({'error': 'Email already registered'}), 409
            
        # Create new user
        new_user = User(
            email=email,
            name=name,
            password=generate_password_hash(password)
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({
            'message': 'User registered successfully',
            'user_id': new_user.id
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500