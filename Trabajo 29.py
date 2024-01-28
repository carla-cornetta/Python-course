cadena_ingresada = input("Ingrese la cadena:")

if cadena_ingresada == "ESPATIFILO":
    print("Si - ¡El Espatifilo! es la mejor planta de todos los tiempos")
elif cadena_ingresada == "espatifilo":
    print("No, ¡quiero un gran Espatifilo!")
else:
    print("¡Espatifilo!, ¡No{}".format(cadena_ingresada))
