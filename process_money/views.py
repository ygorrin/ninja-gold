from django.shortcuts import render, HttpResponse, redirect 
import random
from time import localtime,strftime

texto = []
def index(request):
    if 'contador' in request.session:
        pass
    else:
        request.session['contador'] = 0

    context = {
        "contador": request.session['contador'],
    }
    return render(request,'index.html', context)

def randInt(min=0,max=100):
    num = (random.random() * (max-min)+min)
    return round(num)

def gettime():
    time =strftime("%b %d, %Y, %H:%M %p", localtime())
    return time

def process_money(request):
    if request.POST:
        print("opcion:", request.POST['opcion'])
        opcion = request.POST['opcion']
        if opcion == "granja":
            numero = randInt(10,20)
        elif opcion == "cueva":
            numero = randInt(5,10)
        elif opcion == "casa":
            numero = randInt(2,5)
        elif opcion =="casino":
            numero = randInt(-50,50)

    print("Valor Inicial: ",request.session['contador'])
    request.session['contador'] += numero
    if numero>=0:
        color = "blue"
        textoadd = "Ganaste: " + str(numero) + " Gold desde la " + opcion + "!  (" + gettime() + ")"
    else: 
        color = "red"
        textoadd = "Perdiste: " + str(numero) + " Gold desde la " + opcion + " Sorry!  (" + gettime() + ")"
    print("Random: ", numero , "Request: ", request.session['contador'], textoadd)
    texto.append(textoadd)

    context = {
        'contador':  request.session['contador'],
        'texto': texto,
        'color' : color,
    }
    return render(request, 'index.html', context)
