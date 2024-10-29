from random import randint
nv = 1

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
      'atak pesado:+2 \n')

classe = int(input('Escolha uma classe: '))
if classe == 1:
    atak += 3
    vcatakpasado += 4
    cura += 2
if classe == 2:
    atak += 2
    vcatakpasado += 5
    cura += 3
if classe == 3:
    atak += 4
    vcatakpasado += 2
    cura += 2
if classe == 4:
    atak += 2
    vcatakpasado += 2
    cura += 5

print('RAÇA')
print('1)Humano\n'
      '+2 em todos os atribultos')
print('2)Elfo\n'
      '+2 em classe Arqueira, '
      '-2 em classe Mago, '
      '-1 em classe Gerreiro')
print('3)Ogro\n'
      '-4 em todas as classe, '
      '+6 em classe Gerreiro, ') 
raça = int(input('Escolha uma Raça: '))
if raça == 1:
    atak += 2
    cura += 2
    vcatakpasado += 2
if raça == 2:
    if classe == 2 or classe == 4:
        atak += 2
        cura += 2
        vcatakpasado += 2
    elif classe == 1:
        atak += -1
        cura += -1
        vcatakpasado += -1
    elif classe == 3:
        atak += -2
        cura += -2
        vcatakpasado += -2
if raça == 3:
    if classe == 2 or classe == 3 or classe == 4:
        atak += -4
        cura += -4
        vcatakpasado += -4
    elif classe == 1:
        atak += 6
        vcatakpasado += 6


while True:
    vcaleatorio = randint(0, 10)
    print('Nivel',playerlv)
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
            banco = banco + moeda
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
                atak = atak + 5
            elif up == 2:
                cura = cura + 5
            elif up == 3:
                vcatakpasado = vcatakpasado + 10
        loja = ' '
        while loja not in 'SN':
            loja=str(input('\033[1;35mDESEJA IR PARA A LOJA S/N: '))
            if loja != 'SN' or loja == '':
                print('INVALIDO')
                loja=str(input('\033[1;35mDESEJA IR PARA A LOJA S/N: '))
        if loja == 'S':
            print('=='*15)
            print(f'{'LOJA':>15}')
            print('=='*15)
            print(moeda)
            print('1)Porção de Cura +5 ')
            print('2)Espada afiada +7 ')
            print('3)Porrete +5 ')
            print('4)Barril de vida +10')
            print('5)Katana +10')
            print('6)Arco melhorado +10')
            print('7)cajado Demoniaco ')
            print('8)sair')
            
            compra = int(input('Digite para comprar'))
            if compra == 1:
                cura += 5
                if classe == 4 :
                    cura += 5
            if compra == 2:
                atak += 7
                vcatakpasado += 7
                if classe == 1:
                    atak += 3
                    vcatakpasado += 3
            if compra == 3:
                atak += 5
                vcatakpasado += 5
                if raça == 3:
                    atak += 2
                    vcatakpasado += 2
            if compra == 4:
                cura += 10
                if classe == 4 :
                    cura += 15
            if compra == 5:
                atak += 10
                vcatakpasado += 12
                if classe == 1:
                    atak += 12
                    vcatakpasado += 15
            if compra == 6:
                if classe == 2:
                    if raça == 2:
                        atak += 15
                        vcatakpasado += 17
            if compra == 7:
                if classe == 3:
                    atak += 15
                    vcatakpasado += 17
            if compra == 8:
                break

        elif loja == 'n':
            break
        sn = ' '
        while sn not in 'SN':
            sn= str(input(f'continuar para nv{nv} S/N: ')).upper()
            if sn != 'SN' or sn == ' ':
                print('INVALIDO')
                sn= str(input(f'continuar para nv{nv} S/N: ')).upper()
        if sn == 'S':
            ia = 200
            vc = 100
            if nv == 10:
                print('\033[1;31mBOSS FINAL\033[m')
                vc = 500
                ia = 1000
                iaatak = 44
                iaatakpesado = 55
                iacura = 47
            if nv == 9:
                vc = 450
                ia = 900
                iaatak = 40
                iaatakpesado = 50
                iacura = 45
            if nv == 8:
                vc = 400
                ia = 800
                iaatak = 30
                iaatakpesado = 45
                iacura = 42
            if nv == 7:
                vc = 350
                ia = 700
                iaatak = 26
                iaatakpesado = 39
                iacura = 35
            if nv == 6:
                vc = 300
                ia = 600
                iaatak = 21
                iaatakpesado = 33
                iacura = 30
            if nv == 5:
                vc = 250
                ia = 500
                iaatak = 18
                iaatakpesado = 28
                iacura = 20
            if nv == 4:
                vc = 200
                ia = 400
                iaatak = 14
                iaatakpesado = 23
                iacura = 15
            if nv == 3:
                vc = 150
                ia = 300
            if nv == 2:
                vc = 100
                ia = 200

        else:
            break
    elif vc <= 0:
        print('\033[1;31mGAMER OVER\033[m')
        break
    print('IA',ia)
    print('Você',vc,'\n')
