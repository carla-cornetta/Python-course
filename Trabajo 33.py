odd_numbers = 0
even_numbers = 0

number = int(input("Introduce un número o escribe 0 para detener:"))

while number != 0:
    if number % 2 ==1:
        odd_numbers +=1

    else:
        even_numbers +=1
    number = int(input("Introduce un número o escribe 0 para detener:"))

print("Conteo de números impares:", odd_numbers)
print("Conteo de números pares", even_numbers)
