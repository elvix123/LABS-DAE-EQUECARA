from django.shortcuts import render

from django.http import HttpResponse 

 

def index(request): 

    return HttpResponse("Desde la visa de encuestas!") 

def detalle(request, pregunta_id): 

    return HttpResponse("Estas viendo la pregunta %s." % pregunta_id) 

 

def resultados(request, pregunta_id): 

    response = "Estas viendo los resultado de la pregunta %s." 

    return HttpResponse(response % pregunta_id) 

 

def votar(request, pregunta_id): 

    return HttpResponse("Estas votando por la pregunta %s." % pregunta_id) 


def sumar(request, pregunta_id, pregunta_id2):

    Operacion = pregunta_id + pregunta_id2
    Resultado = "Resultado: La suma de %s + %s =  %s" %(pregunta_id,pregunta_id2,Operacion)

    return HttpResponse(Resultado)

def restar(request, pregunta_id, pregunta_id2):

    Operacion = pregunta_id - pregunta_id2
    Resultado = "Resultado: La resta de %s - %s =  %s" %(pregunta_id,pregunta_id2,Operacion)

    return HttpResponse(Resultado)

def multiplicar(request, pregunta_id, pregunta_id2):

    Operacion = pregunta_id * pregunta_id2
    Resultado = "Resultado: La multiplicacion de %s * %s =  %s" %(pregunta_id,pregunta_id2,Operacion)

    return HttpResponse(Resultado) 