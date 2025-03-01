from django.contrib import admin
from .models import Movie
from accounts.models import Profile



admin.site.register(Movie)
admin.site.register(Profile)
