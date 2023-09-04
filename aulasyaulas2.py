import random

senha = random.randint(1,20)

for i in range(5):
    s = int(input('informe a senha:'))
    if(senha == s):
        print('você acertou!')
        break
    else:
        print('você errou!')

print('a senha era',senha)

