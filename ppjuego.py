  
    # for i in range(15, len(tablero)):
    #     print(tablero[i])

from funcionesjuego import *
from preguntas import *
import csv


jugadores = []


tablero = [0, 1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 1, 0, 0, 2, 1, 1, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0]
ganador = 30
perdedor = 0
preguntas_usadas = []
jugar = True

jugador = input("¿Cómo te llamás?: ")
inicio = input("¿Estás listo para empezar a jugar? Si/No: ").lower()
while inicio != "si" and inicio != "no":
    inicio = input("Indicá una opción correcta. ¿Estás listo para empezar a jugar? Si/No:")

if inicio == "si":

    existe = buscar_jugadorexistente(jugador)
    if existe > -1:
        posicion = existe
        jugador_existente = {'nombre': jugador, 'posicion': {posicion}}
        jugadores.append(jugador_existente)
        print(f"Tu última posición registrada es: {posicion}")
    else:
        posicion = 15
        nuevo_jugador = {'nombre': jugador, 'posicion': posicion}
        jugadores.append(nuevo_jugador)

while jugar:
    pregunta = preguntar(preguntas, preguntas_usadas) 
    respuesta = pedir_respuesta()
    while respuesta != "a" and respuesta != "b" and respuesta != "c":
        print("Indicá una opción válida")
        respuesta = pedir_respuesta()
    acierto = validar_respuesta(preguntas, pregunta, respuesta)
    
    if acierto == True:
        print("¡Correcto! Avanzás")
        movimiento = 'avanzar'
        
    else:
        print("Incorrecto, retrocedés")
        movimiento = 'retroceder'

    nueva_posicion = mover_posicion(posicion, tablero, movimiento)
    posicion = nueva_posicion
    
    if posicion == ganador:
        print("¡Ganaste!")
        break
    elif posicion == perdedor:
        print("Perdiste")
        break
    elif (len(preguntas_usadas)) == 15:
        print("Perdiste, se agotaron las preguntas")
        break
    else:

        continuar = input("¿Querés seguir jugando? Si/No: ").lower()
        while continuar != "si" and continuar != "no":
            continuar = input("Indicá una opción correcta. ¿Querés seguir jugando? Si/No: ").lower()
        jugar = continuar == "si"

actualizar_jugador(jugador, posicion, jugadores)
guardar_jugador(jugadores)

print(f'{jugador}, tu puntaje es {posicion}. ¡Tu progreso se guardó con éxito!')
print("¡Hasta luego!")
