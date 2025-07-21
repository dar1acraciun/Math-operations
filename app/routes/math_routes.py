from flask import Blueprint, request, jsonify
from controller import math_controller

math_bp = Blueprint("math", __name__)

@math_bp.route('/pow', methods=['POST'])
def pow_endpoint():
    data = request.get_json()
    base = data.get("base")
    exponent = data.get("exponent")

    if base is None or exponent is None:
        return jsonify({"error": "Missing base or exponent"}), 400

    result = math_controller.power(base, exponent)
    return jsonify({"result": result})
