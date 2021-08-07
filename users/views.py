from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created successfully. You may now log in.")            
            return redirect('dashboard-home')

    else:
        form = UserRegistrationForm()
    context = {
        'form' : form,
    }
    return render(request, "users/register.html", context )

def profile(request):
    return render(request, 'users/profile.html')