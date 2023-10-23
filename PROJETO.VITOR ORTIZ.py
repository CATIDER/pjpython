nomes = ['vitinho']
senhas = ['1410']
import time

def buscarLink():
        aparelhos = int(input('''
    Qual aparelho é do seu interesse?
                
            1 - IPhone
            2 - AirPods
            3 - iPad
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
                    iphone = input('''
                    IPhone 11 64 gb
                        
                    11 - https://www.alloallo.com/br/refurbished-iphone/iphone-11/64-gb/
                    11 Pro - https://www.alloallo.com/br/refurbished-iphone/iphone-11-pro/64-gb/
                    11 ProMax - https://www.alloallo.com/br/refurbished-iphone/iphone-11-pro-max/midnight-green-64-gb/
                                    ''')
                elif(gb == 2):
                    iphone = input('''
                    IPhone 11 128 gb
                    
                    11 - https://www.mercadolivre.com.br/apple-iphone-11-128-gb-branco/p/MLB15149568?matt_tool=18956390&utm_source=google_shopping&utm_medium=organic&from=gshop
                    11 Pro - https://www.alloallo.com/br/refurbished-iphone/iphone-11-pro/256-gb/
                     
                        
                   
                                    ''')
                elif (gb == 3):
                    iphone = input('''
                    IPhone 11 256 gb
                    
                    11 - https://www.outletdocelular.com.br/iphone/iphone-11-256gb-seminovo?variant_id=5765&parceiro=2710&srsltid=AfmBOoq5njopg49i2cdHIX0UYnc4R5VLGJf80HOBePUYwOisqqbyRmAhw7E
                    11 Pro - https://www.mercadolivre.com.br/iphone-11-pro-256-gb-dourado/p/MLB15150716?matt_tool=18956390&utm_source=google_shopping&utm_medium=organic&from=gshop
                    11 ProMax - https://www.taqi.com.br/seminovo-iphone-11-pro-max-dourado-256gb/220551?srsltid=AfmBOoptjJh7De4ENuhXWHT-oiH76vX0ciEpfVTrTnTqiOCVx42VvsfY9D4   
                   
                                    ''')
                
            elif (iphone == 2):
                gb = int(input('''
        Quantos GB você se interessa?
                    
                1 - 64gb
                2 - 128gb
                3 - 256gb
                              '''))
                if(gb == 1):
                    iphone = input('''
                    IPhone 12 64 gb
                                       
                    12 - https://www.amazon.com.br/Apple-MHDA3BR-A-iPhone-11-64-GB/dp/B08M3KL2JK/ref=asc_df_B08M3KL2JK/?tag=googleshopp00-20&linkCode=df0&hvadid=381869163568&hvpos=&hvnetw=g&hvrand=12439548575935657696&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9102423&hvtargid=pla-1053345204238&psc=1
                    
                
                    
                        
                   
                                    ''')
                elif(gb == 2):
                    iphone = input('''
                    IPhone 12 128 gb
                    
                    12 - https://www.carrefour.com.br/celular-apple-iphone-12-branco-128gb-vitrineseminovo-carregador-e-cabo-mp934109459/p?utm_medium=sem&utm_source=google_pmax_3p&utm_campaign=3p_performancemax_Eletro_Smartphone&gclid=CjwKCAjwyY6pBhA9EiwAMzmfwYKjpsICQvdYK1OQC1gkacgl3Wc_jBaNw7Y1q1v4QqjHKxHgzBDCVxoCwC0QAvD_BwE
                    12 pro - https://loja.switchphone.com.br/iphone-12-pro-128gb-prateado-novo?srsltid=AfmBOoqB15worH-1j4dUItJIjDPKtF2tO6WLAZWTVMnbV5vRH6ufiafIl8Y
                    12 ProMax - https://alifone.com.br/produto/iphone-12-pro-max-seminovo/?attribute_capacidade=128GB&attribute_cor=Dourado&srsltid=AfmBOorgWgbpyetHQEJtlIIEewziLG0T7vrSXyCP-tFDxwVgh2YIw540nXM
                
                        
                   
                                    ''')
                elif (gb == 3):
                    iphone = input('''
                    IPhone 12 256 gb
                    
                    12 - https://www.trocafy.com.br/iphone-12-256gb-azul-tenho-minhas-marcas-de-uso-2254/p?idsku=942&srsltid=AfmBOoptXx2Kiu4f7KLI1cvSEAZQYc-j3X-RMjI0rJ1wavCCOCDdwzk3qeM
                    12 Pro - https://www.casasbahia.com.br/usado-iphone-12-pro-256gb-grafite-excelente-trocafone-1557925377/p/1557925377?utm_medium=Cpc&utm_source=google_freelisting&IdSku=1557925377&idLojista=33013&tipoLojista=3P
                    12 ProMax - https://alifone.com.br/produto/iphone-12-pro-max-seminovo/?attribute_capacidade=256GB&attribute_cor=Dourado&srsltid=AfmBOoq2Ubag-zQ3FY37TOSkELF6JXc4iEKIpDVyQh3orPgjj7etk9o3GT4
                    
                     
                   
                                    ''')
            elif (iphone == 3):
                gb = int(input('''
        Quantos GB você se interessa?
                    
                1 - 128gb
                2 - 256gb
                3 - 512gb
                              '''))  
                if(gb == 1):
                    iphone = input('''
                    IPhone 13 128 gb
                                       
                    13 - https://www.iplace.com.br/apple-iphone-13-128gb-estelar-mlpg3br-a/220851?srsltid=AfmBOoqX3Cv3gnMnUwkm9u5jMnR1huvpTgHU03ZicFo9wZRLvuHQ40_iJCs
                    13 pro - https://www.horizonplay.com.br/apple/apple-iphone-13-pro-128gb-vitrine-tela-super-retina-xdr-oled-6-1?variant_id=21543&parceiro=8926&srsltid=AfmBOorzbaI4iv0HkAbBJC6EJnaT7onZm-MezSHCUmaXY48Nr5rxAV61BYA
                    13 ProMax - https://www.horizonplay.com.br/apple/apple-iphone-13-pro-max-128gb-vitrine-tela-super-retina-xdr-oled-6-7?variant_id=21563&parceiro=8926&srsltid=AfmBOoqJorzAwtFuZfOgS6Xy-nQAwsapDCbPXE8BMz3jZqL5W1G_xFIen80
                
                    
                        
                   
                                    ''')
                elif(gb == 2):
                    iphone = input('''
                    IPhone 13 256 gb
                    
                    13 - https://www.amazon.com.br/Apple-iPhone-13-256-GB-Meia-noite/dp/B09T57QT9Y?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&psc=1&smid=A1ZZFT5FULY4LN
                    13 pro - https://horizonplay.com.br/apple/apple-iphone-13-pro-256gb-vitrine-tela-super-retina-xdr-oled-6-1?variant_id=21555&parceiro=8926&srsltid=AfmBOoq3kReDucRS7Xo82LKo_oJ5DTpKMRDBdNN1rzlaRsro43x9CsrtC9Y
                    13 ProMax - https://www.amazon.com.br/Apple-iPhone-13-256-GB-Meia-noite/dp/B09T57QT9Y?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&psc=1&smid=A1ZZFT5FULY4LN
                    
                   
                                       
                   
                                    ''')
                elif (gb == 3):
                    iphone = input('''
                    IPhone 13 512 gb
                    
                    13 - https://www.iplace.com.br/apple-iphone13-512gb-productred-mlqf3br-a/220850?srsltid=AfmBOoo7uyQ5cI9X9J84742iC9zEMuVz2BOAIpwHlS0Er-plxaSsvM0hq64
                    13 pro - https://www.magazineluiza.com.br/usado-iphone-13-pro-512gb-grafite-bom-trocafone-apple/p/gjha2ha6hf/te/i13p/?seller_id=trocafone
                    13 ProMax - https://www.trocafy.com.br/iphone-13-pro-max-512gb-grafite-sou-como-novo-2686/p?idsku=1339&srsltid=AfmBOoq9ImGKkfocSq0_Gy8l5oKczi61V4cpAoLoq6zagQ5aVpFAgoeESpE
                    
                     
                   
                                    ''')    
            elif (iphone == 4):
                gb = int(input('''
        Quantos GB você se interessa?
                    
                1 - 128gb
                2 - 256gb
                3 - 512gb
                              '''))  
                if(gb == 1):
                    iphone = input('''
                    IPhone 14 128 gb
                                       
                    14 - https://www.amazon.com.br/Apple-iPhone-14-128-GB/dp/B00CLP06OW/ref=asc_df_B00CLP06OW/?tag=googleshopp00-20&linkCode=df0&hvadid=647509453868&hvpos=&hvnetw=g&hvrand=6042798001831101856&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1001670&hvtargid=pla-2223470631834&psc=1
                    14 pro - https://www.carrefour.com.br/apple-iphone-14-pro-128-roxoprofundo-mp934498501/p
                    14 ProMax - https://www.casasbahia.com.br/apple-iphone-14-pro-max-128gb-dourado-55054417/p/55054417?utm_medium=Cpc&utm_source=GP_PLA&IdSku=55054417&idLojista=10037&tipoLojista=1P&&utm_campaign=gg_pmax_core_tele_apostas&gclid=CjwKCAjwyY6pBhA9EiwAMzmfwR6q5Wg38rHsZmRvO6zCSmGxv8N8iLf1Awt5HIjiYFBgsqzxj6igchoCETIQAvD_BwE&gclsrc=aw.ds
                    
                    
                        
                   
                                    ''')
                elif(gb == 2):
                    iphone = input('''
                    IPhone 14 256 gb
                    
                    14 - https://www.tradeinn.com/techinn/pt/apple-iphone-14-256gb-6.1/139331611/p?utm_source=google_products&utm_medium=merchant&id_producte=17677390&country=br&srsltid=AfmBOoomGjl7ktsxijmjoW20UIBXmxVqPHgKcGtYU8L90gB821GQ8t8miaA
                    14 pro - https://www.amazon.com.br/Apple-iPhone-14-256-Cinza-Escuro/dp/B0BZ66Z4GK?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&psc=1&smid=A1ZZFT5FULY4LN
                    14 ProMAX - https://www.horizonplay.com.br/apple/apple-iphone-14-pro-max-1256gb-novo-lacrado-tela-super-retina-xdr-oled-6-7?variant_id=21893&parceiro=8926&srsltid=AfmBOooHI-Z5rol9-qvPunLacJuZUTrOdnhFhit2M-fEkreb4mdtl4-z_jo
                   
                                       
                   
                                    ''')
                elif (gb == 3):
                    iphone = input('''
                    IPhone 14 512 gb
                    
                    14 - https://www.iplace.com.br/apple-iphone-14-512gb-estelar-mpx33be-a/222233?srsltid=AfmBOoq656DXuNgbgLl2KrCRQYLssBPwzB_Ijh4RsdcF7bIXCabFNv-mw-4
                    14 pro - https://www.iplace.com.br/apple-iphone-14-pro-512gb-dourado-mq233be-a/222264?srsltid=AfmBOooEYQpHwuC0poj0qN4TtTn6ew5Y_yFaGsHEhWWP4eWUcVNgX8XSzoo
                    14 ProMax - https://www.horizonplay.com.br/apple/apple-iphone-14-pro-max-512gb-5g-48mp-ios-tela-super-retina-xdr-oled-6-7?variant_id=22397&parceiro=8926&srsltid=AfmBOoof6-jfICORjrSpmg6LrEYoMkoFZYu_jBph1vQLhH2ZA2Jl_GfjcTM
                     
                   
                                    ''')
            elif (iphone == 5):
                gb = int(input('''
        Quantos GB você se interessa?
                    
                1 - 128gb
                2 - 256gb
                3 - 512gb
                              ''')) 
                if(gb == 1):
                    iphone = input('''
                    IPhone 15 128 gb
                    
                    15 - https://www.amazon.com.br/Apple-iPhone-15-128-GB/dp/B0CHXLC666?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&psc=1&smid=A1ZZFT5FULY4LN
                    15 pro - https://www.horizonplay.com.br/apple/apple-iphone-15-pro-128gb-5g-tela-super-retina-xdr-display-6-1?parceiro=8926&srsltid=AfmBOoqwXywWaAwDI_s4SmZOXuNF_revZ7pcEm-0A545hc7J3kY-t32rG2w
                    
                        
                   
                                    ''')
                elif (gb == 2):
                    iphone = input('''
                    IPhone 15 256 gb
                    
                    15 - https://www.apple.com/br/shop/buy-iphone/iphone-15/tela-de-6,1-polegadas-256gb-verde?cid=aos-br-seo-pla-iphone
                    15 pro - https://www.goimports.com.br/iPhone-15-Pro-256GB
                    15 Promax - https://www.fastshop.com.br/web/p/d/AEMU793BEAPTA_PRD/iphone-15-pro-max-apple-256gb-titanio-natural-tela-de-67-5g-e-camera-de-48mp-aemu793beaptaprd?utm_source=google&utm_medium=cpc&utm_term=pmax_1p&utm_campaign=20596588747&gclid=CjwKCAjwyY6pBhA9EiwAMzmfwVLh5OMP9qKS8IeibynuxPa7OgGW89vkUzYTYZ9P2XYHIFascpyxxxoCM3UQAvD_BwE
                                       
                     
                   
                                    ''')  
                elif (gb == 2):
                    iphone = input('''
                    IPhone 15 512 gb
                    
                    15 - https://fastshop.com.br/web/p/d/AEMTPC3BEAPTO_PRD/iphone-15-apple-512gb-preto-tela-de-61-5g-e-camera-de-48-mp-aemtpc3beaptoprd
                    15 pro - https://www.fastshop.com.br/web/p/d/AEMTV93BEAPTA_PRD/iphone-15-pro-apple-512gb-titanio-natural-tela-de-61-5g-e-camera-de-48mp-aemtv93beaptaprd?utm_source=google&utm_medium=cpc&utm_term=pmax_1p&utm_campaign=20596588747&gclid=CjwKCAjwyY6pBhA9EiwAMzmfwQpfkjqxrbvxc89RtjobOGQ1arYNbby4yeD1HI7J_I-3PcttFk4A7BoCjVsQAvD_BwE
                    15 ProMax - https://www.apple.com/br/shop/buy-iphone/iphone-15-pro/tela-de-6,7-polegadas-512gb-tit%C3%A2nio-azul?afid=p238%7Cs1gZ3ZqkV-dc_mtid_1870765e38482_pcrid_676127756048_pgrid_153615808505_pntwk_g_pchan_online_pexid__&cid=aos-br-kwgo-pla-iphone--slid---product-MU7F3BE%2FA-BR
                                       
                     
                   
                                    ''')    
        elif (aparelhos == 2):
             
            AirPods = int(input('''
     Qual modelo de Airpods você se interessa?
                
            1 - AirPods (2ª Gerção)
            2 - AirPods (3ª geração) com estojo de recarga Lightning
            3 - AirPods (3ª geração) com estojo de recarga MagSafe
            4 - AirPods Pro (2ª geração) com estojo de recarga MagSafe (USB‑C)
            5 - AirPods Max
                                                    '''))
            if (AirPods == 1):
                AirPods = input('''
            
                AirPods (2ª Gerção) - https://www.apple.com/br/shop/product/MV7N2BE/A/airpods-com-estojo-de-recarga?afid=p238%7CsN0MMXEF8-dc_mtid_1870765e38482_pcrid_493427106131_pgrid_34149634020_pntwk_g_pchan_online_pexid__&cid=aos-br-kwgo-pla-btb--slid---product-MV7N2BE/A-BR
             ''')
                
            elif (AirPods == 2):
                AirPods = input('''
                
                AirPods (3ª geração) com estojo de recarga Lightning - https://www.amazon.com.br/Apple-AirPods-3%C2%AA-gera%C3%A7%C3%A3o-estojo-recarga-Lightning/dp/B0BDJ6766D/ref=asc_df_B0BDJ6766D/?tag=googleshopp00-20&linkCode=df0&hvadid=379714766595&hvpos=&hvnetw=g&hvrand=17675003663329285362&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1001670&hvtargid=pla-1838048304188&psc=1
            ''')
                
            elif (AirPods == 3):
                 AirPods = input('''
                
                 AirPods (3ª geração) com estojo de recarga MagSafe - https://www.kabum.com.br/produto/375929/airpods-apple-3-geracao-bluetooth-com-estojo-de-recarga-magsafe-branco-mme73be-a?gclid=CjwKCAjwvrOpBhBdEiwAR58-3BVIUUY7SdcUI48CbJAn9fgMrPUdYWfAbyjMowxygmGymLZURxxqdBoCOrYQAvD_BwE
                                     
            ''')

            elif (AirPods == 4):
                 AirPods = input('''
                
                 AirPods Pro (2ª geração) com estojo de recarga MagSafe (USB‑C) - https://www.amazon.com.br/Apple-MQD83BE-A-AirPods-Pro-2%C2%AA-gera%C3%A7%C3%A3o/dp/B0BDJJLCT6/ref=asc_df_B0BDJJLCT6/?tag=googleshopp00-20&linkCode=df0&hvadid=379738801152&hvpos=&hvnetw=g&hvrand=4443301155079881888&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1001670&hvtargid=pla-1885484259513&psc=1
                                     
            ''')
            
            elif (AirPods == 5):
                AirPods = input('''
                
                AirPods Max - https://www.mercadolivre.com.br/apple-airpods-max-cinza-espacial/p/MLB17187387?from=gshop&matt_tool=11660798&matt_word=&matt_source=google&matt_campaign_id=14303413658&matt_ad_group_id=125984293877&matt_match_type=&matt_network=g&matt_device=c&matt_creative=539354956710&matt_keyword=&matt_ad_position=&matt_ad_type=pla&matt_merchant_id=735125422&matt_product_id=MLB17187387-product&matt_product_partition_id=1821855441092&matt_target_id=pla-1821855441092&gclid=CjwKCAjwvrOpBhBdEiwAR58-3JJzUJA0sj62Pxaq2aKC7lZmf9jhpVYBrmDBi6adFVbqfflhC9siexoC1F4QAvD_BwE
                                    

            ''')
        elif (aparelhos == 3):
            iPad = int(input('''
     Qual modelo atual de iPad você se interessa?
                
            1 - iPad Pro 
            2 - iPad Air
            3 - iPad
            4 - iPad mini
           
                                                    '''))
            if (iPad == 1):
                iPad = input('''
                
                iPad pro - https://www.amazon.com.br/Apple-iPad-Pro-Wi-Fi-polegadas-512-GB/dp/B09KMHYYJ2/ref=asc_df_B09KMHYYJ2/?tag=googleshopp00-20&linkCode=df0&hvadid=379728517897&hvpos=&hvnetw=g&hvrand=8011561765449961299&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1001670&hvtargid=pla-1558563170570&psc=1
                                 

            ''')
            elif (iPad == 2):
                iPad = input('''
                
                iPad air - https://www.amazon.com.br/Apple-iPad-Air-gera%C3%A7%C3%A3o-Wi-Fi-64-GB/dp/B09V4D6V9H/ref=asc_df_B09V4D6V9H/?tag=googleshopp00-20&linkCode=df0&hvadid=379728517897&hvpos=&hvnetw=g&hvrand=7601439720875414831&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1001670&hvtargid=pla-1654399523939&psc=1
                                 

            ''')
            elif (iPad == 3):
                iPad = input('''
                
                iPad  - https://www.carrefour.com.br/apple-ipad-9-geracao-wifi-64gb-102-silver-mp929807090/p

            ''')
            elif (iPad == 5):
                 iPad = input('''
                
                iPad mini  - https://www.amazon.com.br/Apple-iPad-mini-Wi-Fi-64-GB/dp/B09L5CNNNM/ref=asc_df_B09L5CNNNM/?tag=googleshopp00-20&linkCode=df0&hvadid=379787220407&hvpos=&hvnetw=g&hvrand=14696299824686144504&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1001670&hvtargid=pla-1648236895634&psc=1
                                  

            ''')
        elif (aparelhos == 4):
             
            AppleWatch = int(input('''
     Qual modelo de Apple Watch você se interessa?
                
            1 - Apple Watch Series 9
            2 - Aplle Watch Series 8
            3 - Apple Watch SE
            4 - Apple Watch Ultra
            5 - Apple Watch Ultra 2
                                                    '''))
            if(AppleWatch == 1):
                AppleWatch = input('''
                
                Apple Watch Series 9 - https://www.apple.com/br/shop/buy-watch/apple-watch/41mm-redecelular-silver-a%C3%A7o-inoxid%C3%A1vel-azul-tempestade-pulseira-esportiva-m-l?afid=p238%7Csk2XwKFIu-dc_mtid_1870765e38482_pcrid_676127756045_pgrid_155057957740_pntwk_g_pchan_online_pexid__&cid=aos-br-kwgo-pla-watch--slid---product-MRJ33BZ%2FA-BR
                                   
                                  

            ''')
            elif (AppleWatch == 2):
                 AppleWatch = input('''
                
                Aplle Watch Series 8 - https://www.amazon.com.br/Apple-Watch-Smartwatch-prateada-alum%C3%ADnio-esportiva/dp/B0BDJ2792P/ref=asc_df_B0BDJ2792P/?tag=googleshopp00-20&linkCode=df0&hvadid=379787833841&hvpos=&hvnetw=g&hvrand=9668645375611258894&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9102423&hvtargid=pla-1911804685863&psc=1
                                    

            ''')
            elif (AppleWatch == 3):
                 AppleWatch = input('''
                
                Apple Watch SE - https://www.amazon.com.br/Apple-Watch-SE-Smartwatch-meia-noite-alum%C3%ADnio-esportiva/dp/B0BDJFXMLV/ref=asc_df_B0BDJFXMLV/?tag=googleshopp00-20&linkCode=df0&hvadid=630348228695&hvpos=&hvnetw=g&hvrand=12610556227601475080&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9102423&hvtargid=pla-1902282644536&psc=1
                                    
                                    

            ''')
            elif (AppleWatch == 4):
                 AppleWatch = input('''
                
                Apple Watch Ultra - https://www.amazon.com.br/Apple-Watch-Ultra-Cellular-tit%C3%A2nio-pulseira-meia-noite/dp/B0BDHQD29D/ref=asc_df_B0BDHQD29D/?tag=googleshopp00-20&linkCode=df0&hvadid=379725922278&hvpos=&hvnetw=g&hvrand=15300746326729753571&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9102423&hvtargid=pla-1884222232707&psc=1
                                    
                                    
                                    

            ''')
            elif (AppleWatch == 5):
                 AppleWatch = input('''
                
                Apple Watch Ultra 2 - https://www.iplace.com.br/apple-watch-ultra-2-gps-cellular-azul-preta-p-m-caixa-titanio-pulseira-loop-trail/226718?gclid=CjwKCAjws9ipBhB1EiwAccEi1Che6FdKGjwAo76wpljpsf1bDUnrcn6Xy11vr1Ci9DNxjSkDJ9BH6RoC8N0QAvD_BwE
                                    
            
                                    
                                    
                                    

            ''')
            
            

                

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

        while True:
            buscarLink()
            x = int(input('''
            1 - Pesquisar outro produto
            2 - Sair                  
            '''))
            if(x==2):
                break   


    elif (n == 3): 
        print('volte sempre!')
    

