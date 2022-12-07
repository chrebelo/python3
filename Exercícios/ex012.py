n = float(input('Qual o valor do produto? R$:'))
d = n - (n * 5 / 100)
print('Seu novo preço com 5% de desconto é R$:{:.2f}'.format(d))
