from flask import Blueprint, request, jsonify

order_bp = Blueprint('order', __name__)

@order_bp.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    # Add logic to create an order
    return jsonify({"message": "Order created successfully"}), 201

@order_bp.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    # Add logic to fetch an order by ID
    return jsonify({"order": {}})

@order_bp.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    # Add logic to delete an order
    return jsonify({"message": "Order deleted successfully"})
