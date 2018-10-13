from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('index.urls')),
    path('search/', include('search.urls')),
    path('accounts/', include('accounts.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
