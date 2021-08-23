from flask import Flask

from extensions.database import mongo
from resources.views import views_bp


def create_app(settings='config.settings'):
    app = Flask(__name__)

    app.config.from_object(settings)
    app.register_blueprint(views_bp)

    mongo.init_app(app)

    return app
