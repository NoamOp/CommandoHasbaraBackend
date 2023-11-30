from resources import (
    UserCampaignsAPI, CampaignAPI, UserAPI, LogoutAPI, AdminCreateUserAPI,
    AdminAddCampaignToUserAPI, AdminDeleteCampaignFromUserAPI,
    AdminGetAllCampaignsStatsAPI, AdminGetAllCampaignNamesAPI,
)


def initialize_api_routes(api):
    # User-specific routes
    api.add_resource(UserCampaignsAPI, '/user/campaigns')
    api.add_resource(CampaignAPI, '/campaign/<int:campaign_id>')
    api.add_resource(UserAPI, '/user')
    api.add_resource(LogoutAPI, '/logout')
    api.add_resource(AdminCreateUserAPI, '/admin/create_user')
    api.add_resource(
        AdminGetAllCampaignNamesAPI, '/admin/get_all_campaign_names'
        )
    api.add_resource(AdminAddCampaignToUserAPI, '/admin/add_campaign_to_user')
    api.add_resource(
        AdminDeleteCampaignFromUserAPI,
        '/admin/delete_campaign_from_user/<int:user_id>/<string:campaign_name>'
    )
    api.add_resource(
        AdminGetAllCampaignsStatsAPI, '/admin/get_all_campaigns_stats'
    )