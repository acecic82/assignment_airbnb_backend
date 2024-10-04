from django.urls import path
from . import views

urlpatterns = [
    path("/<int:userId>/tweets", views.AllTweetByUser.as_view()),
]
