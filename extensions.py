from flask_login import LoginManager
from flask_mail import Mail
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
api = Api()
login_manager = LoginManager()
mail = Mail()


def init_app(app):
    db.init_app(app)
    api.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
