from flask import Blueprint, jsonify
from models.user_model import User, db
import jwt

verify_bp = Blueprint('verify', __name__)
@verify_bp.route('/verify-email/<token>', methods=['GET'])
def verify_email(token):
    try:
        payload = jwt.decode(token, 'your-secret-key', algorithms=['HSA256'])
        user = User.query.filter_by(id=payload['user_id']).first()
        
        if user and user.verification_token ==  token:
            user.is_verified = True
            user.verification_token = None
            db.session.commit()
            return jsonify({'message': 'Email verified successfully'}), 200
        
        return jsonify({'message': 'Email verified successfully'})
    
    return jsonify({'error': Invalid verifucation token}), 400
except jwt.ExpiredSignatureError:
    return jsonify({'error': 'Verification token has expired'}), 400