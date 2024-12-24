from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    BoxViewSet, ItemViewSet
)

router = DefaultRouter()

router.register(r'boxes', BoxViewSet, basename='boxes')
router.register(r'items', ItemViewSet, basename='items')

app_name = "boxesapp"

urlpatterns = [
    path('', include(router.urls))
]
