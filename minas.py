from typing import Any
import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

'''pygame.mixer_music.set_volume(0.9)
musica_de_fundo = pygame.mixer.music.load('Super Mario Bros. Theme Song.mp3')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('Super Mario Bros. - Coin Sound Effect.mp3')
barulho_colisao.set_volume(0.9)'''

largura = 1366
altura = 710
p1_x = (30)
p1_y = (350)

p2_x = (30)
p2_y = (400)

p3_x = (30)
p3_y = (450)

speed = 5

pontos = 0
fonte = pygame.font.SysFont('Arial', 40, True, False)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('RPG')
relogio = pygame.time.Clock()

while True:
    relogio.tick(99999999999)
    tela.fill((0,0,0))
    mesagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mesagem, False, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        pygame.display.flip()
       
    if pygame.key.get_pressed()[K_a]:
        p1_x += - speed
    if pygame.key.get_pressed()[K_d]:
        p1_x += + speed
    if pygame.key.get_pressed()[K_w]:
        p1_y += - speed
    if pygame.key.get_pressed()[K_s]:
        p1_y += + speed

    if pygame.key.get_pressed()[K_LEFT]:
        p2_x += - speed
    if pygame.key.get_pressed()[K_RIGHT]:
        p2_x += + speed
    if pygame.key.get_pressed()[K_UP]:
        p2_y += - speed
    if pygame.key.get_pressed()[K_DOWN]:
        p2_y += + speed

    if pygame.key.get_pressed()[K_KP_4]:
        p3_x += - speed
    if pygame.key.get_pressed()[K_KP_6]:
        p3_x += + speed
    if pygame.key.get_pressed()[K_KP_8]:
        p3_y += - speed
    if pygame.key.get_pressed()[K_KP_5]:
        p3_y += + speed

    #ret_verde = pygame.draw.rect(tela, (0,250,0), (p1_x,p1_y,50,50))
    ret_verde = pygame.draw.circle(tela, (0,250,0), (p1_x,p1_y),20)
    ret_Vermelho = pygame.draw.circle(tela, (255,0,0), (p2_x,p2_y),20)
    ret_Azul = pygame.draw.circle(tela, (0,0,255), (p3_x,p3_y),20)

    ret_1 = pygame.draw.rect(tela, (250,0,0), (60, 300, 30, 400))
    ret_2 = pygame.draw.rect(tela, (250,0,0), (0, 180, 200, 30))
    ret_3 = pygame.draw.rect(tela, (250,0,0), (200, 180, 30, 400))
    ret_4 = pygame.draw.rect(tela, (250,0,0), (20, 550, 70, 30))
    ret_5 = pygame.draw.rect(tela, (250,0,0), (60, 650, 650, 30))
    ret_6 = pygame.draw.rect(tela, (250,0,0), (200, 550, 400, 30))
    ret_7 = pygame.draw.rect(tela, (250,0,0), (570, 400, 30, 150))
    ret_8 = pygame.draw.rect(tela, (250,0,0), (690, 300, 30, 380))
    ret_9 = pygame.draw.rect(tela, (250,0,0), (300, 290, 420, 30))
    
    ret_10 = pygame.draw.rect(tela, (250,0,0), (300, 100, 30, 250))
    ret_11 = pygame.draw.rect(tela, (250,0,0), (300, 200, 230, 50))
    ret_12 = pygame.draw.rect(tela, (250,0,0), (60, 300, 30, 250))
 
    if p1_x <= 15 :
        p1_x += 5
    if p1_x >= 1350:
        p1_x -= 5
    if p1_y <= 15:
        p1_y += 5
    if p1_y >= 685:
        p1_y -= 5
    
    if p2_x <= 15 :
        p2_x += 5
    if p2_x >= 1350:
        p2_x -= 5
    if p2_y <= 15:
        p2_y += 5
    if p2_y >= 685:
        p2_y -= 5

    if p3_x <= 15 :
        p3_x += 5
    if p3_x >= 1350:
        p3_x -= 5
    if p3_y <= 15:
        p3_y += 5
    if p3_y >= 685:
        p3_y -= 5

    if ret_verde.colliderect(ret_1) or ret_verde.colliderect(ret_2) or ret_verde.colliderect(ret_3) or ret_verde.colliderect(ret_4) or ret_verde.colliderect(ret_5) or ret_verde.colliderect(ret_6) or ret_verde.colliderect(ret_7) or ret_verde.colliderect(ret_8) or ret_verde.colliderect(ret_9) or ret_verde.colliderect(ret_10) or ret_verde.colliderect(ret_11) or ret_verde.colliderect(ret_12) :
        p1_x = (30)
        p1_y = (350)
    if ret_Vermelho.colliderect(ret_1) or ret_Vermelho.colliderect(ret_2) or ret_Vermelho.colliderect(ret_3) or ret_Vermelho.colliderect(ret_4) or ret_Vermelho.colliderect(ret_5) or ret_Vermelho.colliderect(ret_6) or ret_Vermelho.colliderect(ret_7) or ret_Vermelho.colliderect(ret_8) or ret_Vermelho.colliderect(ret_9) or ret_Vermelho.colliderect(ret_10) or ret_Vermelho.colliderect(ret_11) or ret_Vermelho.colliderect(ret_12) :
        p2_x = (30)
        p2_y = (400)
    if ret_Azul.colliderect(ret_1) or ret_Azul.colliderect(ret_2) or ret_Azul.colliderect(ret_3) or ret_Azul.colliderect(ret_4) or ret_Azul.colliderect(ret_5) or ret_Azul.colliderect(ret_6) or ret_Azul.colliderect(ret_7) or ret_Azul.colliderect(ret_8) or ret_Azul.colliderect(ret_9) or ret_Azul.colliderect(ret_10) or ret_Azul.colliderect(ret_11) or ret_Azul.colliderect(ret_12) :
        p3_x = (30)
        p3_y = (450)


    tela.blit(texto_formatado,(450, 450))
    pygame.display.update()