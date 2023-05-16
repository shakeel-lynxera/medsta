from django.urls.conf import path
from users import views


urlpatterns = [
    
    #Medsta Application Features
    path("", views.dashboard, name="user-dashboard"),
    path("profile/", views.profile, name="user-profile"),
    path("cv/", views.cv, name="user-cv"),
    path("network/", views.network, name="user-network"),
    
    #User Profile Management
    path("update-profile-basic-information/", views.update_profile_basic_information, name="update-profile-basic-information"),
    path("update_profile_title/", views.update_profile_title, name="update-profile-title"),
    path("update-profile-about/", views.update_profile_about, name="update-profile-about"),
    path("add-education/", views.add_education, name="add-education"),
    path("add-experience/", views.add_experience, name="add-experience"),
    path("update-experience/", views.update_experience, name="update-experience"),
    path("delete-experience/<str:id>/", views.delete_experience, name="delete-experience"),
    path("add-skills/", views.add_skills, name="add-skills"),
    path("delete-skill/<str:id>/", views.delete_skill, name="delete-skill"),
    path("add-interests/", views.add_interests, name="add-interests"),
    path("delete-interest/<str:id>/", views.delete_interest, name="delete-interest"),
    path("add-languages/", views.add_languages, name="add-languages"),
    path("delete-language/<str:id>/", views.delete_language, name="delete-language"),
    path("add-accomplishment/", views.add_accomplishment, name="add-accomplishment"),
    path("update-accomplishment/", views.update_accomplishment, name="update-accomplishment"),
    path("delete-accomplishment/<str:id>/", views.delete_accomplishment, name="delete-accomplishment"),
    
    #User connection Management
    path("send-connect-request/<str:reciever_id>/", views.send_connect_request, name="connect"),
    path("cancel-connect-request/<str:id>/", views.cancel_connect_request, name="cancel-connect-request"),
    path("accept-friend-request/<str:id>/", views.accept_friend_request, name="accept-friend-request"),
    path("reject-friend-request/<str:id>/", views.reject_friend_request, name="reject-friend-request"),
    
]