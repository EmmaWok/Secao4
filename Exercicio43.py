print('Insira abaixo o valor do produto:')
prod = float(input())
desc = prod * 0.90
parc = prod / 3
comi = desc * 0.05
comi2 = prod * 0.05

print(f'O valor do produto com desconto é de: {desc:.2f} R$;')
print(f'O valor de cada parcela em 3x sem juros é de: {parc:.2f} R$;')
print(f'a comissão para o vendedor do produto com desconto é de: {comi:.2f} R$;')
print(f'A comissão do vendedor caso o produto seja parcelado é de: {comi2:.2f} R$.')
