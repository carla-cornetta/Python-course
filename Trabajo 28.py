# Se leen tres números.

number1 = int(input("Ingresa el primer número:"))
number2 = int(input("Ingresa el segundo número:"))
number3 = int(input("Ingresa el tercer número:"))

# verifica cuál de los números es el mayor
#pásalo a la variable largest_number.

largest_number = max(number1, number2, number3)

# Imprime el resultado.
print("El número más grande es:", largest_number)
