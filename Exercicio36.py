import math
print('insira a altura e o raio do cilindro para descobrir o volume')
print("insira abaixo a altura:")
altura = float(input())
print("insira abaixo o raio:")
raio = float(input())
V = math.pi * raio**2 * altura
print(f'o volume do cilíndro é de: {V:.2f}')
