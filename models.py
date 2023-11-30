from flask_login import UserMixin

from extensions import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    campaigns = db.relationship('Campaign', backref='owner', lazy=True)


class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    statistics = db.relationship('Statistics', backref='campaign', lazy=True)


class Statistics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    posts_uploaded = db.Column(db.Integer, default=0)
    campaign_id = db.Column(
        db.Integer, db.ForeignKey('campaign.id'), nullable=False
    )

