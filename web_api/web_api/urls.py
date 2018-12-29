from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

from readings import urls as readings_urls
from current import urls as current_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(readings_urls)),
    path('api/', include(current_urls)),
    path('auth/', views.obtain_auth_token),
]
