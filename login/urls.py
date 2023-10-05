from django.urls import path, include
from .views import inicio, peliculas, login, salir

urlpatterns = [
    path('', inicio, name="inicio"),
    path('peliculas/', peliculas, name="peliculas"),
    path('login/', login, name="login"),
    path('salir/', salir, name="salir"),
]