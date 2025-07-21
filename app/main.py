from flask import Flask
from flask import send_from_directory
from routes.math_routes import math_bp

app = Flask(__name__)
app.register_blueprint(math_bp, url_prefix="/api")



@app.route('/welcome')
def welcome():
    return send_from_directory('model', 'index.html')

    # Servește login.html la ruta /login
    @app.route('/login')
    def login():
        return send_from_directory('model', 'login.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)