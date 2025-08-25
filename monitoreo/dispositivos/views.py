from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    contexto = {"nombre": "Josh"}
    productos = [
        {"nombre":"Sensor 1", "valor": 100},
        {"nombre":"Sensor 2", "valor": 200},
        {"nombre":"Sensor 3", "valor": 300}
    ]

    return render(request, "dispositivos/inicio.html", {
        "contexto":contexto,
        "productos":productos
    })

def panel_dispositivos(request):
    dispositivos = [
        {"nombre":"Sensor Temperatura","consumo":50},
        {"nombre":"Medidor Solar","consumo":120},
        {"nombre":"Sensor Movimiento","consumo":30},
        {"nombre":"Calefactor","consumo":200},
    ]

    consumo_maximo = 100
    
    return render(request, "dispositivos/panel.html", {
        "dispositivos":dispositivos,
        "consumo_maximo":consumo_maximo
    })