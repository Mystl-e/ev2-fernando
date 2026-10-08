from django.urls import path
from . import views

app_name = 'home_fernando'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('generos/<slug:slug>/', views.genero_detalle, name='genero_detalle'),
]