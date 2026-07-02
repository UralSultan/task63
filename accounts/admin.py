from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительная информация', {
            'fields': ('avatar', 'bio', 'phone', 'gender', 'posts_count', 'following_count', 'followers_count')
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'posts_count', 'followers_count')
