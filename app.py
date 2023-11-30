# app.py
from flask import Flask
from config import Config
from extensions import init_app, db, api
from api_routes import initialize_api_routes
from admin import initialize_admin
from auth import initialize_auth
from mail import send_reset_email

app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
init_app(app)

# Initialize API routes
initialize_api_routes(api)

# Initialize Flask-Admin
initialize_admin(app)

# Initialize authentication
initialize_auth(app)


@app.route('/')
def index():
    return ""


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
