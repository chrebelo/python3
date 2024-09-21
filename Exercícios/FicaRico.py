from random import sample

q = int(input('Quantas apostas gerar? '))
nums = [sample(range(1,25), k=15) for x in range(0,q)]

for i in range(0,q):
    print(f'Aposta {i+1}: {sorted(nums)[i]}')
