from rest_framework import serializers


class TweetSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    payload = serializers.CharField(required=True)
    user = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
