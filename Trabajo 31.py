# Solicitar ingresar la cantidad de días del año
ingreso = int(input("Ingrese la cantidad de días del año:"))

# Imprimir el resultado
print("Es un:")

# Condiciones
if ingreso/4!=0:
    print ("año común")
else:
    ingreso/100!=0
    print ("año bisiesto")
if ingreso/400!=0:
    print ("año común")
else:
    ingreso/400==0
    print ("año bisiesto")


    
