from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

categories_list = (
    ("SERIES", "Séries"),
    ("FILMES", "Filmes"),
    ("APRESENTACAO", "Apresentação"),
    ("OUTROS", "Outros")
)


class movie(models.Model):

    thumb = models.ImageField(upload_to='thumb_movies')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    category = models.CharField(max_length=15, choices=categories_list)
    number_of_views = models.IntegerField(default=0)
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
class episode(models.Model):
    movie = models.ForeignKey('movie', related_name="episodes", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video = models.URLField()
    

    def __str__(self):
        return self.movie.title + " | " + self.title

class user(AbstractUser):
    seen_movies = models.ManyToManyField("movie")
