import calendar

def dias_en_mes(ano, mes):

    if 1<= mes <=12:
        return calendar.monthrange(ano, mes)[1]
    else:
        raise ValueError("El mes debe estar en el rango de 1 a 12.")

anno_prueba = 2022
mes_prueba = 2

try:
    num_dias = dias_en_mes(anno_prueba, mes_prueba)
    print(f"El número de días en el mes {mes_prueba} del año {anno_prueba} es: {num_dias} días.")
except ValueError as e:
    print(e)
