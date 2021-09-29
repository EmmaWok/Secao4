print('Insira a quantidade de segundos:')
segundos = int(input())

minuto = segundos / 60
horas = minuto / 60

print(f'São {horas:.4f} Horas, {minuto:.4f} minutos e {segundos} segundos')
