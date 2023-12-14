from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import movie
from django.views.generic import TemplateView, ListView, DetailView

#def homepage(request):
#    return render(request, "homepage.html")

class Homepage(TemplateView):
    template_name = 'homepage.html'

#def homefilms(request):
#   context = {}
#    movie_list = movie.objects.all()
#    context['movie_list'] = movie_list
#    return render(request, "homefilms.html", context)

class Homefilms(ListView):
    template_name = "homefilms.html"
    model = movie
    # object_list

class DetailsFilms(DetailView):
    template_name = "detailsfilm.html"
    model = movie
    #object -> 1 item from our model

    def get(self, request, *args, **kwargs):
        movie = self.get_object()
        movie.number_of_views += 1
        movie.save()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DetailsFilms, self).get_context_data(**kwargs)
        related_movies = movie.objects.filter(category=self.get_object().category)[0:5]
        context["related_movies"] = related_movies
        return context

class SearchFilm(ListView):
    template_name = "searchfilm.html"
    model = movie

    def get_queryset(self):
        search_term = self.request.GET.get('query')
        if search_term:
            object_list = movie.objects.filter(title__icontains= search_term) 
            return object_list
        else:
            return None