import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

'''pygame.mixer_music.set_volume(0.9)
musica_de_fundo = pygame.mixer.music.load('Super Mario Bros. Theme Song.mp3')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('Efeito sonoro da moeda do Mario..mp3')
barulho_colisao.set_volume(0.9)'''

largura = 700
altura = 500
x = int(largura/2)
y = int(altura/2)

posicao_jogador = [550, 600]
posicao_jogador2 = [20, 600]
tamanho_jogador1 = 50
tamanho_jogador2 = 90

#cores
verde = (0, 255, 0)
azul = (0, 0, 255 )

x_1 = randint(-280, 0)

pontos = 0

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('flappy bird')
relogio = pygame.time.Clock()

cont = 650
cont2 = 0
speed = 10

sprite_image = pygame.image.load('passaro.png')
sprite_passaro = sprite_image.get_rect()
sprite_passaro.topleft = (largura/2.2, altura/2.2)

imagem_fundo = pygame.image.load('cano 1.png')
novo_tamanho = (imagem_fundo.get_width() * 1, imagem_fundo.get_height() * 3.5)
imagem_aumentada = pygame.transform.scale(imagem_fundo, novo_tamanho)

imagem_fundo2 = pygame.image.load('cano 2.png')
novo_tamanho2 = (imagem_fundo2.get_width() * 1, imagem_fundo2.get_height() * 3.5)
imagem_aumentada2 = pygame.transform.scale(imagem_fundo2, novo_tamanho2)

imagem_fundo3 = pygame.image.load('cidade.png')
novo_tamanho3 = (imagem_fundo3.get_width() * 8, imagem_fundo3.get_height() * 7)
imagem_aumentada3 = pygame.transform.scale(imagem_fundo3, novo_tamanho3)

fonte = pygame.font.SysFont('Arial', 40, True, False)

while True:
    cont -= 2
    cont2 += 2
    relogio.tick(160)        
    imagem_fundo = pygame.image.load('cidade.png')
    mesagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mesagem, False, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        cont2 -= 5  

    if cont == -80:
        x_1 = randint(-260, 0)
        cont = 660

    if cont2 <= -30 or cont2 >= 480:
        break

    if cont == 280:
        pontos +=1 

    tela.blit(imagem_aumentada3, (0, -6))  
    tela.blit(imagem_aumentada2, (cont, x_1))  
    tela.blit(imagem_aumentada, (cont, x_1 + 500))   
    tela.blit(sprite_image, (300, cont2))
    tela.blit(texto_formatado,(450, 50))   

    cano_topo = pygame.draw.rect(tela, (250,0,0), (cont + 30, x_1, 20, 300))
    cano_inferior = pygame.draw.rect(tela, (250,0,0), (cont + 30, x_1 + 500, 20, 300))

    if sprite_passaro.colliderect(cano_topo) or sprite_passaro.colliderect(cano_inferior):
        pontos += 1
    
    

    pygame.display.flip() 