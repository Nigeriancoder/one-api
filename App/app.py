from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# setup db
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # Load config
    app.config.from_pyfile('settings.py')

    # initialize db
    db.init_app(app)

    with app.app_context():

        ##migrate = Migrate(app, db)
        from Api.api import api
        app.register_blueprint(api)

        return app
