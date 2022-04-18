from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import CreatorViewSet

router = DefaultRouter()
router.register("creator", CreatorViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
