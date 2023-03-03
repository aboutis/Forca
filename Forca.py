from palavras import lista
import random
from art import tprint

tprint("FORCA", font="cybermedium")

escolha = random.choice(lista).lower()
espaco = []
for i in range(len(escolha)):
    espaco.append("_")

vidas = 6
while "_" in espaco:
    letra = input("Escolha uma letra: ").lower()
    if letra not in escolha:
        vidas -= 1
        print(f"Letra errada. Seu número de vidas é {vidas}.")
    if vidas == 0:
        tprint("VOCE  PERDEU")
        print(f"A palavra era: {escolha}")
        break
    for i in range(len(escolha)):
        if letra == escolha[i]:
            espaco[i] = letra
    print(espaco)

if "_" not in espaco:
    tprint("PARABENS  VOCE  GANHOU", font="cybermedium")
