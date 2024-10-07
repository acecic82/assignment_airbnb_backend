from django.urls import path
from . import views

urlpatterns = [
    path("", views.AllTweet.as_view()),
    path("<int:tweetId>", views.TweetDetail.as_view()),
]
