from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

from readings import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(urls)),
    path('auth/', views.obtain_auth_token),
]
