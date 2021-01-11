#gioco "indovina numero"
from random import *
import os

def main():
    attempts = 6
    startInt = 1
    endInt = 100
    print("REGOLE")
    print("Hai "+ str(attempts)+ " tentativi per indovinare un numero casuale tra "+str(startInt)+" e "+ str(endInt))
    print("Inserire Q per terminare")
    print("Premere A per configurare il gioco")
    choice = input("Premere S per cominciare a giocare: ")
    choice = choice.upper()
    if choice == "Q":
        print("fine del programma.")
    elif choice == "A":
        config()
    elif choice == "S":
        game(attempts,startInt,endInt)
    else:
        print("input non valido!")
        print("")
        main()

def game(attempts,startInt,endInt):
    number = randint(startInt, endInt)
    i=0
    victory = False
    while i<attempts and not victory:
        try:
            scelta = input("inserisci numero intero o Q per chiudere: ")
            if scelta.isdigit():
                scelta = int(scelta)
                if scelta == number:
                    victory = True
                    print("Hai vinto!")
                elif scelta < number:
                    print("il numero inserito è troppo basso!")
                    i = i+1
                elif scelta > number:
                    print("il numero inserito è troppo alto!")
                    i = i+1
            else:
                scelta = scelta.lower()
                if scelta == "q":
                    print("Fine del gioco.")
                    break
                else:
                    print("Devi inserire un numero intero positivo!")
        except ValueError:
            print("Devi inserire un numero intero positivo!")
    if victory:
        print("Il numero era:", number)
    else:
        print("Hai perso!")
        print("il numero era:", number)

def config():
    try:
        attempts = int(input("Quanti tentativi vuoi avere? "))
        startInt = int(input("Da che numero vuoi partire?"))
        endInt = int(input("Fino a che numero?"))
        bool = True
        if startInt > endInt:
            print("Il numero di partenza deve essere più piccolo del numero finale!")
            bool = False
        elif attempts > abs(endInt-abs(startInt)):
            print("Troppi tentativi!")
            bool = False
        elif startInt <0:
            print("il numero di partenza deve essere intero e positivo")
            bool = False
        elif attempts<=0:
            print("il numero di tentativi deve essere intero e positivo")
            bool = False
    except ValueError:
        print("Input non valido")
        main()
    
    choice1 = input("(premere S per giocare qualsiasi altro tasto per tornare al menù principale: ")
    choice1 = choice1.upper()
    if choice1 == "S" and bool:
        game(attempts, startInt, endInt)
    else:
        main()

main()
os.system("PAUSE")


