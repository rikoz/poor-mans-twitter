from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apis.models import PoorMansTweet
from apis.serializers import PoorMansTweetSerializer


class PostTweetView(APIView):
    """Handle post and get requests for poor man's twitter."""
    serializer_class = PoorMansTweetSerializer

    def get(self, request):
        _data = PoorMansTweet.objects.all()
        serializer = self.serializer_class(_data, many=True)
        return Response(
            {
                "status": "success", 
                "message": "Tweets retrieved successfully",
                "data": serializer.data
            }
        )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "status": "success", 
                "message": "Tweet posted successfully",
                "data": serializer.data
            }
        )
