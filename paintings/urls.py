from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.painting_list, name='painting_list'),
    path('<int:pk>/', views.painting_detail, name='painting_detail'),
    path('all/', views.all_paintings, name='all_paintings'),
]



