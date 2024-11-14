from typing import Any
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

largura = 800
altura = 500
x = int(largura/2)
y = int(altura/2)

posicao_jogador = [80, 400]
posicao_jogador2 = [660, 400]
tamanho_jogador1 = 50
tamanho_jogador2 = 50

#cores
verde = (0, 255, 0)
vermelho = (255, 0, 0)
azul = (0, 0, 255)

pontos = 0
fonte = pygame.font.SysFont('Arial', 30, True, False)
fonte2 = pygame.font.SysFont('Arial', 30, True, False)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('RPG')
relogio = pygame.time.Clock()

ret_espada = pygame.draw.rect(tela, (211, 211, 211),(posicao_jogador2[0], posicao_jogador2[1],80, 10))
ret_espada2 = pygame.draw.rect(tela, (128, 128, 128),(posicao_jogador[0], posicao_jogador[1],80, 10))
    
while True:
    relogio.tick(120)
    tela.fill((0,0,0))
    mesagem = f'Pontos: {pontos}'
    mesagem2 = 'Game Over'
    texto_formatado = fonte.render(mesagem, False, (255, 255, 255))
    texto_formatado2 = fonte.render(mesagem2, False, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    
        ret_espada2 = pygame.draw.rect(tela, (128, 128, 128),(posicao_jogador[0]+50, posicao_jogador[1]+10, 80, 12))

    if pygame.key.get_pressed()[K_w]:
        posicao_jogador2[1] -= 5
    if pygame.key.get_pressed()[K_s]:
        posicao_jogador2[1] += 5
    if pygame.key.get_pressed()[K_a]:
        posicao_jogador2[0] -= 5
    if pygame.key.get_pressed()[K_d]:
        posicao_jogador2[0] += 5
    if pygame.key.get_pressed()[K_e]:
        ret_espada = pygame.draw.rect(tela, (211, 211, 211),(posicao_jogador2[0]-50, posicao_jogador2[1]+10, 80, 12))
    
    ret_azul = pygame.draw.rect(tela,azul, (posicao_jogador[0], posicao_jogador[1], tamanho_jogador1, tamanho_jogador2))
    ret_vermelho = pygame.draw.rect(tela,vermelho, (posicao_jogador2[0], posicao_jogador2[1], tamanho_jogador1, tamanho_jogador2))
    ret_parede = pygame.draw.line(tela, (0, 100, 0),(-10, 490),(800, 490),40)
    
    if ret_azul.colliderect(ret_espada):
        
        tela.blit(texto_formatado2,(posicao_jogador[0]-40,posicao_jogador[1]-30))
    if ret_vermelho.colliderect(ret_espada2):
        
        tela.blit(texto_formatado2,(posicao_jogador2[0]-40,posicao_jogador2[1]-30))

    if ret_vermelho.x>=750:
        posicao_jogador2[0] -= 10
    if ret_vermelho.x<=0:
        posicao_jogador2[0] += 10
    if ret_vermelho.y>=10:
        posicao_jogador2[1] -= 10
    if ret_vermelho.y<430:
        posicao_jogador2[1] += 10

    if ret_azul.x>=750:
        posicao_jogador[0] -= 10
    if ret_azul.x<=0:
        posicao_jogador[0] += 10
    if ret_azul.y>=10:
        posicao_jogador[1] -= 10
    if ret_azul.y<=420:
        posicao_jogador[1] += 10

    pygame.display.flip()