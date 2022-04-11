from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main.views import EdstemTestViewSet

router = DefaultRouter()
router.register('', EdstemTestViewSet, basename='main')

urlpatterns = [
    path('api/', include(router.urls)),
]