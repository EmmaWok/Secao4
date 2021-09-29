Exercício 51: # Calcular distancia entre o ponto x e y.

print('Insira abaixo uma distancia "x" e uma "y":')
print('Insira a distância "x":')
x = float(input())
print('Insira a distância "y"')
y = float(input())
# elevar à uma fracão corresponde a tirar a raiz tendo como com indice
#  número indicado no denominador
distancia = int((((0 - x) ** 2) + ((0 - y) ** 2)) ** (1 / 2))

print(f'A distância entre a origem (0,0) e o ponto de'
      f' coordenadas ({x},{y})é: {distancia}')

# Demonstrando o cálculo

print(f'x2 - x1 = {0 - x}, \n'
      f'y2 - y1 = {0 - y}')
print(f'(x2 - x1) ** 2 = {(0 - x) ** 2}, \n'
      f'(y2 - y1) ** 2 = {(0 - y) ** 2}')

print(f'Distância da origem = {distancia}')
