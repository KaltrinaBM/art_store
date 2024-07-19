from django.urls import path
from . import views

urlpatterns = [
    path('', views.painting_list, name='painting_list'),
    path('all/', views.all_paintings, name='all_paintings'),
    path('<int:pk>/', views.painting_detail, name='painting_detail'),
]
