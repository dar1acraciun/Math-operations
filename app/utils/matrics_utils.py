
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware


def setup_monitoring(app):
    app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
        '/mathSolve/metrics': make_wsgi_app()
    })
