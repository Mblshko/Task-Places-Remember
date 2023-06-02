from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('list/', views.places_list, name='list'),
    path('add/', views.place_add, name='add'),
]