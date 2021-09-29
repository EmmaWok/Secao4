print('Insira abaixo o valor da hora de trabalho do funcionário:')
hr = float(input())
print('Agora insira o numero de horas trabalhado:')
num = float(input())
pag = hr * num * 0.90
print(f'O valor a ser pago para o funcionário é de: {pag} R$')
