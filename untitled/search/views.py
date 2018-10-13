import subprocess, datetime
from subprocess import Popen, PIPE, STDOUT

from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from index.models import Request
from .models import MovieRequest, HumanRequest, MovieSubscription
from index.models import Movie

from pyArango.connection import *

from search.models import MovieRequest, HumanRequest


class SearchView( generic.TemplateView):
    template_name = 'search/search.html'

@login_required
def movie_search(request):
    if request.method == 'POST':

        movie_request_model = MovieRequest()
        movie_request_model.user = request.user
        movie_request_model.title = request.POST.get('title')
        if request.POST.get('year_from'):
            movie_request_model.year_from = request.POST.get('year_from')
        if request.POST.get('year_to'):
            movie_request_model.year_to = request.POST.get('year_to')
        movie_request_model.genre = request.POST.get('genre')
        errors = movie_request_model.is_valid()

        title = str(request.POST.get('title', '')).lower().replace(' ', '+')
        genre = request.POST.get('genre', '')
        if genre != '---------':
            genre = genre.lower().replace('-', '_')
        year_from = request.POST.get('year_from', '')
        year_to = request.POST.get('year_to', '')
        movie_request = title + ' ' + genre + ' ' + year_from + ' ' + year_to
        new_request = Request(user_id=request.user.id, request=movie_request)
        new_request.save()

        requests = Request.objects.filter(user_id=str(request.user.id), request=str(movie_request))[:1].get()
        request_id = requests.id

        conn = Connection(username='root', password='1111')
        db = conn["Logs"]
        allLogs = db["all"]
        msLogs = db["movie_search"]
        doc = allLogs.createDocument()

        user_id = str(request.user.id)
        cur_time = str(datetime.datetime.now())

        doc["userId"] = user_id
        doc["type"] = 'movie search'
        doc["request"] = movie_request
        doc["time"] = cur_time
        key = ('movie-search_' + user_id + '_' + cur_time).replace(' ', '_')
        doc._key = key
        doc.save()

        msLog = msLogs.createDocument()
        msLog["userId"] = user_id
        doc["request"] = movie_request
        msLog["time"] = cur_time
        key = (user_id + '_' + cur_time).replace(' ', '_')
        msLog._key = key
        msLog.save()

        if len(errors) == 0:
            movie_request_model.save()
            command = 'python titleScraping.py ' + str(request_id) + ' ' + movie_request
            currentPath = 'C:\\Users\\shym9\\PycharmProjects\\MovieProj'
            p = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, cwd=currentPath)
            subprocess.Popen(
                'python manage.py runscript setToDB --script-args result' + str(request_id) + '.json ' + str(
                    request.user.id) + ' ' + str(MovieRequest.objects.filter(user_id=request.user.id).order_by('-id')[0].id))
            return redirect('index:home')
        else:
            return render(request, 'search/movie_search.html', {'errors': '\n'.join(errors)})
    return render(request, 'search/movie_search.html')

@login_required
def human_search(request):
    if request.method == 'POST':
        name = str(request.POST.get('name', '')).lower().replace(' ', '+')
        startYear = str(request.POST.get('year_from'))
        endYear = str(request.POST.get('year_to'))
        profession = str(request.POST.get('profession'))
        new_request = Request(user_id=request.user.id, request=name)
        new_request.save()
        requests = Request.objects.filter(user_id=str(request.user.id), request=str(name))[:1].get()
        request_id = requests.id

        human_request = HumanRequest()
        human_request.user = request.user
        human_request.name = request.POST.get('name')
        if request.POST.get('year_from'):
            human_request.living_year_from = request.POST.get('year_from')
        if request.POST.get('year_to'):
            human_request.living_year_to = request.POST.get('year_to')
        human_request.profession = request.POST.get('profession')
        errors = human_request.is_valid()

        conn = Connection(username='root', password='1111')
        db = conn["Logs"]
        allLogs = db["all"]
        hsLogs = db["human_search"]
        doc = allLogs.createDocument()

        user_id = str(request.user.id)
        cur_time = str(datetime.datetime.now())

        doc["userId"] = user_id
        doc["type"] = 'human search'
        doc["request"] = name
        doc["time"] = cur_time
        key = ('human-search_' + user_id + '_' + cur_time).replace(' ', '_')
        doc._key = key
        doc.save()

        hsLog = hsLogs.createDocument()
        hsLog["userId"] = user_id
        doc["request"] = name
        hsLog["time"] = cur_time
        key = (user_id + '_' + cur_time).replace(' ', '_')
        hsLog._key = key
        hsLog.save()

        if len(errors) == 0:
            human_request.save()
            command = 'python humanScraping.py ' + str(request_id) + ' ' + name
            currentPath = 'C:\\Users\\shym9\\PycharmProjects\\MovieProj'
            p = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, cwd=currentPath)
            subprocess.Popen(
                'python manage.py runscript setHumanToDB --script-args resultHuman' + str(request_id) + '.json ' + str(
                    request.user.id) + ' ' + startYear + ' ' + endYear + ' ' + profession + ' ' + str(HumanRequest.objects.filter(user_id=request.user.id).order_by('-id')[0].id))
            return redirect('index:home')
        else:
            return render(request, 'search/human_search.html', {'errors': '\n'.join(errors)})
    return render(request, 'search/human_search.html')

class SearchView(generic.TemplateView):
    template_name = 'search/search.html'


class MovieRequestView(LoginRequiredMixin, generic.DetailView):
    template_name = 'search/movie_request.html'
    model = MovieRequest

    def get_queryset(self):
        return MovieRequest.objects.filter(user=self.request.user)

class HumanRequestView(LoginRequiredMixin, generic.DetailView):
    template_name = 'search/human_request.html'
    model = HumanRequest
    def get_queryset(self):
        return HumanRequest.objects.filter(user=self.request.user)


@login_required
def movie_subscribe(request, pk):
    subscription = MovieSubscription()
    subscription.user = request.user
    subscription.movie = get_object_or_404(Movie, pk=pk)
    subscription.save()
    subprocess.Popen(
        'python manage.py runscript subscr --script-args ' + str(request.user.id) + ' movie ' + str(subscription.movie.id) + ' week')
    return redirect('index:movie', pk)

@login_required
def movie_unsubscribe(request, pk):
    subscription = get_object_or_404(MovieSubscription, user=request.user, movie=pk)
    conn = Connection(username='root', password='1111')
    db = conn["Logs"]
    subscriptions = db["subscriptions"]
    key = str(request.user.id) + '_movie_' + str(subscription.movie.id)
    subscriptions[key].delete()
    subscription.delete()
    return redirect('index:movie', pk)