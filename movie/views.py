from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from .models import movie, user
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateAcoountForm, HomeForm

class Homepage(FormView):
    template_name = 'homepage.html'
    form_class = HomeForm

    def get_success_url(self):
        email = self.request.POST.get("email")
        users = user.objects.filter(email=email)
        if users:
            return reverse('movie:login')
        else:
            return reverse('movie:createaccount')

        

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('movie:homefilms')
        else:
            return super().get(request,*args,**kwargs)
        
#def homefilms(request):
#   context = {}
#    movie_list = movie.objects.all()
#    context['movie_list'] = movie_list
#    return render(request, "homefilms.html", context)

class Homefilms(LoginRequiredMixin, ListView):
    template_name = "homefilms.html"
    model = movie
    # object_list

class DetailsFilms(LoginRequiredMixin, DetailView):
    template_name = "detailsfilm.html"
    model = movie
    #object -> 1 item from our model

    def get(self, request, *args, **kwargs):
        movie = self.get_object()
        movie.number_of_views += 1
        movie.save()
        user = request.user
        user.seen_movies.add(movie)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DetailsFilms, self).get_context_data(**kwargs)
        related_movies = movie.objects.filter(category=self.get_object().category)[0:5]
        context["related_movies"] = related_movies
        return context

class SearchFilm(LoginRequiredMixin, ListView):
    template_name = "searchfilm.html"
    model = movie

    def get_queryset(self):
        search_term = self.request.GET.get('query')
        if search_term:
            object_list = movie.objects.filter(title__icontains= search_term) 
            return object_list
        else:
            return None
        
class ProfilePage(LoginRequiredMixin, UpdateView):
    template_name = "editprofile.html"
    model = user
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse('movie:homefilms')

class CreateAccount(FormView):
    template_name = "createaccount.html"
    form_class = CreateAcoountForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('movie:login')