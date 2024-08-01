# main urls.py (e.g., art_store/urls.py)
from django.contrib import admin
from django.urls import path, include
from home import views as home_views
from django.conf import settings
from django.conf.urls.static import static
from bag import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('accounts/', include('allauth.urls')),  # Django Allauth URLs for user authentication
    path('paintings/', include('paintings.urls')), 
    path('bag/', include('bag.urls')),
    path('checkout/', views.checkout, name='checkout'),
    path('reviews/', include('reviews.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('checkout/', include('checkout.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


