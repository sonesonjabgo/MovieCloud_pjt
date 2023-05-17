from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    # like_users = models.ManyToManyField() accounts 모델 만들고 하기
    title = models.CharField(max_length=100)
    vote_average = models.FloatField()
    overview = models.TextField()
    popularity = models.FloatField()
    poster_path = models.CharField(max_length=200)
    release_date = models.DateField()


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=300)
    