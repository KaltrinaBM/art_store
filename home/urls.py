from django.urls import path
from . import views

urlpatterns = [
    path('', views.painting_list, name='painting_list'),
    path('all-paintings/', views.all_paintings, name='all_paintings'),
]
