from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    
    path('api-auth/', include('dj_rest_auth.urls')),
    path('rest-auth/', include('rest_framework.urls')),
    
    path('api-registration/', include('dj_rest_auth.registration.urls')),
]
