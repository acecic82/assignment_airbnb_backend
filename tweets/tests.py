from rest_framework.test import APITestCase

from .models import Tweet
from users.models import User

# Create your tests here.


class TestAllTweet(APITestCase):

    PAYLOADS = [
        "Tweet Payload1",
        "Tweet Payload2",
        "Tweet Payload3",
    ]
    TESTUSER = "Test User"
    URL = "/api/v1/tweets/"

    def setUp(self):
        user = User.objects.create(username=self.TESTUSER)

        for paylaod in self.PAYLOADS:
            Tweet.objects.create(
                user=user,
                payload=paylaod,
            )

        self.user = user

    def testAllTweet(self):
        print("-------------test_all_tweet---------------")

        response = self.client.get(self.URL)
        data = response.json()

        self.assertEqual(response.status_code, 200, "Status Code isn't 200.")

        self.assertIsInstance(data, list)

        self.assertEqual(len(data), len(self.PAYLOADS))

        for idx, tweet in enumerate(data):
            self.assertEqual(
                tweet["payload"],
                self.PAYLOADS[idx],
            )

    def testCreateTweet(self):
        print("-------------test_create_tweet---------------")

        newTweetPayload = "New Payload"

        response = self.client.post(
            self.URL,
            data={
                "payload": newTweetPayload,
            },
            headers={
                "X-USERNAME": self.TESTUSER,
            },
        )

        self.assertEqual(response.status_code, 200, "Not 200 status code")

        data = response.json()

        self.assertEqual(
            data["payload"],
            newTweetPayload,
        )


class TestTweetDetail(APITestCase):
    PAYLOADS = [
        "Tweet Payload1",
        "Tweet Payload2",
        "Tweet Payload3",
    ]

    TESTUSER = "Test User"
    URL = "/api/v1/tweets"
    TWEETS = []

    def setUp(self):
        user = User.objects.create(username=self.TESTUSER)

        for paylaod in self.PAYLOADS:
            tweet = Tweet.objects.create(
                user=user,
                payload=paylaod,
            )
            self.TWEETS.append(tweet)

        self.user = user

    def testTweet(self):
        print("-------------test_get_specific_tweet---------------")

        for idx, payload in enumerate(self.PAYLOADS):

            response = self.client.get(
                f"{self.URL}/{idx+1}",
                headers={
                    "X-USERNAME": self.TESTUSER,
                },
            )
            data = response.json()

            self.assertEqual(response.status_code, 200, "Status Code isn't 200.")

            self.assertEqual(
                data["payload"],
                payload,
            )

    def testPutTweet(self):
        print("-------------test_put_specific_tweet---------------")

        editPayload = "edit payload"

        response = self.client.put(
            f"{self.URL}/1",
            data={
                "payload": editPayload,
            },
            headers={
                "X-USERNAME": self.TESTUSER,
            },
        )

        data = response.json()

        self.assertEqual(response.status_code, 200, "Status Code isn't 200.")

        self.assertEqual(data["payload"], editPayload)

    def testTweetDelete(self):
        print("-------------test_delete_specific_tweet---------------")

        response = self.client.delete(
            f"{self.URL}/1",
            headers={
                "X-USERNAME": self.TESTUSER,
            },
        )

        self.assertEqual(response.status_code, 204)
