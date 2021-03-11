from flask import Flask

def create_app():
    app = Flask(__name__, static_folder=None)
    app.secret_key = 'dontsharethiswithanyone'

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from .frontend import frontend
    from .api import api

    app.register_blueprint(frontend)
    app.register_blueprint(api, url_prefix="/api")

    from .models import db
    db.init_app(app)

    return app