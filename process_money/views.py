from django.shortcuts import render, HttpResponse, redirect 
import random
from time import localtime,strftime

# Funcion random
def randInt(min=0,max=100):
    num = (random.random() * (max-min)+min)
    return round(num)

#Funcion tiempo
def gettime():
    time =strftime("%b %d, %Y, %H:%M %p", localtime())
    return time


#Funcion index
def index(request):
    print("Ejecutado index")
    return render(request,'index.html')


#Función principal métodos post
def crear_datos(request):
    #Si no existen, lo creara
    if 'contador' not in request.session:
        request.session['contador'] = 0
    if 'contador1' not in request.session:
        request.session['contador1'] = 0
    else:
        request.session['contador1'] += 1
    if 'logs' not in request.session:
        request.session['logs'] = [] 
    color = ""
    textoadd = ""  
    texto = []  
    # a esta altura existen contadores y variables. 
    print("Ejecutado crear datos - Creacion variables")

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
        request.session['contador'] = request.session['contador'] + numero
        
        if numero>=0:
            color = "azul"
            textoadd = "Ganaste: " + str(numero) + " Gold desde " + opcion + "!  (" + gettime() + ")"
        else: 
            color = "rojo"
            textoadd = "Perdiste: " + str(numero) + " Gold desde " + opcion + " Sorry!  (" + gettime() + ")"
        print("Ejecutado crear datos - Post")

    datos_a_entregar = {
        'contador' : request.session['contador'], #Cuenta las monedas por jugada
        'contador1': request.session['contador1'], #Cuental el número de la jugada
        'color': color,
        'texto' : textoadd,
        }

    request.session['logs'].append(datos_a_entregar)
    request.session.save()
    print("Ejecutado crear datos")
    return redirect('/')

#Función para vaciar datos
def vaciar_datos(request):
    if 'contador' in request.session:
        del request.session['contador']
    if 'contador1' in request.session:
        del request.session['contador1']
    if 'logs' in request.session:
        del request.session['logs']
    crear_datos(request)
    print("Ejecutado vaciar datos")
    return redirect('/')
