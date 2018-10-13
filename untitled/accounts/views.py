from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from pyArango.connection import *
import datetime

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            email = form.data.get('email')
            if email:
                user.email = email
                user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)

            conn = Connection(username='root', password='1111')
            db = conn["Logs"]
            allLogs = db["all"]
            registerLogs = db["register"]
            doc = allLogs.createDocument()

            user_id = str(user.id)
            cur_time = str(datetime.datetime.now())

            doc["userId"] = user_id
            doc["email"] = user.email
            doc["password"] = raw_password
            doc["type"] = 'registration'
            doc["time"] = cur_time
            key = ('registration_' + user_id + '_' + cur_time).replace(' ', '_')
            doc._key = key
            doc.save()

            registerLog = registerLogs.createDocument()
            registerLog["userId"] = user_id
            registerLog["email"] = user.email
            registerLog["password"] = raw_password
            registerLog["time"] = cur_time
            key = (user_id + '_' + cur_time).replace(' ', '_')
            registerLog._key = key
            registerLog.save()

            login(request, user)

            return redirect('index:home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/registration.html', { 'form': form })


@login_required
def profile(request):
    tab = request.GET.get('tab')
    if tab == 'movie_request':
        tab_ind = 1
        profile_tab = 'accounts/profile_movie_request_tab.html'

    elif tab == 'human_request':
        tab_ind = 2
        profile_tab = 'accounts/profile_human_request_tab.html'
    elif tab == 'movie_subscription':
        tab_ind = 3
        profile_tab = 'accounts/profile_movie_subscription_tab.html'
    else:
        tab_ind = 1
        profile_tab = 'accounts/profile_movie_request_tab.html'
    return render(request, 'accounts/profile.html', {
        'tab_ind': tab_ind,
        'profile_tab': profile_tab
    })
