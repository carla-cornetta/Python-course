# Solicitar el ingreso del usuario
ingreso = float(input("Ingrese el monto de ingreso anual:"))

#Definir las constantes para los cálculos
limite_ingreso = 85528
exencion_fiscal = 556.02
impuesto_base = 14839.02
porcentaje_excedente = 0.32

# Calcular el impuesto
if ingreso <= limite_ingreso:
    impuesto = round(0.18 * ingreso - exencion_fiscal)
else:
    impuesto = round (impuesto_base + porcentaje_excedente * (ingreso - limite_ingreso))
    
# Asegurarse de que el impuesto no sea negativo
impuesto = max(impuesto, 0)

# Imprimir el impuesto calculado
print("El impuesto calculado es:", impuesto, "pesos")
