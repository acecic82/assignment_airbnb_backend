from django.contrib import admin
from tweets.models import Tweet, Like
from tweets.filter import ElonMuskFilter

# Register your admin here.


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):

    list_display = (
        "payload",
        "user",
        "countOfLike",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "created_at",
        ElonMuskFilter,
    )

    search_fields = (
        "user__username",
        "payload",
    )


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):

    list_display = (
        "tweet",
        "user",
        "created_at",
        "updated_at",
    )

    list_filter = ("created_at",)

    search_fields = (
        # foreignKey -> User.name contain case
        # you can also use ^user__username"
        "user__username",
    )
