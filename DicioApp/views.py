from django.shortcuts import render
from dicio import Dicio

# Create your views here.

def Home(request):
    dicio = Dicio()
    search = request.GET.get('search')
    if search:
        word = dicio.search(search)   
        return (render(request, 'home.html', {'word': word}))
    else:
        return (render(request, 'home.html'))