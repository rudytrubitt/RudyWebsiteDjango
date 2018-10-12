import requests
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # content_html_file = open("content/index.html","r")
    # content_html = content_html_file.read()
    context = {
        'title': 'Rudy Trubitt • Home',
       
    }
    return render(request, 'index.html', context)



def contact(request):
    print('render contact page')
    # content_html_file = open("content/contact.html","r")
    # content_html = content_html_file.read()
    #print(content_html)
    context = {
        'title': 'Contact',
    }
    return render(request, 'contact.html', context)


def github(request):
    my_github_url_path = 'https://github.com/rudytrubitt/'
    response = requests.get('https://api.github.com/users/rudytrubitt/repos')
    repos = response.json()
    context = {
        'title': 'Github Projects',
        'github_repos': repos,
        'my_github_url_path' : my_github_url_path
    }
    return render(request, 'github_repo_list.html', context)

