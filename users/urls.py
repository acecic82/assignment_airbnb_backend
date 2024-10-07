from django.urls import path
from . import views

urlpatterns = [
    path("", views.AllUser.as_view()),
    path("<int:userId>", views.UserDetail.as_view()),
    path("<int:userId>/tweets", views.AllTweetByUser.as_view()),
    path("password", views.ChangePassword.as_view()),
    path("log-in", views.LogIn.as_view()),
    path("log-out", views.LogOut.as_view()),
]
