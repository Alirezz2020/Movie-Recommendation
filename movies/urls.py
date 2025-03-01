# movies/urls.py
from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.MovieListView.as_view(), name='movie-list'),
    path('<int:pk>/', views.MovieDetailView.as_view(), name='movie-detail'),
    path('search/', views.MovieSearchView.as_view(), name='movie-search'),
    path('rate/<int:movie_id>/', views.rate_movie, name='rate-movie'),
    path('watchlist/', views.WatchlistView.as_view(), name='watchlist'),
    path('watchlist/add/<int:movie_id>/', views.add_to_watchlist, name='add-to-watchlist'),
]
