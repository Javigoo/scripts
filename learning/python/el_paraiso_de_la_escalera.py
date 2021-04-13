#!/usr/bin/env python3

""" El paraiso de la escalera """

global distancia_entre_escalones

def calcular_numero_de_escalones(altura_escalera):
    return altura_escalera // distancia_entre_escalones # trunc(altura_escalera / distancia_entre_escalones)

def calcular_distancia_primer_y_ultimo_escalon(altura_escalera, numero_de_escalones):
    return ((altura_escalera / distancia_entre_escalones) - numero_de_escalones) / 2

def mostrar_escalera(altura_escalera, numero_de_escalones, distancia_primer_y_ultimo_escalon):
    numero_de_escalones = int(numero_de_escalones)
    print("\n")
    for step in range(numero_de_escalones+2):
        if step in [0, numero_de_escalones+1]:
            print("| |  } A =", distancia_primer_y_ultimo_escalon)
        else:
            print("|-|")

    print("\nEsta escalera tiene "+str(numero_de_escalones)+" escalones\n")

if __name__ == "__main__":
    distancia_entre_escalones = 0.4
    altura_escalera = float(input("Introduce la altura de la escalera: "))

    numero_de_escalones = calcular_numero_de_escalones(altura_escalera)
    distancia_primer_y_ultimo_escalon = calcular_distancia_primer_y_ultimo_escalon(altura_escalera, numero_de_escalones)
    
    mostrar_escalera(altura_escalera, numero_de_escalones, distancia_primer_y_ultimo_escalon)