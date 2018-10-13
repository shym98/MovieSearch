from django.urls import include, path
from . import views


app_name = 'search'
urlpatterns = [
    path('', views.SearchView.as_view(), name='index'),
    path('movie', views.movie_search, name='movie'),
    path('human', views.human_search, name='human'),
    path('movie-request/<int:pk>', views.MovieRequestView.as_view(), name='movie_request'),
    path('human-request/<int:pk>', views.HumanRequestView.as_view(), name='human_request'),
    path('movie-subscribe/<int:pk>', views.movie_subscribe, name='movie_subscribe'),
    path('movie-unsubscribe/<int:pk>', views.movie_unsubscribe, name='movie_unsubscribe'),
]
