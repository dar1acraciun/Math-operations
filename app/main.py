from flask import Flask
from flask import send_from_directory, request, make_response, redirect, url_for,stream_with_context
from routes.math_routes import math_bp
from routes.auth_routes import auth_bp
import os
from datetime import datetime, timedelta, timezone
from utils.auth_utils import login_required, logout_required
import logging
import sys
from utils.cache_utils import cache
from utils.matrics_utils import setup_monitoring
from utils.kafka_consumer_thread import start_consumer_thread

start_consumer_thread()

app = Flask(__name__)
#app.debug = True  # Set to False in production

app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", "dev_secret")
app.config['CACHE_TYPE'] = 'RedisCache'

app.config['CACHE_REDIS_URL'] = os.environ.get("REDIS_URL", "redis://redis:6379/0")
cache.init_app(app)

setup_monitoring(app)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s: %(message)s',
    handlers=[
        logging.FileHandler('logger.log', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
app.register_blueprint(math_bp, url_prefix="/mathSolve/api")
app.register_blueprint(auth_bp, url_prefix="/mathSolve/")

@app.route('/mathSolve/kafka-logs')
def show_kafka_logs():
    def tail(file, n=100):
        with open(file, 'r', encoding='utf-8') as f:
            return ''.join(f.readlines()[-n:])
    logs = tail('kafka_consumed.log')
    return logs.replace('\n', '<br>')

@app.route('/mathSolve/welcome')
def welcome():
    return send_from_directory('view', 'index.html')

@app.route('/mathSolve/calculator')
@login_required
def calculator():
    return send_from_directory('view', 'calculator.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)