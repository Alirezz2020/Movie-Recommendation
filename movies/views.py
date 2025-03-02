from django.views.generic import ListView, DetailView
from decimal import Decimal
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from movies.models import Movie, MovieRating
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
        if request.user.is_authenticated:
            # Check if the user already rated this movie
            if MovieRating.objects.filter(movie=movie, user=request.user).exists():
                messages.error(request, "You have already rated this movie.")
                return redirect('movies:movie-detail', pk=movie.id)
            try:
                rating_value = Decimal(request.POST.get('rating'))
            except (TypeError, ValueError):
                messages.error(request, "Invalid rating value.")
                return redirect('movies:movie-detail', pk=movie.id)

            # Create a new rating entry
            MovieRating.objects.create(movie=movie, user=request.user, rating=rating_value)
            # Update the movie's average rating
            movie.update_average_rating()
            messages.success(request, "Thank you for rating!")
            return redirect('movies:movie-detail', pk=movie.id)
        else:
            messages.error(request, "Please log in to rate movies.")
            return redirect('accounts:login')

    # If GET request or other, simply redirect to detail page
    return redirect('movies:movie-detail', pk=movie.id)



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