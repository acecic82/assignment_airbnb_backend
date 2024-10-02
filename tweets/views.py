from django.shortcuts import render
from tweets.models import Tweet

# Create your views here.


def seeAllTweets(request):
    allTweet = Tweet.objects.all()
    return render(
        request,
        "allTweets.html",
        {
            "allTweet": allTweet,
            "title": "See All Tweet",
        },
    )
