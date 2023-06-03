from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import AddPlaceForm
from .models import Places


def index(request):
    '''Главная страница'''
    if request.user.is_authenticated:
        return redirect('list_places')
    return render(request, 'places/index.html', {'title': 'Главная страница'})


class PlacesView(ListView):
    model = Places
    template_name = 'places/list.html'
    context_object_name = 'places'
    extra_context = {'title': 'Воспоминания'}

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')
        return super(PlacesView, self).get(request)

    def get_queryset(self):
        queryset = Places.objects.filter(author=self.request.user)
        return queryset


class AddPlace(CreateView):
    model = Places
    form_class = AddPlaceForm
    template_name = 'places/add.html'
    success_url = reverse_lazy('list_places')

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')
        return super(AddPlace, self).get(request)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AddPlace, self).form_valid(form)
