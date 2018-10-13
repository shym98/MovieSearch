from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registration', views.registration, name='registration'),
    path('profile', views.profile, name='profile'),
]
