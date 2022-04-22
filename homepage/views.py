from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'homepage/index.html')


def projects(request):
    return render(request, 'homepage/projects.html')


def about(request):
    return render(request, 'homepage/about.html')


def contact(request):
    return render(request, 'homepage/contact.html')
