import requests
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    content_html_file = open("content/index.html","r")
    content_html = content_html_file.read()
    context = {
        'title': 'Rudy Trubitt • Home',
        'content': content_html,
    }
    return render(request, 'base.html', context)



def contact(request):
    print('render contact page')
    content_html_file = open("content/contact.html","r")
    content_html = content_html_file.read()
    print(content_html)
    context = {
        'title': 'Contact',
        'content': content_html,
    }
    return render(request, 'base.html', context)


def github(request):
    # We can also combine Django with APIs
    content_html_file = open("content/github.html","r")
    content_html = content_html_file.read()    
    response = requests.get('https://api.github.com/users/rudytrubitt/repos')
    repos = response.json()
    context = {
        'title': 'Github Projects',
        'github_repos': repos,
        'content': content_html,
    }
    return render(request, 'base.html', context)

