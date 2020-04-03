import random
##variaveis iniciais##
comeco= 5
a = random.randint(1,6)
b = random.randint(1,6)
s = a + b
apostas = []
quantias_apostadas = []*4
vence_field= [3,4,9,10,11]
vence_craps=[2,3,12]
entra_em_point=[4,5,6,8,9,10]
point = s
dinheiro= 5
##começando o jogo##
while dinheiro!= 0:
    print(" voce está na fase Come out")
    print("voce começa com 5 fichas")
    ap = input("faça uma aposta(twelve, plb, field, craps)")
    ap1 = int(input("digite a quantia apostada"))
    apostas.append(ap)
    quantias_apostadas.append(ap1)
    apdenovo = input("quer fazer mais uma aposta? (s/n)")
    ap2=quantias_apostadas[0]
    ap4=0
    if apdenovo=="s":
        ap3=input("escolha o tipo de aposta(twelve, plb, field, craps)")
        ap4=int(input("digite a quantia apostada"))
        apostas.append(ap3)
        quantias_apostadas.append(ap4)
    credito = dinheiro-ap1-ap4
    if "twelve" in apostas:
        if s==12:
            dinheiro = credito + (ap2*30)
        else:    
            dinheiro = credito
            print ("você perdeu")
        apostas.remove("twelve")
        del quantias_apostadas[0]
    if "field" in apostas:
        if s==12:
            dinheiro = credito        
        if s== 2:
            dinheiro = credito + (ap2*2)
        if s in vence_field:
            dinheiro = credito + ap2
        else:
            dinheiro = credito
            print ("você perdeu")
        apostas.remove("field")
        del quantias_apostadas[0]
    if "craps" in apostas:
        if s in vence_craps:
            dinheiro = credito + (ap2*7)
        else:
            dinheiro= credito
            print (" você perdeu")
        apostas.remove("craps")
        del quantias_apostadas[0]
    if "plb" in apostas:
        if s==7 or s==11:
            dinheiro = credito+ap2
            apostas.remove("plb")
            del quantias_apostadas[0]
        if s==2 or s==3 or s==12:
            dinheiro = credito
            print ("você perdeu")
            apostas.remove("plb")
            del quantias_apostadas[0]
        if s in entra_em_point:
            fase_point: True
            while True :
                apdenovo = input("quer fazer mais uma aposta? (s/n)")
                if apdenovo=="s":
                    ap3=input("escolha o tipo de aposta(twelve, plb, field, craps)")
                    ap4=int(input("digite a quantia apostada"))
                    apostas.append(ap3)
                    quantias_apostadas.append(ap4)
                    credito = dinheiro-ap1-ap4
                c=random.randint(1,6)
                d= random.randint(1,6)
                s2= c + d
                if s2==point:
                    dinheiro= credito + ap2
                    fase_point: False
                apostas.remove("plb")
                del quantias_apostadas[0]
                if s2==7:
                    dinheiro=credito
                    print ("você perdeu")
                    fase_point: False
                    del quantias_apostadas[0]
                apostas.remove("plb")
                if "twelve" in apostas:
                    if s==12:
                        dinheiro = credito + (ap2*30)
                    else:
                        dinheiro = credito
                        print ("você perdeu")
                    apostas.remove("twelve")
                    del quantias_apostadas[0]
                if "field" in apostas:
                    if s==12:
                        dinheiro = credito        
                    if s== 2:
                        dinheiro = credito + (ap2*2)
                    if s in vence_field:
                        dinheiro = credito + ap2
                    else:
                        dinheiro = credito
                        print ("você perdeu")
                    apostas.remove("field")
                    del quantias_apostadas[0]
            if "craps" in apostas:
                if s in vence_craps:
                    dinheiro = credito + (ap2*7)
                else:
                    dinheiro= credito
                    print (" você perdeu")
                apostas.remove("craps")
                del quantias_apostadas[0]
    print (dinheiro)
    keep_going=input("quer continuar?(s/n)")
    if keep_going=="n":
       breakpoint