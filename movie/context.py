from .models import movie

def recent_movie_list(request):
    movie_list = movie.objects.all().order_by('-create_date')[0:8]
    return{"recent_movie_list": movie_list}

def trending_movies(request):
    movie_list = movie.objects.all().order_by('-number_of_views')[0:8]
    return {"trending_movies": movie_list}

def featured_film(request):
    film = movie.objects.order_by('-create_date')[0]
    return {"featured_film" : film}