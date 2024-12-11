import pygame
from pygame.locals import *
from sys import exit
from random import randint
import sys
# Inicializa o Pygame
pygame.init()

# Configurações da janela
largura, altura = 800, 800
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Tela inicio")

# Carregar os quadros da animação (7 imagens)
frame_1 = pygame.image.load('mapa1.png')
frame_2 = pygame.image.load('mapa2.png')
frame_3 = pygame.image.load('mapa3.png')
frame_4 = pygame.image.load('mapa4.png')
frame_5 = pygame.image.load('mapa3.png')
frame_6 = pygame.image.load('mapa2.png')
frame_7 = pygame.image.load('mapa1.png')

# Redimensionar as imagens para o dobro do tamanho
nova_largura = 700  # Novo tamanho de largura
nova_altura = 700  # Novo tamanho de altura

frame_1 = pygame.transform.scale(frame_1, (nova_largura, nova_altura))
frame_2 = pygame.transform.scale(frame_2, (nova_largura, nova_altura))
frame_3 = pygame.transform.scale(frame_3, (nova_largura, nova_altura))
frame_4 = pygame.transform.scale(frame_4, (nova_largura, nova_altura))
frame_5 = pygame.transform.scale(frame_5, (nova_largura, nova_altura))
frame_6 = pygame.transform.scale(frame_6, (nova_largura, nova_altura))
frame_7 = pygame.transform.scale(frame_7, (nova_largura, nova_altura))

# Coloque os quadros redimensionados em uma lista
quadros = [frame_1, frame_2, frame_3, frame_4, frame_5, frame_6, frame_7]

# Posições iniciais para o quadro de animação
x, y = 60, 40
indice_quadro = 0  # Índice do quadro atual

# Botões do menu
retangulo_iniciar = pygame.Rect(320, 320, 170, 60)
retangulo_sair = pygame.Rect(320, 400, 170, 60)

relogio = pygame.time.Clock()
# Loop principal do jogo
while True:
    relogio.tick(10)
    tela.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    tela.blit(quadros[indice_quadro], (x, y))
    indice_quadro = (indice_quadro + 1) % len(quadros)

    pygame.display.flip()

