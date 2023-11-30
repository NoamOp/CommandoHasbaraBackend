from flask import jsonify, request
from flask_restful import Resource
from flask_login import login_required, current_user, logout_user

from extensions import db
from models import Campaign, User

# RESTful APIs

class UserCampaignsAPI(Resource):
    @login_required
    def get(self):
        # Ensure the user is logged in
        if not current_user.is_authenticated:
            return {'message': 'User not logged in'}, 401

        # Retrieve all campaigns for the current user
        user_campaigns = Campaign.query.filter_by(
            user_id=current_user.id
        ).all()

        # Format the response
        campaigns_data = [{'id': campaign.id, 'name': campaign.name} for
                          campaign in user_campaigns]
        return {'user_campaigns': campaigns_data}


class CampaignAPI(Resource):
    @login_required
    def get(self, campaign_id):
        campaign = Campaign.query.get(campaign_id)
        if not campaign or campaign.owner != current_user:
            return jsonify({'message': 'Campaign not found'}), 404
        return jsonify(
            {'name': campaign.name, 'statistics': campaign.statistics}
        )


class UserAPI(Resource):
    @login_required
    def get(self):
        return jsonify(
            {'username': current_user.username, 'email': current_user.email}
        )


class LogoutAPI(Resource):
    @login_required
    def post(self):
        logout_user()
        return jsonify({'message': 'User logged out'})


class AdminCreateUserAPI(Resource):
    @login_required
    def post(self):
        if not current_user.is_admin:
            return jsonify({'message': 'Permission denied'}), 403

        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        # Validate input...

        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User created successfully'})


class AdminGetAllCampaignNamesAPI(Resource):
    @login_required
    def get(self):
        if not current_user.is_admin:
            return jsonify({'message': 'Permission denied'}), 403

        campaign_names = [campaign.name for campaign in Campaign.query.all()]
        return jsonify({'campaign_names': campaign_names})


class AdminAddCampaignToUserAPI(Resource):
    @login_required
    def post(self):
        if not current_user.is_admin:
            return jsonify({'message': 'Permission denied'}), 403

        data = request.get_json()
        user_id = data.get('user_id')
        campaign_name = data.get('campaign_name')

        user = User.query.get(user_id)
        if not user:
            return jsonify({'message': 'User not found'}), 404

        campaign = Campaign.query.filter_by(name=campaign_name).first()
        if not campaign:
            return jsonify({'message': 'Campaign not found'}), 404

        user.campaigns.append(campaign)
        db.session.commit()

        return jsonify(
            {'message': f'{campaign_name} added to {user.username}'}
        )


class AdminDeleteCampaignFromUserAPI(Resource):
    @login_required
    def delete(self, user_id, campaign_name):
        if not current_user.is_admin:
            return jsonify({'message': 'Permission denied'}), 403

        user = User.query.get(user_id)
        if not user:
            return jsonify({'message': 'User not found'}), 404

        campaign = Campaign.query.filter_by(name=campaign_name).first()
        if not campaign:
            return jsonify({'message': 'Campaign not found'}), 404

        user.campaigns.remove(campaign)
        db.session.commit()

        return jsonify(
            {'message': f'{campaign_name} removed from {user.username}'}
        )


class AdminGetAllCampaignsStatsAPI(Resource):
    @login_required
    def get(self):
        if not current_user.is_admin:
            return jsonify({'message': 'Permission denied'}), 403

        all_campaigns_stats = {
            campaign.name: {'statistics': campaign.statistics} for campaign in
            Campaign.query.all()}
        return jsonify(all_campaigns_stats)
