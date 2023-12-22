from .models import movie

def recent_movie_list(request):
    movie_list = movie.objects.all().order_by('-create_date')[0:8]
    featured_film = movie_list[0] if movie_list else None
    return {"recent_movie_list": movie_list, "featured_film": featured_film}

def trending_movies(request):
    movie_list = movie.objects.all().order_by('-number_of_views')[0:10]
    if movie_list:
        trending_movies = movie_list[0]
    else:
        trending_movies = None
    return {"trending_movies": movie_list}

def featured_film(request):
    film = movie.objects.order_by('-create_date').first()
    return {"featured_film" : film}