from rest_framework import serializers
from apis.models import PoorMansTweet


class PoorMansTweetSerializer(serializers.ModelSerializer):
    """Serialize user data coming from client"""
    class Meta:
        model = PoorMansTweet
        fields = ["name", "message", "timestamp"]
