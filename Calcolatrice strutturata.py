#Scrivere un programma in python che calcoli: le 4 operazioni, la radice quadrata e l'elevamento a potenza,
#la somma dei primi n numeri naturali, la media tra m numeri, il fattoriale di un numero k.
#Usare le funzioni e creare un menù per scegliere l'operazione da eseguire.
from math import *
import os
def main():
    bool = True
    while bool != False:
        print()
        print("MENU': ")
        print("somma 'a', prodotto 'b', differenza 'c', divisione 'd', radice quadrata 'e', potenza 'f'")
        print("OPERAZIONI SPECIALI: ")
        print("somma dei primi n numeri naturali 'g', media tra m numeri 'h', fattoriale di k 'i'")
        print("Inserire 'q' per terminare, oppure scrivere 'quit'")
        scelta = input("Che operazione si desidera eseguire? ")
        scelta = scelta.lower()
        print()
        if scelta == "q" or scelta == "quit":
            bool = False
            print("Fine programma.")
        elif scelta == "a" or scelta == "somma":
            try:
                a = float(input("inserire numero (a): "))
                b = float(input("inserire numero (b): "))
                print("a+b = ",somma(a,b))
            except ValueError:
                print("Errore: a e b devono essere due numeri!")
        elif scelta == "b" or scelta == "prodotto":
            try:
                a = float(input("inserire numero (a): "))
                b = float(input("inserire numero (b): "))
                print("a*b = ",prodotto(a,b))
            except ValueError:
                print("Errore: a e b devono essere due numeri!")
        elif scelta == "c" or scelta == "differenza":
            try:
                a = float(input("inserire numero (a): "))
                b = float(input("inserire numero (b): "))
                print("a-b = ", differenza(a,b))
            except ValueError:
                print("Errore: a e b devono essere due numeri!")
        elif scelta == "d" or scelta == "divisione":
            try:
                a = float(input("inserire dividendo (a): "))
                b = float(input("inserire divisore (b): "))
                if b == 0:
                    print(divisione(a,b))
                else:
                    print("a/b = ",divisione(a,b))
            except ValueError:
                print("Errore: a e b devono essere due numeri!")
        elif scelta == "e" or scelta == "radice quadrata":
            try:
                r = float(input("inserire numero Reale (r): "))
                if r<0:
                    print("r^1/2 = i*",radice_quadrata(abs(r)),"(i è l'unità immaginaria)")
                else:
                    print("r^(1/2) = ",radice_quadrata(r))
            except ValueError:
                print("Errore: r deve essere un numero!")
        elif scelta == "f" or scelta == "potenza":
            try:
                q = float(input("inserire base (q): "))
                p = float(input("inserire potenza (p): "))
                potenza(q,p)
            except ValueError:
                print("Errore: q e p devono essere due numeri!")
        elif scelta == "g":
            n = input("inserire n (n deve essere un numero naturale positivo): ")
            if (not n.isdigit()):
                print("n deve essere un numero naturale positivo!")
            else:
                n = int(n)
                if(n%2!=0 and n%2!=1) or n==0:
                    print("n deve essere un numero naturale positivo! ")
                else:
                    print("somma = ",somma_primi_n_numeri_naturali(n))
        elif scelta == "h":
            m = input("inserire m (m deve essere un numero naturale positivo): ")
            if (not m.isdigit()):
                print("m deve essere un numero naturale positivo! ")
            else:
                m = int(m)
                if (m%2!=0 and m%2!=1) or m==0:
                    print("m deve essere un numero naturale positivo! ")
                else:
                    media_tra_m_numeri(m)
        elif scelta == "i" or scelta == "fattoriale":
            k = input("inserire k (k deve essere un numero naturale): ")
            if (not k.isdigit()):
                print("k deve essere un numero naturale!")
            else:
                k = int(k)
                if (k%2!=0 and k%2!=1):
                    print("k deve essere un numero naturale!")
                else:
                    print("k! = ",fattoriale(k))
        else:
            print("Errore: la scelta NON rientra tra quelle possibili")
            print("oppure il carattere digitato NON è tra quelli possibili")

def somma(a,b):
    return a+b

def prodotto(a,b):
    return a*b

def differenza(a,b):
    return a-b

def divisione(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Errore: impossibile dividere per zero"

def radice_quadrata(r):
    return sqrt(r)

def potenza(q,p):
    if q==0 and p==-1:
        print("Errore: non si può dividere per zero")
    elif q==0 and p==0:
        print("valore indeterminato")
    else:
        print("q^p = ", pow(q,p))

def somma_primi_n_numeri_naturali(n):
    somma = 0
    for i in range(n):
        somma = somma+i
    return somma

def media_tra_m_numeri(m):
    somma = 0
    i = 0
    while i<m:
        try:
            numero = float(input("inserisci numero: "))
            somma = somma + numero
            i=i+1
        except ValueError:
            print("Non ci possono essere caratteri tra gli m numeri!")
    media = somma/i
    print("media =",media)

def fattoriale(k):
    try:
        if k == 0:
            return 1
        else:
            return k*fattoriale(k-1)
    except RecursionError:
        print("il valore del fattoriale è troppo grande da calcolare!")
    except TypeError:
        return 

main()
os.system("PAUSE")
