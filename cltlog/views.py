from django.shortcuts import render
from dashboard.views import apps # for nav links
from .models import Entry
from django.contrib.auth.models import User

def home(request):
    context = {
        'title' : 'Daily Output Log',
        'apps' : apps,
        'entries' : Entry.objects.all()
    }
    return render(request, 'cltlog/home.html', context)