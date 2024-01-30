numero_secreto = 42

while True:
    try:
        numero_usuario = int(input("¡Intenta adivinar el número secreto del mauo! Ingresa un númmero entero:"))
        break
    except ValueError:
        print("Por favor, ingresa un número entero válildo.")

while numero_usuario !=numero_secreto:
    print("¡Ja, ja! ¡Estás en mi bucle!")

    while True:
        try:
            numero_usuario = int(input("Intenta adivinar de nuevo. Ingresa un número entero:"))
            break
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

    print("¡Bien hecho, muggle! Eres libre ahora. El número secreto del mago era:", numero_secreto)
