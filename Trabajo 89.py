def es_bisiesto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

anno_prueba = 2024
resultado = es_bisiesto(anno_prueba)

if resultado:
    print(f"{anno_prueba} es un año bisiesto.")
else:
    print(f"{anno_prueba} no es un año bisiesto.")

