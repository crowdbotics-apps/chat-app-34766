from rest_framework import authentication
from app_social.models import Content, Creator
from .serializers import ContentSerializer, CreatorSerializer
from rest_framework import viewsets


class CreatorViewSet(viewsets.ModelViewSet):
    serializer_class = CreatorSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Creator.objects.all()


class ContentViewSet(viewsets.ModelViewSet):
    serializer_class = ContentSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Content.objects.all()
