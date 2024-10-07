from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from tweets.serializers import TweetSerializer
from tweets.models import Tweet
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT

# Create your views here.


class AllTweet(APIView):
    def get(self, request):
        allTweet = Tweet.objects.all()
        serializer = TweetSerializer(
            allTweet,
            many=True,
        )

        return Response(
            serializer.data,
        )

    def post(self, request):

        print(request)

        serializer = TweetSerializer(
            data=request.data,
        )
        if serializer.is_valid():
            print(request.user)
            tweet = serializer.save(user=request.user)
            serializer = TweetSerializer(tweet)

            return Response(
                serializer.data,
            )

        else:
            return Response(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class TweetDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, tweetId):
        try:
            return Tweet.objects.get(id=tweetId)
        except Tweet.DoesNotExist:
            raise NotFound

    def get(self, request, tweetId):
        tweet = self.get_object(tweetId)

        serializer = TweetSerializer(tweet)

        return Response(
            serializer.data,
        )

    def put(self, request, tweetId):
        tweet = self.get_object(tweetId)

        serializer = TweetSerializer(
            tweet,
            data=request.data,
        )

        if serializer.is_valid():
            tweet = serializer.save()
            serializer = TweetSerializer(tweet)

            return Response(
                serializer.data,
            )

        else:
            return Response(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, tweetId):

        tweet = self.get_object(tweetId)
        tweet.delete()
        return Response(
            status=HTTP_204_NO_CONTENT,
        )
