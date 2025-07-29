
from flask import Blueprint
from flask import request
from flask import send_from_directory
from flask import redirect
from flask import url_for
from flask import jsonify
from controller import login_controller
from controller import register_controller
import jwt
import os
from datetime import datetime, timedelta, timezone
from utils.auth_utils import logout_required

auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/login', methods=['GET'])
@logout_required
def login():
    return send_from_directory('view', 'login.html')


@auth_bp.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    login_controller_instance = login_controller.LoginController()
    result = login_controller_instance.login(email, password)
    is_ajax = (
        request.headers.get('X-Requested-With') == 'XMLHttpRequest' or
        request.accept_mimetypes['application/json'] > 0
    )
    if is_ajax:
        if result["status"] == "success":
            user_id = result["user_id"]
            payload = {
                "email": email,
                "user_id": user_id,
                "exp": (
                    datetime.now(timezone.utc) + timedelta(hours=1)
                ).timestamp()
            }
            token = jwt.encode(
                payload,
                os.environ.get("SECRET_KEY", "dev_secret"),
                algorithm="HS256"
            )
            # Trimite redirect info ca JSON pentru frontend
            response = jsonify({
                "success": "Autentificare reușită!",
                "redirect": url_for('calculator')
            })
            response.set_cookie(
                "jwt", token, httponly=True, samesite="Lax"
            )
            return response, 200
        else:
            # Controllerul returnează probabil 'message' la eroare
            return jsonify({
                "error": result.get("message", "Eroare necunoscută")
            }), 400
    # Fallback pentru POST clasic (form action)
    if result["status"] == "success":
        user_id = result["user_id"]
        payload = {
            "email": email,
            "user_id": user_id,
            "exp": (
                datetime.now(timezone.utc) + timedelta(hours=1)
            ).timestamp()
        }
        token = jwt.encode(
            payload,
            os.environ.get("SECRET_KEY", "dev_secret"),
            algorithm="HS256"
        )
        resp = redirect(url_for('calculator'))
        resp.set_cookie(
            "jwt", token, httponly=True, samesite="Lax"
        )
        return resp


@auth_bp.route('/register', methods=['GET'])
@logout_required
def register():
    return send_from_directory('view', 'register.html')


@auth_bp.route('/register', methods=['POST'])
def register_post():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    password = request.form.get('password')
    conf_password = request.form.get('conf_password')
    register_controller_instance = register_controller.RegisterController()
    from utils.matrics_utils import registration_counter
    from utils.matrics_utils import endpoint_response_time
    import time
    start = time.time()
    result = register_controller_instance.register(
        first_name,
        last_name,
        email,
        password,
        conf_password
    )
    duration = time.time() - start
    endpoint_response_time.labels(endpoint='/register').observe(duration)
    if "success" in result:
        registration_counter.inc()
    # Dacă e AJAX (fetch), răspunde cu JSON
    is_ajax = (
        request.headers.get('X-Requested-With') == 'XMLHttpRequest' or
        request.accept_mimetypes['application/json'] > 0
    )
    if is_ajax:
        if "success" in result:
            return jsonify({"success": result["success"]}), 200
        else:
            return jsonify({
                "error": result.get("error", "Eroare necunoscută")
            }), 400
