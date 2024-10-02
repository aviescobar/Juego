import random

def escoger_palabra():
    palabras = ['python', 'programacion', 'ahorcado', 'desarrollador']
    return random.choice(palabras)

def jugar():
    palabra = escoger_palabra()
    intentos = 6
    letras_adivinadas = ['_'] * len(palabra)
    letras_intentadas = []

    while intentos > 0 and '_' in letras_adivinadas:
        print(" ".join(letras_adivinadas))
        letra = input("Adivina una letra: ").lower()

        if letra in letras_intentadas:
            print("Ya intentaste esa letra. Intenta otra.")
        elif letra in palabra:
            for idx, char in enumerate(palabra):
                if char == letra:
                    letras_adivinadas[idx] = letra
        else:
            intentos -= 1
            print(f"Letra incorrecta. Te quedan {intentos} intentos.")

        letras_intentadas.append(letra)

    if '_' not in letras_adivinadas:
        print(f"¡Ganaste! La palabra era {palabra}.")
    else:
        print(f"Perdiste. La palabra era {palabra}.")

jugar()
