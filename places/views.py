from django.shortcuts import render


def index(request):
    '''Главная страница'''
    return render(request, 'places/index.html', {'title': 'Главная страница'})

def places_list(request):
    return render(request, 'places/list.html', {'title': 'Список мест'})

def place_add(request):
    return render(request, 'places/add.html', {'title': 'Добавить место'})