from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    ost=models.CharField(max_length=200)
    video=models.CharField(max_length=200)
    answerCnt=models.IntegerField(default=0)
