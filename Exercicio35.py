import math
print('Insira os valores dos catetos para descobrir a hipotenusa')
print('Insira um cateto:')
Ha = float(input())
print('Insira outro cateto:')
Hb = float(input())
hipo = math.sqrt(Ha **2 + Hb **2)
print(f'A hipotenusa é: {hipo}')
