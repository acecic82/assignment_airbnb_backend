from rest_framework.views import APIView
from rest_framework.response import Response
from tweets.serializers import TweetSerializer
from tweets.models import Tweet

# Create your views here.


class AllTweet(APIView):
    def get(self, request):
        allTweet = Tweet.objects.all()
        serializer = TweetSerializer(allTweet, many=True)

        return Response(
            {
                "ok": True,
                "categories": serializer.data,
            }
        )
