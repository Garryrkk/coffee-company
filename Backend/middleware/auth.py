from functools import wrap
from flask import request, jsonify
import jwt
from models.user_model import user


# decorator function
def login_required(f)
# f : the function the decorator is applied to, adds auth logic to the req function
@wraps(f)
#ensures the decorated func retains it's original name and metadata 
def decorated_function(*args, **kwargs):
    # a arapper function thst executes the logic for verifying the user token
    token = request.headers.get('Authorization')
#request.headers.get():Retrieves the Authorization header from the HTTP request.The token is expected to be passed as a Bearer Token in this header.

if not token
return jsonify ({error: no token provides}) 401
#if the token is found in the reques headers return a json response with an error message
# 401 is the HTTP status code for Unauthorized

payload = jwt.decode(toke, 'your secret key' algorithms = ['HS256'])
# jwt.decode: decodes using the secret key and the specified algo
# payload: extracts the payload which typicall contains the user specific data

current_user = User.query.get(payload['user_id'])
if not current_user:
return jsonify ({error: invalid token}) 401
#uses sqlalchemy's query.get to fetch the user with the id from the decoded taken payload
# if the user is not found return a json response with an error message
except jwt.ExpiredSignatureError:
    return jsonify({'error': 'Token has expired'}), 401
except jwt.InvalidTokenError:
    return jsonify({'error': 'Invalid token'}), 401
return f(*args, **kwargs)
return decorated_function
def get_current_user():
    token = request.headers.get('Authorization')
    payload = jwt.decode(token, 'your-secret-key', algorithms=['HS256'])
    return User.query.get(payload['user_id'])