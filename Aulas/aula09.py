frase = '  Curso em Video Python'
#frase = frase.replace('Python', 'Porno')
print(frase[3::2])

print('0i')

print("""Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().""")

print(frase.upper().count('O'))

print(len(frase.strip()))

print(frase.replace('Python' , 'Android'))

print(frase.lower().find('Video'))

dividido = frase.split()
print(dividido [2] [3])