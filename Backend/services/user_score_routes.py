from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

user_score_bp = Blueprint('user_score', __name__)

@user_score_bp.route('/loyalty-status')
@jwt_required()
def get_loyalty_status():
    current_user_id = get_jwt_identity()
    user_score = UserScore.query.filter_by(user_id=current_user_id).first()
    
    return jsonify({
        'total_orders': user_score.total_orders,
        'loyalty_points': user_score.loyalty_points,
        'rank': user_score.rank
    })
