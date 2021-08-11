from django.contrib.auth.forms import UsernameField
from django.shortcuts import render
from dashboard.views import apps # for nav links
from .models import Entry
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    context = {
        'title' : 'Daily Output Log',
        'apps' : apps,
        'entries' : request.user.entry_set.all()
    }
    return render(request, 'cltlog/home.html', context)