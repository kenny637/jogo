import pygame
from pygame.locals import *
from sys import exit
from random import randint
import sys

pygame.init()

'''pygame.mixer_music.set_volume(0.9)
musica_de_fundo = pygame.mixer.music.load('Super Mario Bros. Theme Song.mp3')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('Efeito sonoro da moeda do Mario..mp3')
barulho_colisao.set_volume(0.9)'''

largura = 600
altura = 700
x = int(largura/2)
y = int(altura/2)

posicao_jogador = [550, 600]
posicao_jogador2 = [20, 600]
tamanho_jogador1 = 50
tamanho_jogador2 = 90


#cores
verde = (0, 255, 0)
azul = (0, 0, 255 )

x_amarelo = randint(40, 630)
x_amarelo1 = randint(40, 630)
x_amarelo2 = randint(40, 630)
x_amarelo3 = randint(40, 630)
x_amarelo4 = randint(40, 630)
x_amarelo5 = randint(40, 630)
x_amarelo6 = randint(40, 630)

pontos = 0
pontos2 = 0
fonte = pygame.font.SysFont('Arial', 30, True, False)
fonte2 = pygame.font.SysFont('Arial', 30, True, False)
fonte3 = pygame.font.SysFont('Arial', 30, True, False)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Corida')
relogio = pygame.time.Clock()

cont = cont1 = cont2 = cont3 = cont4 = cont5 = cont6 = 0
speed = 3
 
sprite_image2 = pygame.image.load('car 3.png')
sprite_rectcar2 = sprite_image2.get_rect()
sprite_rectcar2.topleft = (50, 500) 

sprite_image1 = pygame.image.load('car 2.png')
sprite_rectcar1 = sprite_image1.get_rect()
sprite_rectcar1.topleft = (400, 500)

sprite_image = pygame.image.load('car 1.png')
sprite_rect = sprite_image.get_rect()
sprite_rect.topleft = (x_amarelo,cont)

sprite_image = pygame.image.load('car 1.png')
sprite_rect1 = sprite_image.get_rect()
sprite_rect1.topleft = (x_amarelo1,cont1)

sprite_image = pygame.image.load('car 1.png')
sprite_rect2 = sprite_image.get_rect()
sprite_rect2.topleft = (x_amarelo2,cont2)

sprite_image = pygame.image.load('car 1.png')
sprite_rect3 = sprite_image.get_rect()
sprite_rect3.topleft = (x_amarelo3,cont3)

sprite_image = pygame.image.load('car 1.png')
sprite_rect4 = sprite_image.get_rect()
sprite_rect4.topleft = (x_amarelo4,cont4)

sprite_image = pygame.image.load('car 1.png')
sprite_rect5 = sprite_image.get_rect()
sprite_rect5.topleft = (x_amarelo5,cont5)

sprite_image = pygame.image.load('car 1.png')
sprite_rect6 = sprite_image.get_rect()
sprite_rect6.topleft = (x_amarelo6,cont6)

imagem_fundo = pygame.image.load('rua.png')
novo_tamanho = (imagem_fundo.get_width() * 7, imagem_fundo.get_height() * 10)
imagem_aumentada = pygame.transform.scale(imagem_fundo, novo_tamanho)

while True:
    cont += 3
    cont1 += 2
    cont2 += 1.7
    cont3 += 1.2
    cont4 += 0.7
    cont5 += 1.5
    cont6 += 2.3
    relogio.tick(160)
    imagem_fundo = pygame.image.load('rua.png')
    mesagem = f'Verde: {pontos}'
    mesagem2 = f'Vermelho: {pontos2}'
    mesagem3 = 'Game Over'
    texto_formatado = fonte.render(mesagem, False, (0, 255, 0))
    texto_formatado2 = fonte.render(mesagem2, False, (255, 0, 0))
    texto_formatado3 = fonte.render(mesagem3, False, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

   
    sprite_rect.topleft = (x_amarelo,cont)
    sprite_rect1.topleft = (x_amarelo1,cont1)
    sprite_rect2.topleft = (x_amarelo2,cont2)
    sprite_rect3.topleft = (x_amarelo3,cont3)
    sprite_rect4.topleft = (x_amarelo4,cont4)
    sprite_rect5.topleft = (x_amarelo5,cont5)
    sprite_rect6.topleft = (x_amarelo6,cont6)

    
    keys = pygame.key.get_pressed()
    
    # Move o sprite com as setas do teclado
    if keys[pygame.K_LEFT]:  
        sprite_rectcar1.x -= speed 
    if keys[pygame.K_RIGHT]:  
        sprite_rectcar1.x += speed
    if keys[pygame.K_UP]:  
        sprite_rectcar1.y -= speed  
    if keys[pygame.K_DOWN]:  
        sprite_rectcar1.y += speed

    if keys[pygame.K_a]:  
        sprite_rectcar2.x -= speed 
    if keys[pygame.K_d]:  
        sprite_rectcar2.x += speed
    if keys[pygame.K_w]:  
        sprite_rectcar2.y -= speed  
    if keys[pygame.K_s]:  
        sprite_rectcar2.y += speed
    

    if sprite_rectcar1.colliderect(sprite_rect) or sprite_rectcar1.colliderect(sprite_rect1) or sprite_rectcar1.colliderect(sprite_rect2) or sprite_rectcar1.colliderect(sprite_rect3) or sprite_rectcar1.colliderect(sprite_rect4) or sprite_rectcar1.colliderect(sprite_rect5) or sprite_rectcar1.colliderect(sprite_rect6):
        tela.blit(texto_formatado3,(largura/2.3, altura/2.6))
        #barulho_colisao.play()
        break

    if sprite_rectcar2.colliderect(sprite_rect) or sprite_rectcar2.colliderect(sprite_rect1) or sprite_rectcar2.colliderect(sprite_rect2) or sprite_rectcar2.colliderect(sprite_rect3) or sprite_rectcar2.colliderect(sprite_rect4) or sprite_rectcar2.colliderect(sprite_rect5) or sprite_rectcar2.colliderect(sprite_rect6):
        tela.blit(texto_formatado3,(largura/2.3, altura/2.6))
        #barulho_colisao.play()
        break

    
    if sprite_rectcar1.x>=555:
        sprite_rectcar1[0] -= speed
    if sprite_rectcar1.x<0:
        sprite_rectcar1[0] += speed
    if sprite_rectcar1.y>0:
        sprite_rectcar1[1] -= speed
    if sprite_rectcar1.y<620:
        sprite_rectcar1[1] += speed

    if sprite_rectcar2.x>=555:
        sprite_rectcar2[0] -= speed
    if sprite_rectcar2.x<0:
        sprite_rectcar2[0] += speed
    if sprite_rectcar2.y>0:
        sprite_rectcar2[1] -= speed
    if sprite_rectcar2.y<620:
        sprite_rectcar2[1] += speed


    if sprite_rect.y>=720:
        x_amarelo = randint(10, 580)
        cont = -50
        pontos += 1
        pontos2 += 1
    if sprite_rect1.y>=720:
        x_amarelo1 = randint(10, 580)    
        cont1 = -150
        pontos += 1
        pontos2 += 1
    if sprite_rect2.y>=720:
        x_amarelo2 = randint(10, 580)    
        cont2 = -250
        pontos += 1
        pontos2 += 1
    if sprite_rect3.y>=720:
        x_amarelo3 = randint(10, 580)    
        cont3 = -200
        pontos += 1
        pontos2 += 1
    if sprite_rect4.y>=720:
        x_amarelo4 = randint(10, 580)
        cont4 = -50
        pontos += 1
        pontos2 += 1
    if sprite_rect5.y>=720:
        x_amarelo5 = randint(10, 580)    
        cont5 = -50
        pontos += 1
        pontos2 += 1
    if sprite_rect6.y>=720:
        x_amarelo6 = randint(10, 580)    
        cont6 = -50
        pontos += 1
        pontos2 += 1

    tela.blit(imagem_aumentada, (-25, 0))
    tela.blit(texto_formatado,(470, 0))
    tela.blit(texto_formatado2,(10, 20))
    
    tela.blit(sprite_image, sprite_rect)
    tela.blit(sprite_image, sprite_rect1)
    tela.blit(sprite_image, sprite_rect2)
    tela.blit(sprite_image, sprite_rect3)
    tela.blit(sprite_image, sprite_rect4)
    tela.blit(sprite_image, sprite_rect5)
    tela.blit(sprite_image, sprite_rect6)
    tela.blit(sprite_image1, sprite_rectcar1)
    tela.blit(sprite_image2, sprite_rectcar2)
    

    if pontos >= 50:
        cont += 0.5
        cont1 += 0.5
        cont2 += 0.5
        cont3 += 0.5
        cont4 += 0.5
        cont5 += 0.5
        cont6 += 0.5
    if pontos >= 100:
        cont += 0.5
        cont1 += 0.5
        cont2 += 0.5
        cont3 += 0.5
        cont4 += 0.5
        cont5 += 0.5
        cont6 += 0.5
   

    pygame.display.flip()