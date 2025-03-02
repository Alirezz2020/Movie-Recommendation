# movies/models.py
from django.db import models
from django.conf import settings
from decimal import Decimal


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=100)
    poster = models.URLField()  # Using URLField for external image URLs
    rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    num_ratings = models.PositiveIntegerField(default=0)

    def update_average_rating(self):
        ratings = self.ratings.all()  # using the related_name from MovieRating
        if ratings.exists():
            total = sum(r.rating for r in ratings)
            self.num_ratings = ratings.count()
            self.rating = total / Decimal(self.num_ratings)
        else:
            self.rating = None
            self.num_ratings = 0
        self.save()

    def __str__(self):
        return self.title


class MovieRating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    class Meta:
        unique_together = ('movie', 'user')  # Ensures one rating per user per movie

    def __str__(self):
        return f"{self.user} rated {self.movie} as {self.rating}"
