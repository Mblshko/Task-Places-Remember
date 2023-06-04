from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.PlacesView.as_view(), name='list_places'),
    path('addplace/', views.AddPlace.as_view(), name='add_place'),
]