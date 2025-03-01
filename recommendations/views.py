from django.views.generic import ListView
from movies.models import Movie

class RecommendationListView(ListView):
    model = Movie
    template_name = 'recommendations/recommendation_list.html'
    context_object_name = 'recommended_movies'

    def get_queryset(self):
        # Sample logic for recommendations based on genre
        genre = self.request.GET.get('genre', 'Action')
        return Movie.objects.filter(genre=genre).exclude(id=self.kwargs.get('movie_id'))

class PersonalizedRecommendationView(ListView):
    model = Movie
    template_name = 'recommendations/personalized_recommendation_list.html'
    context_object_name = 'recommended_movies'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            watched_movies = user.profile.watched_movies.all()
            if watched_movies:
                # Recommend movies from the same genre as watched movies
                genres = watched_movies.values_list('genre', flat=True)
                return Movie.objects.filter(genre__in=genres).exclude(id__in=watched_movies)
        return Movie.objects.all()  # Default to all movies if no history

