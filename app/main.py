from flask import Flask
from flask import send_from_directory, request, make_response, redirect, url_for
from routes.math_routes import math_bp
from controller import register_controller
from controller import login_controller
import os
import jwt
from datetime import datetime, timedelta, timezone



app = Flask(__name__)
app.register_blueprint(math_bp, url_prefix="/api")



@app.route('/welcome')
def welcome():
    return send_from_directory('view', 'index.html')

@app.get('/login')
def login():
        return send_from_directory('view', 'login.html')


@app.post('/login')
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    login_controller_instance = login_controller.LoginController()
    result = login_controller_instance.login(email, password)
    if result["status"] == "success":
        SECRET_KEY = os.environ.get("SECRET_KEY", "dev_secret")
        payload = {
            "email": email,
            "exp": (datetime.now(timezone.utc) + timedelta(hours=1)).timestamp()
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        resp = redirect(url_for('calculator'))
        resp.set_cookie("jwt", token, httponly=True, samesite="Lax")
        return resp
    else:
        return f"<h2 style='color:red;text-align:center;margin-top:2em;'>{result['message']}</h2>"
@app.get('/calculator')
def calculator():
    return send_from_directory('view', 'calculator.html')
@app.get('/register')
def register():
    return send_from_directory('view', 'register.html')

@app.post('/register')
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)