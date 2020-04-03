import random
##variaveis iniciais##
dinheiro= 5
a = random.randint(1,6)
b = random.randint(1,6)
s = a + b
apostas = []
quantias_apostadas = []
ap2 = int(input("digite a quantia apostada")
vence_field= [3,4,9,10,11]
vence_craps=[2,3,12]
entra_em_point=[4,5,6,8,9,10]
point = s
##começando o jogo##
while dinheiro != 0:
    ap1 = input("faça uma aposta(twelve, plb, field, craps)")
    ap2 = int(input("digite a quantia apostada")
    apostas.append(ap1)
    quantias_apostadas.append(ap2)
    credito = dinheiro -quantias_apostadas[i]
    apdenovo = input("quer fazer amis uma aposta? (s/n)")
    if apdenovo=="s":
        ap3=input("escolha o tipo de aposta(twelve, plb, field, craps)")
        ap4=int(input("digite a quantia apostada"))
        apostas.append(ap3)
        quantias_apostadas.append(ap4)
    if twelve in apostas:
        if s==12:
            dinheiro = credito + (ap2*30)
        else:    
            dinheiro = credito
            print ("você perdeu")
        apostas.remove(twelve)
    if field in apostas:
        if s==12:
            dinheiro = credit        
        if s== 2:
            dinheiro = credito + (ap2*2)
        if s in vence_field:
            dinheiro = credito + ap2
        else:
            dinheiro = credito
            print ("você perdeu")
        apostas.remove(field)
    if craps in apostas:
        if s in vence_craps:
            dinheiro = credito + (ap2*7)
        else:
            dinheiro= credito
            print (" você perdeu")
        apostas.remove(craps)
    if plb in apostas:
        if s==7 or s==11:
            dinheiro = credito+ap2
        if s==2 or s==3 or s==12:
            dinheiro = credito
            print ("você perdeu")
        if s in entra_em_point:
            while 
                ap4=input("Quer fazer mais uma aposta? (twelve, field, craps)")
                ap5=int(input("digite a quantia apostada"))
                apostas.append(ap4)
                quantias_apostadas.append(ap5)
                c=random.randint(1,6)
                d= random.randint(1,6)
                s2= c + d
                if s2==point:
                    dinheiro= credito + ap2
                    break
                apostas.remove(plb)
                if s2==7:
                    dinheiro=credito
                    print ("você perdeu")
                    break
                apostas.remove(plb)
                if twelve in apostas:
                    if s==12:
                        dinheiro = credito + (ap2*30)
                    else:
                        dinheiro = credito
                        print ("você perdeu")
                    apostas.remove(twelve)
                if field in apostas:
                    if s==12:
                        dinheiro = credit        
                    if s== 2:
                        dinheiro = credito + (ap2*2)
                    if s in vence_field:
                        dinheiro = credito + ap2
                     else:
                        dinheiro = credito
                        print ("você perdeu")
                    apostas.remove(field)
            if craps in apostas:
                if s in vence_craps:
                    dinheiro = credito + (ap2*7)
                else:
                    dinheiro= credito
                    print (" você perdeu")
                apostas.remove(craps)
    keep_going=input("quer continuar?(s/n)")
    if keep_going=="n"
       breakpoint