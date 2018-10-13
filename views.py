import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect

import os

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


mailgun_api_key = os.environ["MAILGUN_API_KEY"]

def send_email(request):
  name = request.POST["name"]
  email = request.POST["email"]
  message = request.POST["message"]
  print('in the send_mail function',name,email,message)
  return redirect('/')
# Do something with these three variables... return redirect("/") # Return a redirect!

# def send_email(request):
#     return requests.post(
#         "https://api.mailgun.net/v3/sandbox707f318e9d3449bda7397c824329e068.mailgun.org/messages",
#         auth=("api", mailgun_api_key),
#         data={"from": "Excited User <mailgun@sandbox707f318e9d3449bda7397c824329e068.mailgun.org>",
#               "to": ["rudy@trubitt.com"],
#               "subject": "Contact form email",
#               "text": message})


''' reference - this curl command works
curl -s --user 'api:XXXXXXXXXXXXXXXXX' \
    https://api.mailgun.net/v3/sandbox707f318e9d3449bda7397c824329e068.mailgun.org/messages \
    -F from='Excited User <mailgun@sandbox707f318e9d3449bda7397c824329e068.mailgun.org>' \
    -F to=rudy@trubitt.com \
    -F subject='Hello' \
    -F text='Testing some Mailgun awesomeness!'  

    '''