from django.contrib import admin
from .models import Comment, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'likes_count', 'comments_count', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('author__username', 'description')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('author__username', 'text')
