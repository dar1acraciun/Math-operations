

from prometheus_client import make_wsgi_app, Counter, Histogram
from werkzeug.middleware.dispatcher import DispatcherMiddleware

# Counter for new user registrations
registration_counter = Counter(
    'user_registrations_total',
    'Total number of user registrations'
)

# Counter for math operations by type
math_operations_counter = Counter(
    'math_operations_total',
    'Total number of math operations by type',
    ['operation']
)

# Histogram for response time per endpoint
endpoint_response_time = Histogram(
    'endpoint_response_seconds',
    'Response time in seconds for each endpoint',
    ['endpoint']
)


def setup_monitoring(app):
    app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
        '/mathSolve/metrics': make_wsgi_app()
    })
