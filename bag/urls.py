from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add_to_bag/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('adjust_bag/<item_id>/', views.adjust_bag, name='adjust_bag'),
    path('remove_from_bag/<item_id>/', views.remove_from_bag, name='remove_from_bag'),
    path('update_icon_count/', views.update_icon_count, name='update_icon_count'),  

]
