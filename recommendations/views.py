from django.views.generic import ListView
from movies.models import Movie

class RecommendationListView(ListView):
    model = Movie
    template_name = 'recommendations/recommendation_list.html'
    context_object_name = 'recommended_movies'

    def get_queryset(self):
        # Try to get movies with a non-null rating
        qs = Movie.objects.filter(rating__isnull=False).order_by('-rating')[:10]

        if not qs.exists():
            # Fallback: order by release_date if no ratings are available
            qs = Movie.objects.order_by('-release_date')[:10]
        return qs

class PersonalizedRecommendationView(ListView):
    model = Movie
    template_name = 'recommendations/personalized_recommendation_list.html'
    context_object_name = 'recommended_movies'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            watchlist = user.profile.saved_movies.all()  # Ensure you have this relation in your profile
            if watchlist.exists():
                # Gather genres from movies in the watchlist (assuming genre is stored as a string)
                genres = [movie.genre for movie in watchlist if movie.genre]
                if genres:
                    # For simplicity, use the first genre as the preferred genre
                    preferred_genre = genres[0]
                    qs = Movie.objects.filter(genre__icontains=preferred_genre).order_by('-rating')
                    if qs.exists():
                        return qs[:10]
            # If no watchlist movies or no genre data available, you might use another personalized criteria,
            # e.g., based on user's ratings if implemented
        # Fallback: return top-rated movies
        return Movie.objects.order_by('-rating')[:10]

