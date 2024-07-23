# main urls.py (e.g., art_store/urls.py)
from django.contrib import admin
from django.urls import path, include
from home import views as home_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('accounts/', include('allauth.urls')),  # Django Allauth URLs for user authentication
    path('paintings/', include('paintings.urls')), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


