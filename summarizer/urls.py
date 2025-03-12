from django.urls import path
from .views import summarize_and_tweet

urlpatterns = [
    path("summarize-and-tweet/", summarize_and_tweet, name="summarize_and_tweet"),
]