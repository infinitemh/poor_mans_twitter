from django.db import models
# Create your models here.
class Tweet(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    tweet_body = models.CharField(max_length=50)

    def __str__(self):
        return self.tweet_body[:10]
