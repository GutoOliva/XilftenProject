from django.urls import path, reverse_lazy
from .views import Homepage, Homefilms, DetailsFilms, SearchFilm, ProfilePage, CreateAccount
from django.contrib.auth import views as auth_view

app_name = 'movie'

urlpatterns = [
    path('', Homepage.as_view(),name='homepage'),
    path('films/', Homefilms.as_view(), name='homefilms'),
    path('films/<int:pk>', DetailsFilms.as_view(), name='detailsfilms'),
    path('searchfilm/', SearchFilm.as_view(), name='searchfilm'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html') , name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html') , name='logout'),
    path('editprofile/<int:pk>', ProfilePage.as_view(), name='editprofile'),
    path('createaccount/', CreateAccount.as_view(), name='createaccount'),
    path('changepassword/', auth_view.PasswordChangeView.as_view(template_name='editprofile.html', success_url=reverse_lazy('movie:homefilms')), name='changepassword'),
]
