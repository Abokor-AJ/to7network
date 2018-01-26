from django.shortcuts import render


def index(request):
    return render(request, 'to7network/index.html', {'index': 'index'})
