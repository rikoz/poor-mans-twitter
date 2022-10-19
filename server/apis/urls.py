from django.urls import path
from apis.views import PostTweetView

urlpatterns = [
    path("tweet/", PostTweetView.as_view(), name="tweet"),
]
