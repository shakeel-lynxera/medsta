from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from medsta import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authModule.urls')),
    path('', include('users.urls')),
    path('posts/', include('posts.urls')),
]
