from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

from django.contrib.auth import authenticate, login, logout

from users.models import User
from tweets.models import Tweet
from tweets.serializers import TweetSerializer
from users.serializers import PrivateUserSerializer, TinyUserSerializer

# Create your views here.


class AllUser(APIView):
    def get(self, request):
        users = User.objects.all()

        serializer = TinyUserSerializer(
            users,
            many=True,
        )

        return Response(
            serializer.data,
        )

    def post(self, request):
        password = request.data.get("password")

        if not password:
            raise ParseError

        serializer = PrivateUserSerializer(
            data=request.data,
        )

        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()

            serializer = PrivateUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class UserDetail(APIView):

    def get(self, request, userId):
        user = User.objects.get(id=userId)

        serializer = TinyUserSerializer(user)

        return Response(
            serializer.data,
        )


class ChangePassword(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user

        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")

        if not old_password or not new_password:
            raise ParseError

        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response(status=HTTP_200_OK)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)


class LogIn(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            raise ParseError

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user:
            login(
                request,
                user,
            )

            return Response({"ok": "Welcome!"})
        else:
            return Response({"error": "wrong password"})


class LogOut(APIView):

    def post(self, request):
        logout(request)

        return Response(
            {
                "ok": "Bye Bye~",
            },
        )


class AllTweetByUser(APIView):

    def get(self, request, userId):
        try:
            User.objects.get(pk=userId)
            allTweet = Tweet.objects.filter(user_id=userId)
            serializer = TweetSerializer(allTweet, many=True)
            return Response(
                serializer.data,
            )
        except User.DoesNotExist:
            raise NotFound
