from django.urls import path

from .views import (
    index_view,
    login_view,
    logout_view,
    profile_edit_view,
    profile_view,
    register_view,
    user_posts_view,
    user_profile_view,
    user_search_view,
)


app_name = 'accounts'

urlpatterns = [
    path('', index_view, name='index'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', profile_edit_view, name='profile_edit'),
    path('users/search/', user_search_view, name='user_search'),
    path('users/<str:username>/', user_profile_view, name='user_profile'),
    path('users/<str:username>/posts/', user_posts_view, name='user_posts'),
]
