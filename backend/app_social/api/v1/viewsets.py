from rest_framework import authentication
from app_social.models import Creator
from .serializers import CreatorSerializer
from rest_framework import viewsets


class CreatorViewSet(viewsets.ModelViewSet):
    serializer_class = CreatorSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Creator.objects.all()
