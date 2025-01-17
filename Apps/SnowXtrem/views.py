from django.http import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserRegistration, UserEditForm


# Create your views here.

@login_required
def home(request):
    context = {
        "welcome": "Welcome to SnowXtrem"
    }
    return render(request, 'snowxtrem/home.html', context=context)

@login_required
def news(request):
    context = {
        "news": "News"
    }
    return render(request, 'snowxtrem/news.html', context=context)

@login_required
def parks(request):
    context = {
        "parks": "Parks"
    }
    return render(request, 'snowxtrem/parks.html', context=context)

@login_required
def gallery(request):
    context = {
        "gallery": "Gallery"
    }
    return render(request, 'snowxtrem/gallery.html', context=context)

def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(
                form.cleaned_data.get('password')
            )
            new_user.save()
            return render(request, 'snowxtrem/register_done.html')
    else:
        form = UserRegistration()

    context = {
        "form": form
    }

    return render(request, 'snowxtrem/register.html', context=context)


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        if user_form.is_valid():
            user_form.save()
            return render(request, 'snowxtrem/home.html')
    else:
        user_form = UserEditForm(instance=request.user)
    context = {
        'form': user_form,
    }
    return render(request, 'snowxtrem/edit.html', context=context)
