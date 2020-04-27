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


#Programa principal del joc Tic Tac Toe

nivel=presentacion_1() #Cridem a la funció
if nivel==1:
    print("Has escollit nivell fàcil")
else:
    print("Has escollit nivell difícil")

os.system("cls")

humano,ordenador = presentacion_2() #cridem a la funció, ens retornaràla fitxa del jugador i la del ordinador

print("Tu has escollit:")
print(humano)
print("Ordinador juga amb:")
print(ordenador)
    

