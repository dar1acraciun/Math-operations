
from functools import wraps
import jwt
from flask import request, redirect, url_for, current_app


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.cookies.get('jwt')
        if not token:
            return redirect(url_for('login'))
        try:
            jwt.decode(
                token,
                current_app.config['SECRET_KEY'],
                algorithms=["HS256"]
            )
        except jwt.ExpiredSignatureError:
            return redirect(url_for('login'))
        except jwt.InvalidTokenError:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


def logout_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.cookies.get('jwt')
        if token:
            try:
                jwt.decode(
                    token,
                    current_app.config['SECRET_KEY'],
                    algorithms=["HS256"]
                )
                return redirect(url_for('calculator'))
            except jwt.InvalidTokenError:
                pass
        return f(*args, **kwargs)
    return decorated_function


def get_user_id_from_token():
    token = request.cookies.get('jwt')
    try:
        payload = jwt.decode(
            token,
            current_app.config['SECRET_KEY'],
            algorithms=["HS256"]
        )
        return payload.get('user_id')
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
