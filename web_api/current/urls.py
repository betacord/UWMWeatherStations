from django.urls import path, include
from rest_framework import routers
from current import views

router = routers.DefaultRouter()
router.register(r'current', views.CurrentViewSet, base_name='current')
router.register(r'station', views.StationViewSet, base_name='station')

urlpatterns = [
    path('', include(router.urls))
]
