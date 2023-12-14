from django.urls import path, include
from .views import Homepage, Homefilms, DetailsFilms, SearchFilm


app_name = 'movie'

urlpatterns = [
    path('', Homepage.as_view(),name='homepage'),
    path('films/', Homefilms.as_view(), name='homefilms'),
    path('films/<int:pk>', DetailsFilms.as_view(), name='detailsfilms'),
    path('searchfilm/', SearchFilm.as_view(), name='searchfilm')
]
