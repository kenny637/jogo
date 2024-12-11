from random import randint
nv = 1

cont = 0
moeda = 0

banco = 0
experiencia = 0

playerlv = 1

atak = 5
vcatakpasado = 6
cura = 3
fugio = 0

iaatak = 10
iaatakpesado = 20
iacura = 5


vc = 100
ia = 100


print('CLASSE')
print('1)Guerreiro \n'
      'atak:+3 '
      'cura:+2 '
      'atak pesado:+4 ')
print('2)Arqueiro \n'
      'atak:+2 '
      'cura:+3 '
      'atak pesado:+5 ')
print('3)Mago \n'
      'atak:+4 '
      'cura:+2 '
      'atak pesado:+2 ')
print('4)Sacerdote \n'
      'atak:+2 '
      'cura:+5 '
      'atak pesado:+2 ')
print('5)Assasino \n'
      'atak:+7 '
      'cura:+1 '
      'atak pesado:+5 \n')

while True:
    classe = int(input('Escolha uma classe: '))
    if classe == 1:
        atak += 3
        vcatakpasado += 4
        cura += 2
        break
    if classe == 2:
        atak += 2
        vcatakpasado += 5
        cura += 3
        break
    if classe == 3:
        atak += 4
        vcatakpasado += 2
        cura += 2
        break
    if classe == 4:
        atak += 2
        vcatakpasado += 2
        cura += 5
        break
    if classe == 5:
        atak += 7
        vcatakpasado += 5
        cura += 1
        break

print('RAÇA')
print('1)Humano\n'
      '+2 em todas as classes'
      '+1 em classe Assasino')
print('2)Demi-Humano\n'
      '+1 em classe Arqueira, '
      '+1 em classe sacerdote, '
      '-1 em classe Mago, '
      '+3 em classe Gerreiro, '
      '+3 em classe Assasino')
print('3)Elfo\n'
      '+2 em classe Arqueira, '
      '+5 em classe sacerdote, '
      '+1 em classe Mago, '
      '-1 em classe Gerreiro, '
      '-1 em classe Assasino')
print('4)Ogro\n'
      '-4 em todas as classe, '
      '+4 em classe Gerreiro, ') 
while True:
    raça = int(input('Escolha uma Raça:'))
    if raça == 1:
        atak += 2
        cura += 2
        vcatakpasado += 2
        if classe == 5:
            atak += 1
            break
    if raça == 2:
        if classe == 1:
            atak += 3
            cura += 3
            vcatakpasado -= 4
            break
        elif classe == 2:
            atak += 1
            cura += 1
            vcatakpasado += 1
            break
        elif classe == 3:
            atak -= 1
            cura -= 1
            vcatakpasado -= 1
            break
        elif classe == 4:
            atak += 1
            cura += 2
            vcatakpasado += 1
            break
        elif classe == 5:
            atak += 3
            cura += 1
            vcatakpasado += 5
            break
        
    if raça == 3:
        if classe == 1:
            atak -= 1
            cura -= 1
            vcatakpasado -= 1
            break
        elif classe == 2 :
            atak += 3
            cura += 3
            vcatakpasado += 2
            break
        elif classe == 3:
            atak -= 2
            cura -= 2
            vcatakpasado -= 2
            break
        elif classe == 4:
            atak += 3
            cura += 5
            vcatakpasado += 2
            break
        elif classe == 5:
            atak -= 1
            cura -= 2
            vcatakpasado -= 1
            break
    if raça == 4:
        if classe == 2 or classe == 3 or classe == 4 or classe == 5:
            atak -= 4
            cura -= 4
            vcatakpasado -= 4
            break
        elif classe == 1:
            atak += 4
            vcatakpasado += 6
            break

 
while True:
    vcaleatorio = randint(0, 10)
    print('\nNivel',playerlv)
    print(f'1)Ataque: {atak:<10} 2)Cura: {cura}\n3)atak pesado: {vcatakpasado:<5} 4)fugir: 0')
    dec = int(input('Digite o numero da a ação: '))
    if dec == 1:
        a = ia - atak
        ia = a
        print('\033[1;36mVocê atak:\033[m',atak)
    elif dec == 2:
        s = vc + cura 
        vc = s
        print('\033[1;36mvocê cura:\033[m',cura)
    elif dec == 999:
        q = ia - 1000
        ia = q
        print('\033[1;31mchet ativado\033[m')
    elif dec == 3:
        if dec == 3 and vcaleatorio == 3 or vcaleatorio == 6  or vcaleatorio == 9:
            print('\033[1;36mVocê\033[m \033[1;31mERROU\033[m \033[1;36mo golpe\033[m')   
        else:
            a = ia - vcatakpasado
            ia = a
            print('\033[1;36mVocê atak pesado:\033[m',vcatakpasado)
    elif dec == 4:
        if vcaleatorio == 5 or vcaleatorio == 8:
            print('\033[1;36mVocê Fugiu\033[m')
            ia += - 1000
            fugio += 1
        else:
            print('\033[1;36mIA pesegui-o você\033[m')
    com2 = randint(0, 10)      
    com = randint(1, 5)
    if com == 1 or com == 2 or com == 3:
        a = vc - iaatak
        vc = a
        print('\033[1;32mIA atak: \033[m',iaatak )
    elif com == 4:
        s = ia + iacura
        ia = s
        print('\033[1;32mIA cura:\033[m',ia)
    if nv == 3 or nv == 4:
        if com == 5 and com2 == 3 or com2 == 9:
            print('\033[1;32mIA\033[m \033[1;31mERROU\033[m \033[1;32mo golpe\033[m')   
            dec = int(input('Contra ataque: 1 Cura: 2:  '))
            if dec == 1:
                a = ia - atak
                ia = a
                print('\033[1;36mVocê contra atak:\033[m',atak)
            elif dec == 2:
                s = vc + cura 
                vc = s
                print('\033[1;36mvocê cura:\033[m',cura)
        elif com == 5:
            d = vc - iaatakpesado
            vc = d
            print('\033[1;32mIA atak pesado: \033[m',iaatakpesado)
    if vc <= 0 and ia <= 0:
        print('\033[1;36m Empate\033[m')
        break
    elif ia <= 0:
        nv += 1
        if nv == 11 and dec == 4:
            print(f'\033[1;31mFUGI-O {fugio} vezes, e não venceu o BOSS\033[m')
            break
        elif nv == 11:
            print('\033[1;33mVOCÊ VENCEU O JOGO, PARABENS\033[m')
            break
        if dec == 4 and vcaleatorio == 5 or dec == 4 and vcaleatorio == 8:
            print('Você não Venceu')              
        else:
            print('\033[1;33mVOCÊ VENCEU\033[m')
            moeda = randint(10, 50)
            xp = randint(10, 50)
            banco += moeda
            experiencia = experiencia + xp
            print(f'Moedas: {banco}')
            print(f'XP: {experiencia}')
            if experiencia >= 200 and playerlv == 4:
                print('MAX')
                playerlv = 5
                experiencia = 0
                atak += 3
                cura += 3
                vcatakpasado += 3
            elif experiencia >= 150 and playerlv == 3:
                print('Você pasou de nivel')
                playerlv = 4
                experiencia = 0
                atak += 3
                cura += 3
                vcatakpasado += 3
            elif experiencia >= 100 and playerlv == 2:
                print('Você pasou de nivel')
                playerlv = 3
                experiencia = 0
                atak += 3
                cura += 3
                vcatakpasado += 3
            elif experiencia >= 50 and playerlv == 1:
                print('Você pasou de nivel')
                playerlv = 2
                experiencia = 0
                atak += 3
                cura += 3
                vcatakpasado += 3

            print('UPGRADE')
            up = int(input('Aumento de ataque: 1, Aumento de Cura: 2, Aumento de taque pesado: 3: '))
            if up == 1:
                atak += 5
                if classe == 1:
                    atak += 2
            elif up == 2:

                cura += 5
            elif up == 3:
                vcatakpasado += 10
        
        while True:
            loja = str(input('\033[1;35mDESEJA IR PARA A LOJA S/N: \033[m')).upper().strip()
            if loja == 'N':
                break
            elif loja != 'S':
                print('INVALIDO')
            elif loja == 'S':
                print('=='*15)
                print(f'{"LOJA":>15}')
                print('=='*15)
                print(f'Moedas disponíveis: {banco}')
                print('1) Porção de aumento Cura +5  R$ 50')
                print('2) Espada afiada +7 R$ 80')
                print('3) Porrete +5 R$ 90')
                print('4) Barril de vida +10 R$ 150')
                print('5) Katana +10 R$ 170')
                print('6) Arco melhorado +10 R$ 160')
                print('7) Cajado Demoniaco +8 R$ 150')
                print('8) Sair')

                compra = int(input('Digite o número para comprar: '))
                
                if compra == 1 and banco >= 50:
                    cura += 5
                    banco -= 50
                    if classe == 4:
                        cura += 5
                    print('Você comprou Porção de aumento Cura +5')
                elif compra == 2 and banco >= 80:
                    atak += 7
                    vcatakpasado += 7
                    banco -= 80
                    if classe == 1:
                        atak += 3
                        vcatakpasado += 3
                    print('Você comprou Espada afiada +7')
                elif compra == 3 and banco >= 90:
                    atak += 5
                    vcatakpasado += 5
                    banco -= 90
                    if raça == 3:
                        atak += 2
                        vcatakpasado += 2
                    print('Você comprou Porrete +5')
                elif compra == 4 and banco >= 150:
                    cura += 10
                    banco -= 150
                    if classe == 4:
                        cura += 15
                    print('Você comprou Barril de vida +10')
                elif compra == 5 and banco >= 170:
                    atak += 10
                    vcatakpasado += 12
                    banco -= 170
                    if classe == 1:
                        atak += 12
                        vcatakpasado += 15
                    print('Você comprou Katana +10')
                elif compra == 6 and banco >= 160:
                    banco -= 160
                    if classe == 2:
                        if raça == 2:
                            atak += 15
                            vcatakpasado += 17
                    print('Você comprou Arco melhorado +10')
                elif compra == 7 and banco >= 150:
                    banco -= 150
                    if classe == 3:
                        atak += 15
                        vcatakpasado += 17
                    print('Você comprou Cajado Demoníaco +8')
                elif compra == 8:
                    break
                else:
                    print("Você não tem moedas suficientes ou opção inválida.")
        while True:
            sn= str(input(f'continuar para nv{nv} S/N: ')).upper().strip()
            if sn == 'N':
                break
            elif sn != 'S':
                print('INVALIDO')
            elif sn == 'S':
                cont += 1
                ia = 200
                vc = 100
                if nv == 10:
                    print('\033[1;31mBOSS FINAL\033[m')
                if nv > 1:
                    iaatak += 7
                    iaatakpesado += 7
                    iacura += 7
    elif vc <= 0:
        print('\033[1;31mGAMER OVER\033[m')
        break
    print('IA',ia)
    print('Você',vc,'\n')
