from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView

from models import User, Campaign, Statistics
from extensions import db

from flask_login import (
    UserMixin, LoginManager, login_user, login_required, logout_user,
    current_user,
)


class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('admin/index.html')


class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin


def initialize_admin(app):

    # Initialize extensions
    admin = Admin(app, index_view=MyAdminIndexView())
    admin.add_view(MyModelView(User, db.session))
    admin.add_view(MyModelView(Campaign, db.session))
    admin.add_view(MyModelView(Statistics, db.session))
