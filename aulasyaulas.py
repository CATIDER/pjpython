import random

X = random.randint(0,10)
#print(X)
ip = input('escolha par ou impar:')
N = int(input('escolha um número:'))
soma = X+N

print('o computador jogou',X)
if(soma%2==0):
    print('deu par')
    resultado = 'par'
else:
    print('deu impar')
    resultado = 'impar'

if(ip == resultado):
    print('deu',resultado,'. você ganhou!')
else:
    print('deu',resultado,'. você perdeu!')
