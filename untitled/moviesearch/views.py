from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Movie

def link_generator(title, genre, start_year, end_year):
    if genre == '---------':
        genre = ''
    if int(start_year) > int(end_year):
        start_year, end_year = end_year, start_year
    start_year += '-01-01'
    end_year += '-12-31'
    link = 'https://www.imdb.com/search/title?title=' + title + '&release_date=' + start_year + ',' + end_year + '&genres=' + genre + '&adult=include&count=1000'
    return link

class IndexView(generic.ListView):
    template_name = 'moviesearch/index.html'
    context_object_name = 'movies'

    def get_queryset(self):
        f = open("test", "w")
        f.write("test")
        return Movie.objects.order_by('-release')[:10]

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            title = request.POST.get('title_field', '')
            genre = request.POST.get('genre_field', '')
            start_year = request.POST.get('start_year', '')
            end_year = request.POST.get('end_year', '')
            print(link_generator(title, genre, start_year, end_year))
            return render(request, self.template_name)
        else:
            return Movie.objects.order_by('-release')[:10]