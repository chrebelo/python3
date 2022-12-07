d = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km rodou? '))
valor = (60 * d) + (0.15 * km)
print('O total a pagar é R$:{:.2f}'.format(valor))
