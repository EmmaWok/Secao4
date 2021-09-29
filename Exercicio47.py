print('digite um numero de 1000 a 9999 para ver 1 digito por linha:')
num = int(input())

while num<1000 or num> 9999:
    print('Número inválido')
    num = int(input())

num = str(num)

print(f'O primeiro digito é: {num[0]}')
print(f'O segundo digito é: {num[1]}')
print(f'O terceiro digito é: {num[2]}')
print(f'O quarto digito é: {num[3]}')
