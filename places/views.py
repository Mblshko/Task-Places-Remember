from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import Places


def index(request):
    '''Главная страница'''
    if request.user.is_authenticated:
        return redirect('list')
    return render(request, 'places/index.html', {'title': 'Главная страница'})


class PlacesView(ListView):
    model = Places
    template_name = 'places/list.html'
    context_object_name = 'places'

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset().filter(author=request.user)
        return render(request, 'places/list.html', {'title': 'Воспоминания'})


def place_add(request):
    return render(request, 'places/add.html', {'title': 'Добавить воспоминание'})