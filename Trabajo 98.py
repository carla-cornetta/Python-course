try:
    value = int(input('Ingresa un número natural:'))
    print('El recíproco de', value, 'es', 1/value)
except ValueError:
    print('No sé qué hacer con', value)
except ZeroDivisionError:
    print('La división entre cero no está permitida en nuestro Universo.')
