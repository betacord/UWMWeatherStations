from django.urls import path, include
from rest_framework import routers
from readings import views

router = routers.DefaultRouter()
router.register(r'readings', views.ReadingViewSet, base_name='users')

urlpatterns = [
    path('', include(router.urls))
]
