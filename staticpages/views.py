from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    context = {}
    return render(request, 'staticpages/index.html', context)


def about(request):
    context = {}
    return render(request, 'staticpages/about.html', context)

def musicas(request):
    context = {}
    return render(request, 'staticpages/musicas.html', context)