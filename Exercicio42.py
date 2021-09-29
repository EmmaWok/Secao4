print('Insira abaixo o salário base do funcionário:')
sal_b = float(input())
desc1 = (sal_b * 0.05)
desc2 = (sal_b * 0.93)
rec = desc1 + desc2
print(f'O salário do funcionário com descontos será de: {rec:.2f} R$.')
