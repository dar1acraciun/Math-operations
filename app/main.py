from flask import Flask
from flask import send_from_directory, request, make_response, redirect, url_for
from routes.math_routes import math_bp
from routes.auth_routes import auth_bp
from controller import register_controller
from controller import login_controller
import os
import jwt
from datetime import datetime, timedelta, timezone




app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", "dev_secret")

app.register_blueprint(math_bp, url_prefix="/mathSolve/api")
app.register_blueprint(auth_bp, url_prefix="/mathSolve/")

# Decorator pentru verificare JWT
from functools import wraps
import jwt

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.cookies.get('jwt')
        if not token:
            return redirect(url_for('login'))
        try:
            jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return redirect(url_for('login'))
        except jwt.InvalidTokenError:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/mathSolve/welcome')
def welcome():
    return send_from_directory('view', 'index.html')

@app.get('/mathSolve/calculator')
@login_required
def calculator():
    return send_from_directory('view', 'calculator.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)