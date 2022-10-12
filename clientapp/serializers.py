from rest_framework import serializers

from clientapp.models import Tweet


class TweetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tweet
        fields = ['name', 'tweet_body']
