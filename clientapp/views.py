from django.shortcuts import render, redirect

from clientapp.models import Tweet
from rest_framework import viewsets
from clientapp.serializers import TweetSerializer


def home(request):
    return render(request, "clientapp/index.html")


class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all().order_by('-created_at')
    serializer_class = TweetSerializer
