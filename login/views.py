from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

def inicio(request):
    return render(request, 'inicio/inicio.html')

@login_required
def peliculas(request):
    return render(request, 'inicio/peliculas.html')

def login(request):
    return render(request, 'login/login.html')

def salir(request):
    logout(request)
    return redirect('inicio')