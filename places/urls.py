from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('list/', views.PlacesView.as_view(), name='list'),
    path('add/', views.place_add, name='add'),
]