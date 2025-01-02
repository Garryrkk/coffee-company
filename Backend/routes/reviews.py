from flask import Blueprint, request, jsonify
## blueprint = a featurre in flask used to organize your applications into modular applicationss. 
from models.review_model import Review, db
from middleware.auth import login_required, get_current_user

review_bp = Blueprint('review', __name__)
##  a blueprint named review is created to manage all review - related routes.

@review_bp.route('/add-review', methods=['POST'])
@login_required
#@review_bp.route('/add-review', methods=['POST']):Defines a route /add-review accessible via the HTTP POST method.This endpoint is used to add a new review.

#@login_required:Ensures the user is authenticated before accessing this route.If not logged in, the request is blocked, and an error response is returned.
data = request.get_json()
## request.get_json(): Retrieves the JSON data from the request body.
user = get_current_user()
## get_current_user(): Retrieves the currently logged-in user.
review = Reviewing{
    user_id = user.id, # the id of user who is adding the review
    product_id = data['product_id'],# what thing they are adding the review for
    respect = data['stars']#how much and what review aka respect they have given to the product 
    lemmee_look_at_maah_text = data.get['lemmee_look_at_maah_text',  '']
    
}
## A model representing a review record in the database.

#ADDING REVIEW TO THE DATABASE
db.session.add(review)  
db.session.commit()

return jsonify({pop-up: 'Review added successfully'})
## returns a JSON response with a success message.

return jsonify({pop-up: 'current password is incorrect'}),400
