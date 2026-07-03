from django.urls import path

from .views import post_create_view, post_detail_view, post_like_view


app_name = 'posts'

urlpatterns = [
    path('create/', post_create_view, name='create'),
    path('<int:pk>/', post_detail_view, name='detail'),
    path('<int:pk>/like/', post_like_view, name='like'),
]
