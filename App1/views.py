from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Este es el index Principal de la APP1")

# Utilizando ruta dinámica
def saludar(request, estudiante):
    # message = f"Bienvenida {estudiante}"
    data = [1, 2, 3, 4]
    return render(request, "saludar.html", {"data": data})


def sumar(request, num1, num2):
    return HttpResponse(f"El resultado de la suma es { num1 + num2}")


def restar(request, num1, num2):
    return HttpResponse(f"El resultado de la resta es {num1 - num2}")


def multi(request, num1, num2):
    return HttpResponse(f"El resultado de la multiplicaicón es {num1 * num2}")


def dividir(request, num1, num2):
    return HttpResponse(f"El resultado de la multiplicaicón es {num1 / num2}")