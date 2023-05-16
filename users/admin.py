from django.contrib import admin
from django.contrib.auth.models import User

from users.models import Profile

# Register your models here.

class ProfileAttr(admin.ModelAdmin):
    list_display = ("id", "user")

admin.site.register(Profile, ProfileAttr)