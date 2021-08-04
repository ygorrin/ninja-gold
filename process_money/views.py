from django.shortcuts import render, HttpResponse, redirect 
import random
from time import localtime,strftime


"""
def randInt(min=0,max=100):
    num = (random.random() * (max-min)+min)
    return round(num)
print(randInt(10,20))
"""
texto = []
def index(request):
    if 'contador' in request.session:
        pass
    else:
        request.session['contador'] = 0

    context = {
        "palabra" : 'palabra',
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
    print("opcion:", request.POST['option'])
    valor = int(request.POST['option'])
    if valor == 1:
        numero = randInt(10,20)
        card = "Farm"
    elif request.POST['option'] ==2:
        print("Entré en la opcion 2")
    elif request.POST['option'] ==3:
        print("Entré en la opcion 3")
    elif request.POST['option'] ==4:
        print("Entré en la opcion 4")

    print("Valor Inicial: ",request.session['contador'])
    request.session['contador'] += numero
    if numero>=0:
        textoadd = "Ganaste: " + str(numero) + " Gold desde la " + card+ "!  (" + gettime() + ")"
    else: 
        textoadd = "Perdiste: " + str(numero) + " Gold desde la " + card+ " Sorry!  (" + gettime() + ")"
    print("Random: ", numero , "Request: ", request.session['contador'], textoadd)
    texto.append(textoadd)

    context = {
        'contador':  request.session['contador'],
        'texto': texto,
    }
    return render(request, 'index.html', context)
