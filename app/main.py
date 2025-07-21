from flask import Flask
from routes.math_routes import math_bp

app = Flask(__name__)
app.register_blueprint(math_bp, url_prefix="/api")


@app.get('/first')
def first():
    return {'message': 'Hello from the first endpoint!'}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)