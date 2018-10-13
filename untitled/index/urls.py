from django.urls import path
from . import views


app_name = 'index'
urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('movie/<int:pk>', views.MovieView.as_view(), name='movie'),
    path('human/<int:pk>', views.HumanView.as_view(), name='human'),
]
