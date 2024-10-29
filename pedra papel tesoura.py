import random 

while True:
    cont =+ 1
    print('vamos jogar pedra, papel e tesoura')
    print('1 pedra')
    print('2 papel')
    print('3 tesoura')
    com = random.randint(1, 3)
    vc = int(input('escolha um numero de 1 a 3 :'))
    print('computador',com)
    print('Você',vc)
    if vc == com:
        print('Empate')
    elif vc == 1 and com == 2:
        print('voce perdeu')
    elif vc == 3 and com == 1:
        print('Você perdeu')
    elif vc == 2 and com == 3:
        print('Você perdeu')
    else:
        print('Você ganhou')
        print(cont)
    dec = str(input('Quer continua S/N')).upper.[0]
    if dec == 'N':
        break
nome=input('Qual o seu nome?') 
print('paser em conheçe-lo',nome)