from rest_framework import serializers
from app_social.models import Creator


class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creator
        fields = "__all__"
