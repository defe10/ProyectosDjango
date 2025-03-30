from django.http import HttpResponse
from django.template import Template, Context

class Persona(object):# <------ Ejemplo de clase

    def __init__(self, nombre, apellido):

        self.nombre = nombre
        self.apellido = apellido
        

def saludo(request): # primera vista

    p1 = Persona ("Federico", "Casoni") #<-----clase
    # nombre = "Federico"
    # apellido = "Casoni"

    temas = ["modelos"] # <------ Ejemplo con lista
    
    doc_externo = open("/Users/hasguell/Documents/ProyectosDjango/Proyecto1/Proyecto1/plantilla/miplantilla.html")

    plt= Template(doc_externo.read()) # <----- abro template
    doc_externo.close()

    ctx = Context({"nombre_persona": p1.nombre, "apellido_persona": p1.apellido, "lista":temas}) # <----- hago contexto (diccionarios)

    documento = plt.render(ctx) # <----- renderizo

    return HttpResponse(documento)

