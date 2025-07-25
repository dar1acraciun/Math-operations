from flask import Blueprint, request, send_from_directory, redirect, url_for
from controller import login_controller, register_controller
import jwt, os
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
    if result["status"] == "success":
        user_id = result["user_id"]
        payload = {
            "email": email,
            "user_id": user_id,
            "exp": (datetime.now(timezone.utc) + timedelta(hours=1)).timestamp()
        }
        token = jwt.encode(payload, os.environ.get("SECRET_KEY", "dev_secret"), algorithm="HS256")
        resp = redirect(url_for('calculator'))
        resp.set_cookie("jwt", token, httponly=True, samesite="Lax")
        return resp
    else:
        return f"<h2 style='color:red;text-align:center;margin-top:2em;'>{result['message']}</h2>"

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
    result = register_controller_instance.register(first_name, last_name, email, password, conf_password)
    if "success" in result:
        return f"<h2 style='color:green;text-align:center;margin-top:2em;'>{result['success']}</h2>"
    else:
        return f"<h2 style='color:red;text-align:center;margin-top:2em;'>{result['error']}</h2>"
