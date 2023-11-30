from extensions import login_manager
from models import User


# Authentication

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def initialize_auth(app):
    login_manager.init_app(app)
