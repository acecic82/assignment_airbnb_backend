from rest_framework.decorators import api_view
from rest_framework.response import Response
from tweets.serializers import TweetSerializer
from tweets.models import Tweet

# Create your views here.


@api_view()
def seeAllTweets(request):
    allTweet = Tweet.objects.all()
    serializer = TweetSerializer(allTweet, many=True)
    return Response(
        {
            "ok": True,
            "categories": serializer.data,
        }
    )
