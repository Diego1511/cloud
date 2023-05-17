from django.shortcuts import render
from django.http import HttpResponse
from . import models


def projects(request):
    return render(request, 'registro.html')


def project(request):
        return render(request, 'registro.html')


def registro(request):
    if request.metod == 'POST':
        Nombre = request.POST['Nombre']
        Apellidos = request.POST['Apellidos']

        user=models.project()
        user.is_activate=1
        user.Nombre = Nombre
        user.Apellidos = Apellidos
        user.save()

    return render(request, 'registro.html')

