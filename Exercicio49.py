print('Digite abaixo as Horas, os minutos e os segundos:')

print('Insira as horas:')
hora = int(input())

print('Minutos:')
minutos = int(input())

print('Segundos:')
segundos = int(input())

print('Insira agora a duração:')
duracao = int(input())

segundos_final = (segundos + duracao) % 60
minutos_final = (minutos + (segundos + duracao) // 60) % 60
hora_final = (hora + (minutos + (segundos + duracao) // 60) // 60) % 24

print(f'O final do evento irá ser ás: {hora_final}h {minutos_final}min e {segundos_final}seg.')
