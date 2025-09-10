from django.shortcuts import render
from .models import Car

def index(request):
    cars = Car.objects.all()
    return render(request, 'index.html', {'cars': cars})