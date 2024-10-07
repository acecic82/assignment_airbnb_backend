from rest_framework import serializers
from tweets.models import Tweet
from users.serializers import TinyUserSerializer


class TweetSerializer(serializers.ModelSerializer):

    user = TinyUserSerializer(
        read_only=True,
    )

    class Meta:
        model = Tweet
        fields = "__all__"
