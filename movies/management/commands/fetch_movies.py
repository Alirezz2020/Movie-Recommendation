import requests
from django.core.management.base import BaseCommand
from movies.models import Movie

class Command(BaseCommand):
    help = 'Fetch movie data from TMDb API'

    def handle(self, *args, **kwargs):
        api_key = '29003c0e0133439088601a1d3d669d0b'
        url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en-US&page=1'
        response = requests.get(url)
        data = response.json()

        for movie_data in data.get('results', []):
            if not Movie.objects.filter(title=movie_data['title']).exists():
                movie = Movie(
                    title=movie_data['title'],
                    description=movie_data.get('overview', ''),
                    release_date=movie_data.get('release_date', None),
                    # Here you might need to process genres properly.
                    genre=', '.join(str(genre) for genre in movie_data.get('genre_ids', [])),
                    poster=f'https://image.tmdb.org/t/p/w500{movie_data.get("poster_path", "")}',
                    rating=movie_data.get('vote_average', 0)
                )
                movie.save()
        self.stdout.write(self.style.SUCCESS('Successfully fetched movies'))
