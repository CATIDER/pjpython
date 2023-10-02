nomes = ['vitinho']
senhas = ['1410']
import time

while True:
    n = int(input('''
   ---- MENU ----
                
   1 - CADASTRAR
   2 - ENTRAR
   3 - SAIR
   -------------
   '''))
    if (n == 1):    
        print('Olá seja bem vindo ao nosso programa!')
        while True:
            usr = input('indetifique o nome do usuario:')
            if(usr in nomes):
                print('este nome já está sendo usado.')
            else:
                print('bem vindo', usr)
                break

        while True:
            senha = input('crie sua senha:')
            confirmar = input('confirme sua senha:')
            if(senha == confirmar):
                print('usuario criado!')
                break
            else:
                print('as senhas não se correspondem!')
        
        nomes.append(usr)
        senhas.append(senha)

    elif (n == 2):
            
        print('Olá seja bem vindo novamente ao nosso programa!')
        
        while True:
            conectado = 0
            usr = input('indetifique o nome do usuario:')
            if(usr in nomes):
                print('bem vindo novamente', usr)
                while True:
                    senha = input('digite sua senha:')
                    if (senha == senhas [nomes.index(usr)]):
                        print('login correto!')
                        conectado = 1
                        break
                    else:
                        print('senha incorreta, digite novamente!')
            else:
                print('usuário invalido, digite novamente!')
            if(conectado == 1):
                break

        
        
        tc=('''Olá, Somos uma empresa de produtos Apple, iremos passar para você os melhores preços do mercado conforme suas respostas!
                
                                                           Vamos lá?''')
        for x in range(len(tc)):
            print(tc[x], end='')
            time.sleep(0.02)
              
        aparelhos = int(input('''
    Qual aparelho é do seu interesse?
                
            1 - IPhone
            2 - AirPods
            3 - MacBook
            4 - Apple Watch
            
            -------------
                              ''')) 

        if (aparelhos == 1):
            iphone = int(input('''
     Qual modelo de Iphone você se interessa?
                
            1 - 11
            2 - 12
            3 - 13
            4 - 14
            5 - 15                   '''))
            if (iphone == 1):
                gb = int(input('''
        Quantos GB você se interessa?
                    
                1 - 64gb
                2 - 128gb
                3 - 256gb
                              '''))
                if (gb == 1):
                    iphone = int(input('''
                    IPhone 11 64 gb
                        
                    11 - https://www.alloallo.com/br/refurbished-iphone/iphone-11/64-gb/
                    11 Pro - https://www.alloallo.com/br/refurbished-iphone/iphone-11-pro/64-gb/
                    11 ProMax - https://www.alloallo.com/br/refurbished-iphone/iphone-11-pro-max/midnight-green-64-gb/
                                    '''))
                elif(gb == 2):
                    iphone = int(input('''
                    IPhone 11 128 gb
                    
                    11 - https://www.mercadolivre.com.br/apple-iphone-11-128-gb-branco/p/MLB15149568?matt_tool=18956390&utm_source=google_shopping&utm_medium=organic&from=gshop
                    11 Pro - https://www.alloallo.com/br/refurbished-iphone/iphone-11-pro/256-gb/
                     
                        
                   
                                    '''))
                elif (gb == 3):
                    iphone = int(input('''
                    IPhone 11 256 gb
                    
                    11 - https://www.outletdocelular.com.br/iphone/iphone-11-256gb-seminovo?variant_id=5765&parceiro=2710&srsltid=AfmBOoq5njopg49i2cdHIX0UYnc4R5VLGJf80HOBePUYwOisqqbyRmAhw7E
                    11 Pro - https://www.mercadolivre.com.br/iphone-11-pro-256-gb-dourado/p/MLB15150716?matt_tool=18956390&utm_source=google_shopping&utm_medium=organic&from=gshop
                    11 ProMax - https://www.taqi.com.br/seminovo-iphone-11-pro-max-dourado-256gb/220551?srsltid=AfmBOoptjJh7De4ENuhXWHT-oiH76vX0ciEpfVTrTnTqiOCVx42VvsfY9D4   
                   
                                    '''))
            

    elif (n == 3):
        print('volte sempre!')
    

