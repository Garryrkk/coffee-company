from flask import Blueprint, request, jsonify
# a blueprint is a system that provides a structural approach to organizing and managing components of a system
#The Auth Blueprint manages routes for login, logout, and password reset.The Product Blueprint handles product listing, details, and cart functionality.
from models.user_model import User
from middleware.auth import login_required, get_current_user

#### DEFINING THE ROUTE #####

update_bp = Blueprint('update'__name__)
@update_bp.route('/change-password', methods=['POST']) #creates an endpoint Post/change password
#post method indicateds that the route is for sending data to the server not tretrieving it
@login_required #ensures only looged in users can access this rourte, if a users is't authenticated it returns an error before accessing the func

def change_password():
#This function handles the logic for updating the password.

data = request.get_json()
user = get_current_user()# retrieves the user object of currently authenticated user 
#Likely implemented in the auth middleware, possibly by decoding a token.

if user.check_password(data['current_password']):
    user.set_password(data['new_password'])
db.session.commit()
#Saves the changes (updated password) to the database permanently.
return jsonify({'message': 'Password changed successfully'})
return jsonify({'error': 'Current password is incorrect'}), 400



