from django.urls import path
from movies.views import MovieListView


urlpatterns = [
    path('movies/', MovieListView.as_view(), name='movie_list_view')
]