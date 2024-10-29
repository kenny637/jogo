import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

#musica
musica_de_fundo = pygame.mixer.music.load('Super Mario Bros. Theme Song.mp3')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('Efeito sonoro da moeda do Mario..mp3')
barulho_colisao.set_volume(0.9)

#tela
largura = 1920
altura = 1020

meio= altura/2.6
meio2 = largura/2.3
#POSISOES E TAMANHOS
posicao_jogador1 = [1800, 50]
posicao_jogador2 = [100, 800]
posicao_jogador3 = [1800, 900]
posicao_jogador4 = [60, 100]
tamanho_jogador1 = 50
tamanho_jogador2 = 50
tamanho_jogador3 = 50
tamanho_jogador4 = 50

#cores
branco = (255, 255, 255)
vermelho = (255, 0, 0)
azul = (0, 0, 255)
rosa = (255, 192, 203)
verde = (0, 255, 0)
preto = (0, 0, 0)
ciano = (0, 255, 255)

#postos aleatorio
x_amarelo = randint(40, 500)
y_amarelo = randint(50, 500)
x_amarelo2 = randint(400, 500)
y_amarelo2 = randint(500, 500)
x_laranja = randint(100, 500)
y_laranja = randint(100, 500)
x_ciano = randint(100, 500)
y_ciano = randint(300, 600)

pontos = 0
pontos2 = 0
pontos3 = 0
pontos4 = 0
#texto tela
fonte = pygame.font.SysFont('Arial', 40, True, False)
fonte2 = pygame.font.SysFont('Arial', 40, True, False)
fonte3 = pygame.font.SysFont('Arial', 40, True, False)
fonte4 = pygame.font.SysFont('Arial', 40, True, False)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('RPG')
relogio = pygame.time.Clock()

cont1 = cont2 = cont3 = cont4 = cont5 = cont6 = cont7 = cont = 0


BACKGROUND_COLOR = (0, 150, 0)
while True:
    relogio.tick(120)
    tela.fill(BACKGROUND_COLOR)
    mesagem = f'Vermelho: {pontos}'
    mesagem2 = f'Azul: {pontos2}'
    mesagem3 = f'Verde: {pontos3}'
    mesagem4 = f'Rosa: {pontos4}'

    texto_formatado = fonte.render(mesagem, False, (255,0, 0))
    texto_formatado2 = fonte.render(mesagem2, False, (0, 0, 255))
    texto_formatado3 = fonte.render(mesagem3, False, (0, 255,0))
    texto_formatado4 = fonte.render(mesagem4, False, (255, 192, 203))

    for event in pygame.event.get():
        if event.type == quit:
            pygame.quit()
            exit()
    '''if pygame.key.get_pressed()[K_a]:
        x = x - 15
    if pygame.key.get_pressed()[K_d]:
        x = x + 15
    if pygame.key.get_pressed()[K_w]:
        y = y - 15
    if pygame.key.get_pressed()[K_s]:
        y = y + 15'''
    # Movimentação do Jogador 1 (teclas W, A, S, D)
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w]:  # Cima
        posicao_jogador1[1] -= 10
    if teclas[pygame.K_s]:  # Baixo
        posicao_jogador1[1] += 10
    if teclas[pygame.K_a]:  # Esquerda
        posicao_jogador1[0] -= 10
    if teclas[pygame.K_d]:  # Direita
        posicao_jogador1[0] += 10

    # Movimentação do Jogador 2 (setas do teclado)
    if teclas[pygame.K_UP]:  # Cima
        posicao_jogador2[1] -= 10
    if teclas[pygame.K_DOWN]:  # Baixo
        posicao_jogador2[1] += 10
    if teclas[pygame.K_LEFT]:  # Esquerda
        posicao_jogador2[0] -= 10
    if teclas[pygame.K_RIGHT]:  # Direita
        posicao_jogador2[0] += 10
    
    # Movimentação do Jogador 3 (I, K, J, L)
    if teclas[pygame.K_i]:  # Cima
        posicao_jogador3[1] -= 10
    if teclas[pygame.K_k]:  # Baixo
        posicao_jogador3[1] += 10
    if teclas[pygame.K_j]:  # Esquerda
        posicao_jogador3[0] -= 10
    if teclas[pygame.K_l]:  # Direita
        posicao_jogador3[0] += 10

    # Movimentação do Jogador 4 (T, G, F, h)
    if teclas[pygame.K_t]:  # Cima
        posicao_jogador4[1] -= 10
    if teclas[pygame.K_g]:  # Baixo
        posicao_jogador4[1] += 10
    if teclas[pygame.K_f]:  # Esquerda
        posicao_jogador4[0] -= 10
    if teclas[pygame.K_h]:  # Direita
        posicao_jogador4[0] += 10

    #players
    ret_vermelho = pygame.draw.rect(tela, vermelho, (posicao_jogador1[0], posicao_jogador1[1], tamanho_jogador1, tamanho_jogador1))
    ret_azul = pygame.draw.rect(tela, azul, (posicao_jogador2[0], posicao_jogador2[1], tamanho_jogador2, tamanho_jogador2))
    ret_verde = pygame.draw.rect(tela,verde, (posicao_jogador3[0], posicao_jogador3[1], tamanho_jogador3, tamanho_jogador3))
    ret_rosa = pygame.draw.rect(tela,rosa, (posicao_jogador4[0], posicao_jogador4[1], tamanho_jogador4, tamanho_jogador4))

    # ponto e poder
    ret_amarelo = pygame.draw.circle(tela, (255,255,0), (x_amarelo,y_amarelo),20 )
    ret_amarelo2 = pygame.draw.circle(tela, (128,0,128), (x_amarelo2,y_amarelo2),20 )
    ret_laranja = pygame.draw.circle(tela, (255,165,0), (x_laranja ,y_laranja ),50 )
    ret_ciano = pygame.draw.circle(tela, (0,255,255), (x_ciano ,y_ciano ),120 )


    #paredes
    ret_parede = pygame.draw.line(tela, (0, 100, 0),(1920,0),(10,0),40)
    ret_parede2 = pygame.draw.line(tela, (0, 100, 0),(0,1020),(0,0),40)
    ret_parede3 = pygame.draw.line(tela, (0, 100, 0),(1920, 0),(1920, 1020),40)
    ret_parede4 = pygame.draw.line(tela, (0, 100, 0),(0,1000),(1920, 1000),20)

    #obistacolos
    #ret_objeto = pygame.draw.rect(tela, preto, (meio2, meio,200,200 ))

    # pontos
    if ret_vermelho.colliderect(ret_amarelo) or ret_azul.colliderect(ret_amarelo) or ret_verde.colliderect(ret_amarelo) or ret_rosa.colliderect(ret_amarelo):
        x_amarelo = randint(40, 1900)
        y_amarelo = randint(40, 980)
        if ret_vermelho.colliderect(ret_amarelo):
            pontos += 1
        if ret_azul.colliderect(ret_amarelo):
            pontos2 += 1
        if ret_verde.colliderect(ret_amarelo):
            pontos3 += 1
        if ret_rosa.colliderect(ret_amarelo):
            pontos4 += 1
        barulho_colisao.play()

    if ret_vermelho.colliderect(ret_amarelo2) or ret_azul.colliderect(ret_amarelo2) or ret_verde.colliderect(ret_amarelo2) or ret_rosa.colliderect(ret_amarelo2):
        x_amarelo2 = randint(40, 1900)
        y_amarelo2 = randint(40, 980)
        if ret_vermelho.colliderect(ret_amarelo2):
            pontos += 2
        if ret_azul.colliderect(ret_amarelo2):
            pontos2 += 2
        if ret_verde.colliderect(ret_amarelo2):
            pontos3 += 2
        if ret_rosa.colliderect(ret_amarelo2):
            pontos4 += 2
        barulho_colisao.play()

    # Poder
    if ret_vermelho.colliderect(ret_laranja) or ret_azul.colliderect(ret_laranja) or ret_verde.colliderect(ret_laranja) or ret_rosa.colliderect(ret_laranja):
        x_laranja = randint(40, 1900)
        y_laranja = randint(40, 980)
        if ret_vermelho.colliderect(ret_laranja):
            cont1 += 1
            tamanho_jogador1 = 100
            if cont1 == 2:
                tamanho_jogador1 = 50
                cont1 = 0
        if ret_azul.colliderect(ret_laranja):
            cont2 += 1
            tamanho_jogador2 = 100
            if cont2 == 2:
                tamanho_jogador2 = 50
                cont2 = 0
        if ret_verde.colliderect(ret_laranja):
            cont3 += 1
            tamanho_jogador3 = 100
            if cont3 == 2:
                tamanho_jogador3 = 50
                cont3 = 0
        if ret_rosa.colliderect(ret_laranja):
            cont4 += 1
            tamanho_jogador4 = 100
            if cont4 == 2:
                tamanho_jogador4 = 50
                cont4 = 0
        barulho_colisao.play()

    if ret_vermelho.colliderect(ret_ciano) or ret_azul.colliderect(ret_ciano) or ret_verde.colliderect(ret_ciano) or ret_rosa.colliderect(ret_ciano):
        x_ciano = randint(40, 1900)
        y_ciano = randint(40, 980)
        if ret_vermelho.colliderect(ret_ciano):
            pontos -= 2
        if ret_azul.colliderect(ret_ciano):
            pontos2 -= 2
        if ret_verde.colliderect(ret_ciano):
            pontos3 -= 2
        if ret_rosa.colliderect(ret_ciano):
            pontos4 -= 2
        barulho_colisao.play()

    # colizao com a parede
    if ret_vermelho.x>=1870:
        posicao_jogador1[0] -= 10
    if ret_vermelho.x<20:
        posicao_jogador1[0] += 10
    if ret_vermelho.y>10:
        posicao_jogador1[1] -= 10
    if ret_vermelho.y<960:
        posicao_jogador1[1] += 10
    
    if ret_azul.x>=1870:
        posicao_jogador2[0] -= 10
    if ret_azul.x<20:
        posicao_jogador2[0] += 10
    if ret_azul.y>10:
        posicao_jogador2[1] -= 10
    if ret_azul.y<960:
        posicao_jogador2[1] += 10

    if ret_verde.x>=1870:
        posicao_jogador3[0] -= 10
    if ret_verde.x<20:
        posicao_jogador3[0] += 10
    if ret_verde.y>10:
        posicao_jogador3[1] -= 10
    if ret_verde.y<960:
        posicao_jogador3[1] += 10

    if ret_rosa.x>=1870:
        posicao_jogador4[0] -= 10
    if ret_rosa.x<20:
        posicao_jogador4[0] += 10
    if ret_rosa.y>10:
        posicao_jogador4[1] -= 10
    if ret_rosa.y<960:
        posicao_jogador4[1] += 10

    #colizao com objeto



    tela.blit(texto_formatado,(1600, 40))
    tela.blit(texto_formatado2,(50, 900))
    tela.blit(texto_formatado3,(1660, 900))
    tela.blit(texto_formatado4,(40, 40))

    pygame.display.flip()