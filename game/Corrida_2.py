import pygame
from pygame.locals import *
from sys import exit
from random import randint
import sys

pygame.init()


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

Marcha = 0
Marcha2 = 0
fonte = pygame.font.SysFont('Arial', 30, True, False)
fonte2 = pygame.font.SysFont('Arial', 30, True, False)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Corida')
relogio = pygame.time.Clock()

sprite_image1 = pygame.image.load('carro1.png')
sprite_car1 = sprite_image1.get_rect()
sprite_car1.topleft = (400, 500)

sprite_image2 = pygame.image.load('carro2.png')
sprite_car2 = sprite_image2.get_rect()
sprite_car2.topleft = (50, 500) 

imagem_fundo = pygame.image.load('rua')

speed = 3
speed2 = 3

while True:

    relogio.tick(160)
    imagem_fundo = pygame.image.load('rua')
    mesagem = f'Marcha: {Marcha}'
    mesagem2 = f'Marcha: {Marcha2}'
    
    texto_formatado = fonte.render(mesagem, False, (0, 255, 0))
    texto_formatado2 = fonte.render(mesagem2, False, (255, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    
    # Move o sprite com as setas do teclado
    if keys[pygame.K_LEFT]:  
        sprite_car1.x -= speed 
    if keys[pygame.K_RIGHT]:  
       sprite_car1.x += speed
    if keys[pygame.K_UP]:  
        sprite_car1.y -= speed  
    if keys[pygame.K_DOWN]:  
        sprite_car1.y += speed

    if keys[pygame.K_a]:  
        sprite_car2.x -= speed2
    if keys[pygame.K_d]:  
        sprite_car2.x += speed2
    if keys[pygame.K_w]:  
        sprite_car2.y -= speed2  
    if keys[pygame.K_s]:  
        sprite_car2.y += speed2

    tela.blit(imagem_fundo, (0, 0))
    tela.blit(sprite_image1, sprite_car1)
    tela.blit(sprite_image2, sprite_car2)
    pygame.display.flip()
