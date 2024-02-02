temps = [[0.0 for h in range(24)] for d in range(31)]

highest = -100.0

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("La temperatura más alta fue:", highest)
