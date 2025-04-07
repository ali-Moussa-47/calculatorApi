from flask import Flask
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

def create_app():
    sentry_sdk.init(
        dsn="https://7d24ad2245b497ba37bd4d65142cd3fc@o4508976581312512.ingest.us.sentry.io/4509112215601152",

        integrations=[FlaskIntegration()],
        traces_sample_rate=1.0,
        environment="dev"
    )

    app = Flask(__name__)

    from .routes import calc_bp
    app.register_blueprint(calc_bp)

    return app
