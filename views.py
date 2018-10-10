import requests
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
    }
    return render(request, 'index.html', context)

def tech_writer(request):
    # Django comes with a "shortcut" function called "render", that
    # lets us read in HTML template files in separate directories to
    # keep our code better organized.
    context = {
        'name': 'Ash Ketchum',
        'pokemon': 'Pikachu',
    }
    return render(request, 'tech_writer.html', context)

def contact(request):
    # Django comes with a "shortcut" function called "render", that
    # lets us read in HTML template files in separate directories to
    # keep our code better organized.
    context = {

    }
    return render(request, 'contact.html', context)


def github(request):
    # We can also combine Django with APIs
    response = requests.get('https://api.github.com/users/rudytrubitt/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'github.html', context)

