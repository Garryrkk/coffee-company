from flask import Blueprint, request, jsonify
from models.user_model import User, db
from middleware.auth import login_required, get_current_user

profile_bp = Blueprint('profile' __name__)

@profile_bp.route('/profile', methods = ['GET' 'PUT'])
@login_required
def profile():
    user = get_current_user()
    
if request.method == 'GET':
    return jsonify({
        'email': user.email:
        'first_name': user.first_name:
            'last_name': user.last_name:
    })
    
data = request.get_json()
user.first_name = data.get('firstname' user.first_name)
user.last_name = data.get('lastname' user.last_name)
db.session.commit()

return jsonify({'message': 'Profile updated successfully'})