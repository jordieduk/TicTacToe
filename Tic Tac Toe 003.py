'''Joc del 3 en ratlla'''

import random
import time
import os

def presentacion_1():
    #Retorna el nivell en que vol jugar l'usuari
    print()
    print("                TRES EN RAYA")
    print()
    print()
    print("                 1. Fàcil")
    print("                 2. Difícil")
    print()
    print()
    print()

    nivel = ""
    while nivel != "1" and nivel != "2":
        nivel=input("--> ")

    return int (nivel)


def presentacion_2():
    #Retorna la fitxa escollida per l'usuari i la fitxa del ordinador
    print()
    print("                TRES EN RAYA")
    print()
    print()
    print("                 Sale la ficha O")
    print("                 Elige: O/X")
    print()
    print()
    print()

    ficha = ""
    while ficha != "O" and ficha != "X":
        ficha = input("--> ").upper()

    if ficha == "O":
       humano = "O"
       ordenador = "X"
    else:
        humano = "X"
        ordenador = "O"

    return humano, ordenador 

def mostrar_tablero(tablero):
    #Mostra el tauler de joc amb les caselles buides i les fitxes posades.

    print()
    print("                TRES EN RAYA")
    print()
    print("     1       |2      |3")
    print("        {}    |  {}    |   {}".format(tablero[0], tablero[1], tablero[2]))
    print("             |       |")
    print("-------------+-------+--------")
    print("     4       |5      |6")
    print("        {}    |  {}    |   {}".format(tablero[3], tablero[4], tablero[5]))
    print("             |       |")
    print("-------------+-------+--------")
    print("     7       |8      |9")
    print("        {}    |  {}    |   {}".format(tablero[6], tablero[7], tablero[8]))
    print("             |       |")
    print()


def seguir_jugando():
    #Retornara True si l'usuari vol fer una altre partida, sino retorna false

    print()
    respuesta=input("         ¿Otra partida(s)?").lower()
    if respuesta == "s" or respuesta == "si":
        return True
    else:
        return False
 

def hay_ganador(tablero,jugador): #Aquesta funció pren dos parametres
    #Comproba si un estat del tauler es guanyador: si té 3 fitxes en ratlla

    if tablero[0] == tablero[1] == tablero[2] == jugador or \
       tablero[3] == tablero[4] == tablero[5] == jugador or \
       tablero[6] == tablero[7] == tablero[8] == jugador or \
       tablero[0] == tablero[3] == tablero[6] == jugador or \
       tablero[1] == tablero[4] == tablero[7] == jugador or \
       tablero[2] == tablero[5] == tablero[8] == jugador or \
       tablero[0] == tablero[4] == tablero[8] == jugador or \
       tablero[2] == tablero[4] == tablero[6] == jugador:   \

        return True
    else:
        return False
    
def tablero_lleno(tablero):
    #Retorna true si el tauler està ple i false si queden caselles buides.
    for i in tablero:
        if i == " ": #Si hi ha algun element a tablero que encara estigui buit
            return False

    return True

    
def casilla_libre(tablero,casilla):
    #Retorna true si una casella està buida i false si està plena
    return tablero[casilla] == " " 


def movimiento_jugador(tablero):
    #Retorna la casella escollida per la persona
    posiciones = ["1","2","3","4","5","6","7","8","9"]
    posicion = None
    while True:
        if posicion not in posiciones:
            posicion = input("      Et toca (1-9): ")
        else:
            posicion = int(posicion)
            if not casilla_libre(tablero, posicion-1):
                print("           Aquesta posició està ocupada")
            else:
                return posicion-1 #La lista tablero tiene los indices del 0-8, no del 1-9
            

def mov_ordenador_facil(tablero,jugador):
    #L'ordinador nomès es defensa de ser guanyat a la següent jugada

    ''' 
    for i in range (9):
        copia = list(tablero)
        if casilla_libre(copia,i)

    '''

    if tablero[0] == tablero[1] == jugador and tablero[2] == " ": #si tablero 0,1 están ocupadas por la ficha del jugador y tablero2 vacia...
        casilla = 2 #el ordenador decidirá y moverá a casilla 2 para contrarestrar que gane el jugador
    elif tablero[0] == tablero[2] == jugador and tablero[1] == " ":
        casilla = 1
    elif tablero[1] == tablero[2] == jugador and tablero[0] == " ":
        casilla = 0
        
    elif tablero[3] == tablero[4] == jugador and tablero[5] == " ":
        casilla = 5
    elif tablero[3] == tablero[5] == jugador and tablero[4] == " ":
        casilla = 4
    elif tablero[4] == tablero[5] == jugador and tablero[3] == " ":
        casilla = 3

    elif tablero[6] == tablero[7] == jugador and tablero[8] == " ":
        casilla = 8
    elif tablero[6] == tablero[8] == jugador and tablero[7] == " ":
        casilla = 7
    elif tablero[7] == tablero[8] == jugador and tablero[6] == " ":
        casilla = 6

    elif tablero[0] == tablero[3] == jugador and tablero[6] == " ":
        casilla = 6
    elif tablero[0] == tablero[6] == jugador and tablero[3] == " ":
        casilla = 3
    elif tablero[3] == tablero[6] == jugador and tablero[0] == " ":
        casilla = 0

    elif tablero[1] == tablero[4] == jugador and tablero[7] == " ":
        casilla = 7
    elif tablero[1] == tablero[7] == jugador and tablero[4] == " ":
        casilla = 4
    elif tablero[4] == tablero[7] == jugador and tablero[1] == " ":
        casilla = 1

    elif tablero[2] == tablero[5] == jugador and tablero[8] == " ":
        casilla = 8
    elif tablero[2] == tablero[8] == jugador and tablero[5] == " ":
        casilla = 5
    elif tablero[5] == tablero[8] == jugador and tablero[2] == " ":
        casilla = 2

    elif tablero[0] == tablero[4] == jugador and tablero[8] == " ":
        casilla = 8
    elif tablero[0] == tablero[8] == jugador and tablero[4] == " ":
        casilla = 4
    elif tablero[4] == tablero[8] == jugador and tablero[0] == " ":
        casilla = 0

    elif tablero[2] == tablero[4] == jugador and tablero[6] == " ":
        casilla = 6
    elif tablero[2] == tablero[6] == jugador and tablero[4] == " ":
        casilla = 4
    elif tablero[6] == tablero[4] == jugador and tablero[2] == " ":
        casilla = 2

    else: #si no se cumple ninguna de las anteriores, se elegirá de forma aleatoria una casilla vacia
        while True:
            casilla = random.randint(0,8)
            if tablero[casilla] == " ":
                break
            
    return casilla

def mov_ordenador_dificil(tablero,jugador,maquina):

    pass
        
#Programa principal del joc Tic Tac Toe

jugando = True

while jugando:

    tablero = [" "] * 9 #S'ha de crear el tauler de joc amb 9 espais buits

    os.system("cls")

    nivel=presentacion_1() #Cridem a la funció

    os.system("cls")

    humano,ordenador = presentacion_2() #cridem a la funció, ens retornaràla fitxa del jugador i la del ordinador

    os.system("cls")

    mostrar_tablero(tablero) #mostrarem el tauler buit al principi de la partida

    if humano == "O":
        turno = "Humano" #Indica si es "O" que comença el jugador humà, sinó, ordinador.
    else:
        turno = "Ordenador"
        
    partida = True

    while partida:

        if tablero_lleno(tablero): #si el tauler està ple mostrarem un empat
            print("           Empate")
            partida = False

        elif turno == "Humano": #si el torn és del jugador humà
            casilla = movimiento_jugador(tablero) #Cridem a la funció i ens retorna la casella o mou el jugador
            tablero[casilla]=humano
            turno="Ordenador" #Canviem el torn
            os.system("cls")
            mostrar_tablero(tablero)
            if hay_ganador(tablero, humano): #comprobem si hi ha guanyador
                print("          Has guanyat!")
                partida=False

        elif turno == "Ordenador":
            print("        L'ordinador està pensant...")
            time.sleep(2)
            if nivel == 1:
                casilla = mov_ordenador_facil(tablero,humano)
            elif nivel == 2:
                casilla = mov_ordenador_dificil(tablero,ordenador,humano)
            tablero[casilla] = ordenador
            turno = "Humano"
            os.system("cls")
            mostrar_tablero(tablero)
            
            if hay_ganador(tablero,ordenador):
                print("          Has perdut!")
                partida = False

jugando = seguir_jugando()
