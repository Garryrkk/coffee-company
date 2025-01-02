from flask import Blueprint, request, jsonify
from models.user_model import User, db
from services.email_service import send_reset_email

reset_bp = Blueprint('reset', __name__)

@reset_bp.route('/forgot-password', methods=['POST'])
def forgot_password():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    
    if user:
        reset_token = create_reset_token(user)
        user.reset_token = reset_token
        db.session.commit()
        send_reset_emal(user, email, reset_token)
        
    return jsonify({'message': 'if account exists reset email sent'})

@reset_bp.route('/reset-password/<token>', methods =['Post'])
def reset_password(token):
try:
    data = request.get_json()
    payload = jwt.ecole(token, 'your-secret-key', algorithms=['HS256']) # type: ignore
    user = User.query.filter_by(id=payload['user_id']).first()
        
if user and user.reset_token == token:
        user.set_password(data['new_password'])
        user.reset_token = None
        db.session.commit()
return jsonify = ({'error: Invalid reset token'}). 400

except jwt.ExpiredSignatureError:
    
return jsonify({'error: Token has expired'}). 400
    
        