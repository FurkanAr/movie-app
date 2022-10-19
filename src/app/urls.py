from django.urls import path
from .views import home, getProfileList, createProfile, getMovies, getMovieDetail, playMovie

app_name = 'app'

urlpatterns = [
    path('', home, name='Home'),
    path('profiles/', getProfileList, name='profile_list'),
    path('profiles/create', createProfile, name='create_profile'),
    path('watch/<str:profile_id>', getMovies, name='movie_list'),
    path('watch/detail/<str:movie_id>', getMovieDetail, name='movie_detail'),
    path('watch/play/<str:movie_id>', playMovie, name='play_movie'),

]