from django.views.generic import ListView, DetailView
from .models import Movie
from django.shortcuts import render, get_object_or_404

from django.shortcuts import redirect
class MovieListView(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'movies'

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'
    context_object_name = 'movie'


def rate_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'POST':
        rating = float(request.POST.get('rating', 0))
        movie.update_rating(rating)
        return redirect('movies:movie-detail', pk=movie.id)
    else:
        # Optionally, show the rating form if needed
        return render(request, 'movies/movie_detail.html', {'movie': movie})



class MovieSearchView(ListView):
    model = Movie
    template_name = 'movies/movie_search_results.html'
    context_object_name = 'movies'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Movie.objects.filter(title__icontains=query)
        return Movie.objects.all()



class WatchlistView(ListView):
    model = Movie
    template_name = 'movies/watchlist.html'
    context_object_name = 'watchlist_movies'

    def get_queryset(self):
        return self.request.user.profile.saved_movies.all()





def add_to_watchlist(request, movie_id):
    if request.method == 'POST':
        movie = get_object_or_404(Movie, pk=movie_id)
        user_profile = request.user.profile  # Adjust based on your user profile implementation
        if movie in user_profile.saved_movies.all():
            user_profile.saved_movies.remove(movie)
        else:
            user_profile.saved_movies.add(movie)
        # Use 'pk' in kwargs when redirecting to the movie detail view
        return redirect('movies:movie-detail', pk=movie.id)
    else:
        # If not a POST, simply redirect to the movie detail view.
        return redirect('movies:movie-detail', pk=movie_id)