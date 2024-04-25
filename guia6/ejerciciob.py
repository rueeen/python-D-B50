# 14:0:0
# 14:0:1
# 14:0:2

for horas in range(14, 16):
    for minutos in range(0, 60):
        for segundos in range(0, 60):
            print(f'{horas}:{minutos}:{segundos}')
            if horas == 15 and segundos == 0:
                break
        if horas == 15 and minutos == 0:
            break

             