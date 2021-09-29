premio = 780000.00
ganhador1 = premio * 0.46
ganhador2 = premio * 0.32
ganhador3 = premio - ganhador1 - ganhador2

print(f'O primeiro ganhador receberá: {ganhador1:.2f};')
print(f'O segundo receberá: {ganhador2:.2f};')
print(f'O terceiro receberá: {ganhador3:.2f}.')
