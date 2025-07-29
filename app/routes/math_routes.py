
from flask import Blueprint, request, jsonify
from controller import math_controller
from schemas.math_schemas import (
    PowerRequest, PowerResponse,
    FibonacciRequest, FibonacciResponse,
    FactorialRequest, FactorialResponse
)
from pydantic import ValidationError

math_bp = Blueprint('math_bp', __name__)
math_controller = math_controller.MathController()


@math_bp.route('/power', methods=['POST'])
def power():
    data = request.get_json()
    try:
        req = PowerRequest(**data)
        result, error = math_controller.power(req.base, req.exponent)
        if error:
            return jsonify(success=False, error=error)
        resp = PowerResponse(result=result)
        return jsonify(success=True, **resp.dict())
    except ValidationError as ve:
        return jsonify(success=False, error=ve.errors()), 400
    except Exception:
        return jsonify(success=False, error='Eroare la calculul puterii!')


@math_bp.route('/fibonacci', methods=['POST'])
def fibonacci():
    data = request.get_json()
    try:
        req = FibonacciRequest(**data)
        result, sequence, error = math_controller.fibonacci(req.n)
        if error:
            return jsonify(success=False, error=error)
        resp = FibonacciResponse(result=result, sequence=sequence)
        return jsonify(success=True, **resp.dict())
    except ValidationError as ve:
        return jsonify(success=False, error=ve.errors()), 400
    except Exception:
        return jsonify(success=False, error='Eroare la calculul Fibonacci!')


@math_bp.route('/factorial', methods=['POST'])
def factorial():
    data = request.get_json()
    try:
        req = FactorialRequest(**data)
        result, error = math_controller.factorial(req.n)
        if error:
            return jsonify(success=False, error=error)
        resp = FactorialResponse(result=result)
        return jsonify(success=True, **resp.dict())
    except ValidationError as ve:
        return jsonify(success=False, error=ve.errors()), 400
    except Exception:
        return jsonify(
            success=False,
            error='Eroare la calculul factorialului!'
        )


@math_bp.route('/history', methods=['GET'])
def history():
    try:
        history = math_controller.get_history()
        return jsonify(success=True, history=history)
    except Exception:
        return jsonify(
            success=False,
            error='Eroare la recuperarea istoricului!'
        )
