from django.urls.conf import path
from posts import views

urlpatterns = [
    path("upload-post/", views.upload_post, name="user-dashboard")
]
