from django.urls import path
from movies.views import MovieListCreateView, MovieRetrieveUpdateDeleteView, MovieRandomizerView


urlpatterns = [
    path('movies/', MovieListCreateView.as_view(), name='movie_list_create'),
    path('movies/random/', MovieRandomizerView.as_view(), name='movie-random'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDeleteView.as_view(), name='movie_detail'),
]
