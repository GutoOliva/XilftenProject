from django.contrib import admin
from .models import movie, episode, user
from django.contrib.auth.admin import UserAdmin

fields = list(UserAdmin.fieldsets)
fields.append(
    ("Historic", {'fields' : ('seen_movies',)})
)
UserAdmin.fieldsets = tuple(fields)

admin.site.register(movie)
admin.site.register(episode)
admin.site.register(user, UserAdmin)