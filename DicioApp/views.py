from django.shortcuts import render
from dicio import Dicio

# Create your views here.

def Home(request):
    dicio = Dicio()
    search = request.GET.get('search')
    if search:
        word = dicio.search(search)
        tem_pesquisa = 1
        return (render(request, 'home.html', {'word': word, 'tem_pesquisa': tem_pesquisa}))
    else:
        tem_pesquisa = 0
        return (render(request, 'home.html', {'tem_pesquisa': tem_pesquisa}))