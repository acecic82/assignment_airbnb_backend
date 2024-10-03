from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from users.models import User
from tweets.models import Tweet
from tweets.serializers import TweetSerializer

# Create your views here.


@api_view()
def seeUserAllTweet(request, userId):
    try:
        User.objects.get(pk=userId)
        allTweet = Tweet.objects.filter(user_id=userId)
        serializer = TweetSerializer(allTweet, many=True)
        return Response(
            {
                "ok": True,
                "categories": serializer.data,
            }
        )
    except User.DoesNotExist:
        raise NotFound
