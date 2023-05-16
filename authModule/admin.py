from django.contrib import admin
from authModule.models import UserOTP

# Register your models here.


class UserOTPAttr(admin.ModelAdmin):
    list_display = ('id','user')

admin.site.register(UserOTP, UserOTPAttr)