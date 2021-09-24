from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser, Profile


class ProfileInline(admin.TabularInline):
    model = Profile

class CustomUserAdmin(UserAdmin):
    list_display = ['id', 'username', 'email',
                    'first_name', 'last_name', ]
    list_display_links = ['id', 'username']
    inlines = [
        ProfileInline,
    ]

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'image', 'bio', 'country']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)
