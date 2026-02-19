from random import randint
pc = randint(0, 5) #faz o pc pensar
print('-=-' *20)
print('Vou pensar em um número entre 0 e 5. Tente Acertar! ')
print('-=-' *20)
jogador = int(input('Digite um número: ')) #Jogador tenta adivinhar
if jogador == pc:
    print('Parabéns... Acertou!')
else:
    print('Ganhei! Eu escolhi {} e você {}.'.format(pc, jogador))
