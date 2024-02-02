temps = [[0.0 for h in range(24)] for d in range(31)]

hot_days = 0

for day in temps:
    if day[11] > 20.0:
        hot_days += 1

print(hot_days, "fueron los días calurosos.")
