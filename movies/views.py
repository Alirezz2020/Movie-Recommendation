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
        rating = float(request.POST['rating'])
        movie.update_rating(rating)
        # Optionally, save the user's rating in a separate model (UserMovieRating)

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
    movie = get_object_or_404(Movie, pk=movie_id)
    user_profile = request.user.profile

    if movie in user_profile.saved_movies.all():
        user_profile.saved_movies.remove(movie)
    else:
        user_profile.saved_movies.add(movie)

    return redirect('movies:movie-detail', movie_id=movie.id)

