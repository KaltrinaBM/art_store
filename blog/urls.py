from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_post_list, name='blog_post_list'),
    path('<int:post_id>/', views.blog_post_detail, name='blog_post_detail'),
]
