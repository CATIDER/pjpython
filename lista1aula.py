import time
jogos = []
preco = []
while True:
    x = int(input('''

1 - Adicionar jogo
2 - Remover jogo
3 - Ver lista
4 - Sair

'''))

    if(x == 1):
        j = input('qual jogo adicionar:').capitalize()
        if(j in jogos):
            z = 'Esse jogo já existe'
            for x in range(len(z)):
                print(z[x] , end = "")
                time.sleep(0.1)
            time.sleep(1.5)
        else:
            p = float (input('Qual o preço:'))
            jogos.append(j)
            jogos.append(p)

    elif(x == 2):
        j = input('Qual jogo remover:')
        if(j in jogos):
            i = jogos.index(j)
            jogos.remove(j)
            preco.pop(i)
        else:
            print('esse item não existe na lista')
    elif(x == 3):
        for x in range(len(jogos)):
            print(x+1, ':', jogos[x])
    elif(x == 4):
        break
    else:
        print('opção inválida')