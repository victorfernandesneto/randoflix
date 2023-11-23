from django.urls import path
from . import views


urlpatterns = [
    path('movies/', views.MovieListCreateView.as_view(), name='movie_list_create'),
    path('movies/random/', views.MovieRandomizerView.as_view(), name='movie-random'),
    path('movies/<int:pk>/', views.MovieRetrieveUpdateDeleteView.as_view(),
         name='movie_detail'),
]
