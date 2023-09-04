while True:
    n= input('entrar ou criar usuario:')
    if n in['criar usuario','Criar usuario','CRIAR USUARIO', 'criar']:    
        print('Olá seja bem vindo ao nosso programa!')
        usr = input('indetifique o nome do usuario:')
        print('bem vindo', usr)

        senha = input('crie sua senha:')

        dica = input('uma dica das sua senha:')
        print('usuario criado!')


    lgn = input('você deseja entrar ou sair?')
    if lgn in ['entrar', 'ENTRAR', 'Entrar']:
            
        print('Olá seja bem vindo novamente ao nosso programa!')
        
        while True:
            usr2 = input('indetifique o nome do usuario:')
            if usr2 == usr:
                print('bem vindo novamente', usr)
                while True:
                    senha2 = input('digite sua senha:')
                    if senha2 == senha:
                        print('login correto!')
                        break
                    else:
                        print('senha incorreta, digite novamente!')
            else:
                print('usuário invalido, digite novamente!')
                
                    



