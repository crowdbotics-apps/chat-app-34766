from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ContentViewSet, CreatorViewSet

router = DefaultRouter()
router.register("creator", CreatorViewSet)
router.register("content", ContentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
