from django.views import generic
from .models import Movie, Human


class IndexView(generic.ListView):
    template_name = 'index/index.html'
    context_object_name = 'movies'

    def get_queryset(self):
        set = Movie.objects.all().order_by('-imdb_rating', 'title').distinct('title', 'imdb_rating').filter(user_id=self.request.user.id)
        return set[:50]


class MovieView(generic.DetailView):
    model = Movie
    template_name = 'index/movie.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_subscribed'] = False
        if self.request.user:
            user = self.request.user
            movie = user.moviesubscription_set.filter(movie=self.kwargs['pk'])
            if movie:
                context['user_subscribed'] = True
        return context

class HumanView(generic.DetailView):
    model = Human
    template_name = 'index/human.html'
