from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser, Profile


admin.site.register(CustomUser, UserAdmin)
admin.site.register(Profile)
