import pygame
from tablero import *
from funcionespygame import *
from preguntas import *

# agregar sonido
# solucionar opción ver puntaje (del más alto al más)
# agregar opciones para salir durante el juego


pygame.init()

ANCHO_VENTANA = 800
ALTO_VENTANA = 800
naranja = (200, 109, 91)
blanco = (255,255,255)

pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

pygame.display.set_caption("Escaleras y serpientes")

pygame.mixer.init()
sonido_fondo = pygame.mixer.Sound("forest.wav")
volumen = 0.09
sonido_fondo.set_volume(volumen)

inicio = pygame.image.load("inicio.png")
inicio = pygame.transform.scale(inicio, (800,800))

menu = pygame.image.load("menu.png")
menu = pygame.transform.scale(menu, (800,800))

jugar = pygame.image.load("jugar.png")
jugar = pygame.transform.scale(jugar, (800,800))

intro = pygame.image.load("intro1.png")
intro = pygame.transform.scale(intro,(800, 800))

intro_dos = pygame.image.load("intro2.png")
intro_dos = pygame.transform.scale(intro_dos, (800, 800))

intro_tres = pygame.image.load("intro3.png")
intro_tres = pygame.transform.scale(intro_tres, (800, 800))

pantalla_puntajes = pygame.image.load("puntajes.png")
pantalla_puntajes = pygame.transform.scale(pantalla_puntajes, (800,800))

pantalla_nombre = pygame.image.load("nombre.png")
pantalla_nombre = pygame.transform.scale(pantalla_nombre, (800,800))

pantalla_pregunta = pygame.image.load("tableropregunta.png")
pantalla_pregunta = pygame.transform.scale(pantalla_pregunta, (800,800))

pantalla_ganaste = pygame.image.load("ganaste.png")
pantalla_ganaste = pygame.transform.scale(pantalla_ganaste, (800,800))

pantalla_perdiste = pygame.image.load("perdiste.png")
pantalla_perdiste = pygame.transform.scale(pantalla_perdiste, (800,800))



# botones

font_input = pygame.font.SysFont("Arial", 40)
font = pygame.font.SysFont("Arial", 20)
font_puntajes = pygame.font.SysFont("Arial", 40)

ingreso_rect = pygame.Rect(265,550,270,70)


boton_menu_jugar = pygame.Rect(253, 271, 290, 70)
boton_menu_puntajes = pygame.Rect(253, 406, 290, 70)
boton_menu_salir = pygame.Rect(253, 542, 290, 70)
boton_siguiente = pygame.Rect(268, 618, 270,70)
boton_jugar = pygame.Rect(265, 550, 270, 70)
boton_salir = pygame.Rect(305, 669, 200, 50)
botona = pygame.Rect(91, 622, 220, 45)
botonb = pygame.Rect(491, 622, 220, 45)
botonc = pygame.Rect(286, 689, 220, 45)
boton_si = pygame.Rect(91, 622, 220, 45)
boton_no = pygame.Rect(491, 622, 220, 45)
boton_final_salir = pygame.Rect(151, 622, 220, 45)
boton_final_volverajugar = pygame.Rect(439, 617, 220, 45)


#  personaje

personaje = pygame.image.load("personaje_parado.gif.gif")
personaje = pygame.transform.scale(personaje, (50,50))

personaje_aterriza = pygame.image.load("personaje_aterriza.gif.gif")
personaje_aterriza = pygame.transform.scale(personaje_aterriza, (50,50))

tablero = [0, 1, 0, 0, 0,3, 0, 0, 0, 0, 0, 1, 0, 0, 2, 1, 1, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0]
casilleros = [casillero_uno, casillero_dos, casillero_tres, casillero_cuatro, casillero_cinco, casillero_seis, casillero_siete, casillero_ocho, casillero_nueve, casillero_diez, casillero_once, casillero_doce, casillero_trece, casillero_catorce, casillero_quince, casillero_dieciseis, casillero_diecisiete, casillero_dieciocho, casillero_diecinueve, casillero_veinte, casillero_veintiuno, casillero_veintidos, casillero_veintitres, casillero_veinticuatro, casillero_veinticinco, casillero_veintiseis, casillero_veintisiete, casillero_veintiocho, casillero_veintinueve, casillero_treinta ,casillero_meta]
preguntas_usadas = []
jugadores = [
]

posicion = 0
puntaje = str(posicion+1)
ingreso = ""
respuesta = None
acierto = None
movimiento = ""
esperar_click_suelto = False
timer = pygame.USEREVENT + 1
pygame.time.set_timer(timer, 1000)
tiempo = 0
textotiempo = font.render(str(tiempo), True, blanco)
tiempo_respuesta = None
tiempo_inicio_tablero = None
tiempo_introduccion = None
tiempo_final = None
reinicio = False
flag_correr = True
estado = "inicio"

pregunta = preguntar(preguntas, preguntas_usadas)
opciones = mostrar_opciones(pregunta, preguntas)

while flag_correr:

    sonido_fondo.play()
    lista_eventos = pygame.event.get()

    for evento in lista_eventos:

        if esperar_click_suelto:
            if evento.type == pygame.MOUSEBUTTONUP:
                esperar_click_suelto = False
            continue
        
        if evento.type == pygame.MOUSEBUTTONDOWN:
             print(evento.pos)

        if evento.type == pygame.QUIT:
            flag_correr = False

        if estado == "tablero" and evento.type == timer and acierto == None:
            tiempo += 1
            textotiempo = font.render(str(tiempo), True, blanco)
            if tiempo == 11:
                tiempo = 10
                acierto = False
                correcto = font.render("Se agotó el tiempo, retrocedés", True, blanco)
                tiempo_respuesta = pygame.time.get_ticks()
                movimiento = "retroceder"
                mover = True
                estado = "validando"


        elif estado == "menu":
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_menu_jugar.collidepoint(evento.pos):
                    estado = "pantallanombre"
                elif boton_menu_puntajes.collidepoint(evento.pos):
                    estado = "puntajes"
                elif boton_menu_salir.collidepoint(evento.pos):
                    flag_correr = False

        elif estado == "pantallanombre" and evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_BACKSPACE:
                ingreso = ingreso[:-1]
            else:
                ingreso += evento.unicode
            if evento.key == pygame.K_RETURN:
                estado = "intro"
                jugador = ingreso.strip()
                existe = buscar_jugadorexistente(jugador) 
                if existe > -1:
                    posicion = existe
                else:
                    posicion = 15
                    nuevo_jugador = {'nombre': jugador, 'posicion': posicion}
                    jugadores.append(nuevo_jugador)
            puntaje = str(posicion+1)

    if estado == "inicio":
        pantalla.blit(inicio, (0,0))
        if not esperar_click_suelto and evento.type == pygame.MOUSEBUTTONDOWN:
            estado = "menu"
            esperar_click_suelto = True
    
    if estado == "menu":
        pygame.draw.rect(pantalla, naranja, boton_menu_jugar)
        pygame.draw.rect(pantalla, naranja, boton_menu_puntajes)
        pygame.draw.rect(pantalla, naranja, boton_menu_salir)
        pantalla.blit(menu, (0,0))
    
    if estado == "puntajes":
        lista_jugadores = cargar_puntajes()
        ordenar_puntajes(lista_jugadores)
        pantalla.blit(pantalla_puntajes, (0,0))
        y = 335
        for nombre, posicion in lista_jugadores: 
            texto = font_puntajes.render(f"{nombre}:     {posicion}", True, blanco)
            pantalla.blit(texto, (200, y))
            y += 40

    if estado == "pantallanombre":
        pygame.draw.rect(pantalla, naranja, ingreso_rect , 2)
        pantalla.blit(pantalla_nombre, (0,0)) 
        font_input_surface = font_input.render(ingreso, True, blanco) 
        pantalla.blit(font_input_surface, ( ingreso_rect.x+5 , ingreso_rect.y + 5 ))
    
    if estado == "intro":
        pygame.draw.rect(pantalla, naranja, boton_siguiente)
        pantalla.blit(intro, (0,0))
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_siguiente.collidepoint(evento.pos):
                estado = "intro_dos"
                tiempo_introduccion = pygame.time.get_ticks()

    
    if estado == "intro_dos":
        if pygame.time.get_ticks() - tiempo_introduccion > 500:
            pygame.draw.rect(pantalla, naranja, boton_siguiente)
            pantalla.blit(intro_dos, (0,0))
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_siguiente.collidepoint(evento.pos):
                    tiempo_introduccion = pygame.time.get_ticks()
                    estado = "intro_tres"
                    
                    
    if estado == "intro_tres":
        pantalla.blit(intro_tres, (0,0))
        if pygame.time.get_ticks() - tiempo_introduccion > 1000:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_siguiente.collidepoint(evento.pos):
                    estado = "jugar"
            
    if estado == "jugar":
        pygame.draw.rect(pantalla, naranja, boton_jugar)
        pygame.draw.rect(pantalla, naranja, boton_salir)
        pantalla.blit(jugar, (0,0))
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_jugar.collidepoint(evento.pos):
                estado = "tablero"
                tiempo_inicio_tablero = pygame.time.get_ticks() 
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_salir.collidepoint(evento.pos):
                    flag_correr = False
        
    if estado == "tablero":

        if reinicio == True:
            pregunta = preguntar(preguntas, preguntas_usadas)
            opciones = mostrar_opciones(pregunta, preguntas)
            reinicio = False
        elif reinicio == False:
            pygame.draw.rect(pantalla, naranja, botona)
            pygame.draw.rect(pantalla, naranja, botonb)
            pygame.draw.rect(pantalla, naranja, botonc)
            pantalla.blit(pantalla_pregunta, (0,0))
            pantalla.blit(personaje_aterriza, casilleros[posicion])
            textopuntaje = font.render(puntaje, True, blanco)
            textopregunta = font.render(pregunta["pregunta"], True, blanco)
            textoopciona = font.render(opciones[0], True, blanco)
            textoopcionb = font.render(opciones[1], True, blanco)
            textoopcionc = font.render(opciones[2], True, blanco)
            opciona = font.render("a:", True, blanco)
            opcionb = font.render("b:", True, blanco)
            opcionc = font.render("c:", True, blanco)
            pantalla.blit(textotiempo, (80, 425))
            pantalla.blit(textopuntaje, (80,102))
            pantalla.blit(textopregunta, (29, 550))
            pantalla.blit(opciona, (85, 631))
            pantalla.blit(textoopciona, (115, 631))
            pantalla.blit(opcionb, (485, 631))
            pantalla.blit(textoopcionb, (515, 631))
            pantalla.blit(opcionc, (286, 698))
            pantalla.blit(textoopcionc, (316, 698))


            if pygame.time.get_ticks() - tiempo_inicio_tablero > 300:
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if botona.collidepoint(pos):
                        respuesta = "a"
                    elif botonb.collidepoint(pos):
                        respuesta = "b"
                    elif botonc.collidepoint(pos):
                        respuesta = "c"
    
    if respuesta is not None and estado == "tablero":
        acierto = validar_respuesta(preguntas, pregunta, respuesta)
        mover = True

        if acierto == True:
            pantalla.blit(pantalla_pregunta, (0,0))
            pantalla.blit(personaje, casilleros[posicion])
            correcto = font.render("¡Correcto! Avanzás", True, blanco)
            movimiento = "avanzar"

        if acierto == False:
            pantalla.blit(pantalla_pregunta, (0,0))
            pantalla.blit(personaje, casilleros[posicion])
            correcto = font.render("Incorrecto, retrocedés", True, blanco)
            movimiento = "retroceder"

        tiempo_respuesta = pygame.time.get_ticks()
        estado = "validando"
    
    if estado == "validando":
        if pygame.time.get_ticks() - tiempo_respuesta > 1000:
            pantalla.blit(pantalla_pregunta, (0,0))
            pantalla.blit(personaje, casilleros[posicion])
            pantalla.blit(correcto, (264 ,549))
            
            if pygame.time.get_ticks() - tiempo_respuesta > 2000:
                if mover == True:
                    
                    posicion = mover_posicion(posicion, tablero, movimiento)
                    puntaje = str(posicion+1)

                    if posicion == 30:
                        estado = "ganador"
                        tiempo_final = pygame.time.get_ticks()

                    elif posicion == 0:
                        estado = "perdedor"

                    elif (len(preguntas_usadas)) == 15:
                        estado = "preguntas_agotadas"
                    
                    else:
                        estado = "posicion_actualizada"
    
    if estado == "ganador":
        pygame.draw.rect(pantalla, naranja, boton_final_salir)
        pygame.draw.rect(pantalla, naranja, boton_final_volverajugar)
        pantalla.blit(pantalla_ganaste, (0,0))
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_final_salir.collidepoint(evento.pos):
                flag_correr = False
            elif boton_final_volverajugar.collidepoint(evento.pos):
                estado = "pantallanombre"
                

    if estado == "perdedor" and estado == "preguntas_agotadas":
        pygame.draw.rect(pantalla, naranja, boton_final_salir)
        pygame.draw.rect(pantalla, naranja, boton_final_volverajugar)
        pantalla.blit(pantalla_perdiste, (0,0))
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_final_salir.collidepoint(evento.pos):
                flag_correr = False
            elif boton_final_volverajugar.collidepoint(evento.pos):
                estado = "pantallanombre"


    if estado == "posicion_actualizada":
        pantalla.blit(pantalla_pregunta, (0,0))
        pantalla.blit(personaje, casilleros[posicion])
        estado = "preguntar_continuar"   
        mover = False 

    if estado == "preguntar_continuar":
        continuar = font.render("¿Querés seguir jugando?", True, blanco)
        opcion_si = font.render("Si", True, blanco)
        opcion_no = font.render("No", True, blanco)
        pygame.draw.rect(pantalla, naranja, boton_si)
        pygame.draw.rect(pantalla, naranja, boton_no)
        pantalla.blit(pantalla_pregunta, (0,0))
        pantalla.blit(personaje, casilleros[posicion])
        pantalla.blit(continuar, (264 ,549))
        pantalla.blit(opcion_si, (183, 631))
        pantalla.blit(opcion_no, (590, 631))


        if evento.type == pygame.MOUSEBUTTONDOWN:
            reinicio = True
            respuesta = None
            movimiento = ""
            mover = True
            esperar_click_suelto = True
            pos = pygame.mouse.get_pos()
            tiempo_inicio_tablero = pygame.time.get_ticks()

            if boton_si.collidepoint(pos):
                estado = "tablero"
                esperar_click_suelto = True
                tiempo_inicio_tablero = pygame.time.get_ticks()
                acierto = None
                tiempo = 0

            elif boton_no.collidepoint(pos):
                actualizar_jugador(jugador, posicion, jugadores)
                guardar_jugador(jugadores)
                esperar_click_suelto = True
                ingreso = ""
                estado = "inicio"
                tiempo = 0
    
        
    pygame.display.flip()

sonido_fondo.stop()
pygame.quit()



