from django.urls import path
from . import views

app_name = 'recommendations'

urlpatterns = [
    path('', views.RecommendationListView.as_view(), name='recommendation-list'),
    path('personalized/', views.PersonalizedRecommendationView.as_view(), name='personalized-recommendations'),
]
