# home/views.py
from django.views.generic import TemplateView
from movies.models import Movie

class HomeView(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch latest 5 movies based on release date (new movies)
        context['new_movies'] = Movie.objects.order_by('-release_date')[:5]
        # Fetch top 5 movies based on rating
        context['top_movies'] = Movie.objects.order_by('-rating')[:5]
        return context
