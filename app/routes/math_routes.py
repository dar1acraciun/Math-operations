from flask import Blueprint, request, jsonify
from controller import math_controller

math_bp = Blueprint('math_bp', __name__)

@math_bp.route('/power', methods=['POST'])
def power():
    data = request.get_json()
    try:
        base = data.get('base', 0)
        exponent = data.get('exponent', 0)
        result, error = math_controller.power(base, exponent)
        if error:
            return jsonify(success=False, error=error)
        return jsonify(success=True, result=result)
    except Exception:
        return jsonify(success=False, error='Eroare la calculul puterii!')

@math_bp.route('/fibonacci', methods=['POST'])
def fibonacci():
    data = request.get_json()
    try:
        n = data.get('n', 0)
        result, sequence, error = math_controller.fibonacci(n)
        if error:
            return jsonify(success=False, error=error)
        return jsonify(success=True, result=result, sequence=sequence)
    except Exception:
        return jsonify(success=False, error='Eroare la calculul Fibonacci!')

@math_bp.route('/factorial', methods=['POST'])
def factorial():
    data = request.get_json()
    try:
        n = data.get('n', 0)
        result, error = math_controller.factorial(n)
        if error:
            return jsonify(success=False, error=error)
        return jsonify(success=True, result=result)
    except Exception:
        return jsonify(success=False, error='Eroare la calculul factorialului!')
