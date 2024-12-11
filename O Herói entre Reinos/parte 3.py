import pygame
from pygame.locals import *
from sys import exit
import time
import random
import math
import sys

import pygame
from pygame.locals import *
from sys import exit
import time

# Inicializa o Pygame
pygame.init()

# Configurações da janela
largura, altura = 800, 700
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Casa")

# Cores
vermelho = (255, 0, 0)
branco = (255, 255, 255)

# Jogador
jogador_x, jogador_y = 100, 350
velocidade = 3
vida_jogador = 300

direcao = "baixo"
frame_atual = 0
tempo_por_frame = 0.1  # Segundos por frame

# Animações do jogador
animacao_ataque = {
    "cima": [pygame.image.load(f"protagonista_costa{i}.png") for i in range(1, 4)],
    "baixo": [pygame.image.load(f"protagonista_frente_espa{i}.png") for i in range(1, 3)],
    "esquerda": [pygame.image.load(f"protagonista_ladoE_espa{i}.png") for i in range(1, 3)],
    "direita": [pygame.image.load(f"protagonista_lado_espa{i}.png") for i in range(1, 3)],
}
animacao_normal = {
    "cima": [pygame.image.load(f"protagonista_costa{i}.png") for i in range(1, 5)],
    "baixo": [pygame.image.load(f"protagonista_frente_espa{i}.png") for i in range(1, 5)],
    "esquerda": [pygame.image.load(f"protagonista_ladoE_espa{i}.png") for i in range(1, 5)],
    "direita": [pygame.image.load(f"protagonista_lado_espa{i}.png") for i in range(1, 5)],
}

# Controle de ataque
atacando = False
ultimo_ataque = 0
cooldown_ataque = 0.5  # Em segundos

# Relógio para FPS
relogio = pygame.time.Clock()

metros = 0
metros2 = 0
# Configurações da janela
largura, altura = 800, 700
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Casa")

# Cores
vermelho = (255, 0, 0)
amarelo = (245, 186, 24)
branco = (255, 255, 255)
roxo = (147, 112, 219)
azul = (0, 0, 255)

# Jogador
velocidade = 3
po_jo = [100, 350]
jogador_x = 100
jogador_y = 350
vida_jogador = 300
defesa_jogador = 200
xp_jogador = 0
nivel_jogador = 1



# Raio de detecção dos inimigos
# Esquiva
esquivando = False
tempo_esquiva = 2  # 2 segundos entre esquivas
ultimo_temporal_esquiva = 0

# Animações do jogador
direcao = "baixo"
frame_atual = 0
tempo_por_frame = 0.1  # Segundos por frame (ajuste conforme necessário)
tempo_ultimo_frame = time.time()

# Imagens de fundo e HUD
imagem_rua = pygame.image.load('chão2.png')
imagem_rua = pygame.transform.scale(imagem_rua, (largura*2, altura))
imagem_coracao = pygame.image.load('coração.png')
imagem_escudo = pygame.image.load('Escudo1.png')

# Fontes
fonte = pygame.font.SysFont('Arial', 30, True, False)

# Relógio para FPS
relogio = pygame.time.Clock()

# Móveis (obstáculos)
paredes = [
]

# Loop principal
while True:
    tempo_atual = time.time()
    relogio.tick(60)  # 60 FPS

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            exit()

        if evento.type == KEYDOWN:
            if evento.key == K_SPACE and not atacando and tempo_atual - ultimo_ataque >= cooldown_ataque:
                atacando = True
                ultimo_ataque = tempo_atual
                frame_atual = 0  # Reinicia a animação de ataque

    # Movimentação do jogador
    teclas = pygame.key.get_pressed()
    dx, dy = 0, 0
    nova_direcao = None

    if not atacando:  # Não se move enquanto ataca
        if teclas[K_LEFT]:
            dx = -velocidade
            nova_direcao = "esquerda"
        elif teclas[K_RIGHT]:
            dx = velocidade
            nova_direcao = "direita"
        elif teclas[K_UP]:
            dy = -velocidade
            nova_direcao = "cima"
        elif teclas[K_DOWN]:
            dy = velocidade
            nova_direcao = "baixo"

    if nova_direcao:
        direcao = nova_direcao
        if time.time() - ultimo_ataque >= tempo_por_frame:
            frame_atual = (frame_atual + 1) % len(animacao_normal[direcao])

    jogador_x += dx
    jogador_y += dy

    # Seleciona a animação correta
    if atacando:
        if frame_atual < len(animacao_ataque[direcao]):
            sprite_atual = animacao_ataque[direcao][frame_atual]
            if tempo_atual - ultimo_ataque >= tempo_por_frame:
                frame_atual += 1
        else:
            atacando = False
    else:
        sprite_atual = animacao_normal[direcao][frame_atual]

    # Limites da tela
    jogador_x = max(0, min(jogador_x, largura - 80))
    jogador_y = max(0, min(jogador_y, altura - 120))

    # Desenha o fundo e o jogador
    tela.fill(branco)
    tela.blit(sprite_atual, (jogador_x, jogador_y))
    
    if metros <= -750:
        metros = 0
    
    saida_rua = pygame.draw.rect(tela, vermelho, (780, 100, 10, 400))
        
    # Desenha o fundo e as informações do jogador
    tela.blit(imagem_rua, (metros, -12))
    # Desenha o jogador
    tela.blit(sprite_atual, (jogador_x, jogador_y))

    pygame.draw.rect(tela, vermelho, (25, 13, vida_jogador, 30))  # Barra de vida
    pygame.draw.rect(tela, amarelo, (30, 65, defesa_jogador, 30))  # Barra de defesa
    tela.blit(imagem_coracao, (-18, -18))
    tela.blit(imagem_escudo, (-18, 35))

    # Renderiza textos
    tela.blit(fonte.render(f'      {vida_jogador}', False, branco), (30, 10))
    tela.blit(fonte.render(f'      {defesa_jogador}', False, branco), (30, 60))
    tela.blit(fonte.render(f'Nível: {nivel_jogador}', False, branco), (30, 120))
    tela.blit(fonte.render(f'XP: {xp_jogador}', False, roxo), (30, 160))
    print(metros2)

    # Atualiza a tela
    pygame.display.flip()
 