print('Digite um numero 100 a 999 e veja ele ao contrário:')

num = int(input())
while num <100 or num > 999:
    print('Numero inválido. Digite um numero 100 a 999 e veja ele ao contrário:')
    num = int(input())

num = str(num)
reverter = num[::-1]
print(f'O numero que você digitou ao contrário é: {reverter}.')
