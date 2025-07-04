
tablero = [0, 1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 1, 0, 0, 2, 1, 1, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0]

from preguntas import *
import random
import csv
import os


def preguntar(lista, preguntas_usadas:list):
    """
    Función que muestra una pregunta aleatoria con sus opciones de respuestas, retorna la pregunta
    lista = lista donde se encuentran las preguntas
    preguntas_usadas = lista donde se revisa que la pregunta no haya sido preguntada antes
    Retorna la pregunta aleatoria
    """
    while True:
        pregunta = random.choice(preguntas)
        for e_pregunta in preguntas_usadas:
            if e_pregunta == pregunta:
                break
        else:
            preguntas_usadas.append(pregunta)
            print(pregunta["pregunta"])
            print(f" a: {pregunta['respuesta_a']}\n b: {pregunta['respuesta_b']}\n c: {pregunta['respuesta_c']}")
            return pregunta

def mostrar_opciones(pregunta, preguntas):
    for e_pregunta in preguntas:
        if e_pregunta == pregunta:
            opciones = [pregunta['respuesta_a'], pregunta['respuesta_b'], pregunta['respuesta_c']]
    return opciones

def pedir_respuesta():
    """
    Función que pide y retorna la respuesta
    """
    return input("Indique su respuesta: ")


def validar_respuesta(lista, pregunta, respuesta):
    """
    Función que valida si la respuesta es correcta
    lista = lista de preguntas y respuestas
    pregunta = pregunta que se hizo anteriormente
    respuesta = respuesta del usuario
    Retorna bool mediante variable "acierto"
    """
    acierto = None
    for e_pregunta in preguntas:
        if e_pregunta == pregunta:
            if e_pregunta['respuesta_correcta'] == respuesta:
                acierto = True
            else:
                acierto = False
    return acierto

def mover_posicion(posicion, tablero, movimiento):
    """
    Función que mueve la posición del usuario
    posicion = posicion actual
    tablero = lista de posiciones
    movimiento = avanzar o retroceder
    Retorna la nueva posicion
    """
    nueva_posicion = 0
    if movimiento == 'avanzar':
        posicion = posicion + 1
        nueva_posicion = posicion + tablero[posicion]
    else:
        posicion = posicion - 1
        nueva_posicion = posicion - tablero[posicion]
    if nueva_posicion >= len(tablero):
        nueva_posicion = len(tablero) - 1
    elif nueva_posicion < 0:
        nueva_posicion = 0
    return nueva_posicion
    
def buscar_jugadorexistente(jugador)->int:
    """
    Función que identifica si el nombre del jugador ya existe en el archivo csv de jugadores
    jugador = nombre del jugador actual
    Retorna la posicion del jugador ya existente o -1 en caso de que no exista
    """
    posicion = -1
    with open ("historialjugadores.csv", 'r') as file:
        lector = csv.DictReader(file)
        for e_jugador in lector:
            if jugador == e_jugador['nombre']:
                posicion = int(e_jugador['posicion'])
                break
    return posicion


def actualizar_jugador(jugador, posicion, jugadores):
    """
    Función que actualiza la posicion del jugador
    jugador = jugador actual
    posicion = posicion actualizada del jugador
    jugadores = lista de diccionarios de los jugadores
    Retorna los datos del jugador
    """
    for e_jugador in jugadores:
        if e_jugador['nombre'] == jugador:
            e_jugador['posicion'] = posicion
        return e_jugador

def guardar_jugador(lista: list):
     """
    Función que guarda al jugador y su posicion en el archivo csv
    lista = lista de diccionarios de los jugadores
    """
     encabezados = ['nombre', 'posicion']
     with open('historialjugadores.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=encabezados)
        writer.writeheader()
        writer.writerows(lista)


def cargar_puntajes()-> list:
    """
    Función que pasa los jugadores de un archivo a una lista
    list = lista donde se agregarán los jugadores
    Retorna la lista
    """
    lista = []
    with open('historialjugadores.csv', 'r') as file:
        lector = csv.DictReader(file)
        for fila in lector:
            nombre = fila["nombre"]  
            posicion = int(fila["posicion"])  
            lista.append((nombre, posicion))  
    return lista


def ordenar_puntajes(lista):
    """
    Función que ordena los puntajes de mayor a menor
    """
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i][1] < lista[j][1]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

# def mostrar_puntajes(list):
#     for i in range(len(list)):
#         print(list[i])