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
amarelo = (245, 186, 24)
branco = (255, 255, 255)
roxo = (147, 112, 219)
azul = (0, 0, 255)

# Jogador
velocidade = 3
pj_x, pj_y = 100, 400
vida_jogador = 100
defesa_jogador = 50
xp_jogador = 0
nivel_jogador = 1

# Esquiva
esquivando = False
tempo_esquiva = 2  # 2 segundos entre esquivas
ultimo_temporal_esquiva = 0

# Animações do jogador
animacao_cima = [pygame.image.load(f"protagonista_costa{i}.png") for i in range(1, 5)]
animacao_baixo = [pygame.image.load(f"protagonista_frente{i}.png") for i in range(1, 5)]
animacao_esquerda = [pygame.image.load(f"protagonista_ladoE{i}.png") for i in range(1, 5)]
animacao_direita = [pygame.image.load(f"protagonista_lado{i}.png") for i in range(1, 5)]

direcao = "baixo"
frame_atual = 0
tempo_por_frame = 0.1  # Segundos por frame (ajuste conforme necessário)
tempo_ultimo_frame = time.time()

# Imagens de fundo e HUD
imagem_casa = pygame.image.load('casa.png')
imagem_casa = pygame.transform.scale(imagem_casa, (largura, altura))
imagem_coracao = pygame.image.load('coração.png')
imagem_escudo = pygame.image.load('Escudo1.png')

# Fontes
fonte = pygame.font.SysFont('Arial', 30, True, False)

# Relógio para FPS
relogio = pygame.time.Clock()

# Móveis (obstáculos)
paredes = [
        pygame.Rect(60, 200, 120, 150),
        pygame.Rect(220, 230, 100, 10),
        pygame.Rect(0, -20, 800, 220),
        pygame.Rect(540, 230, 120, 10),
        pygame.Rect(570, 370, 200, 10),
        pygame.Rect(670, 250, 20, 50),
        pygame.Rect(425, 230, 70, 10),
        pygame.Rect(400, 610, 190, 70)
    ]

# Loop principal
# Loop principal
while True:
    tempo_atual = time.time()
    relogio.tick(60)  # 60 FPS

    # Eventos
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            exit()

        # Detecta esquiva
        if evento.type == pygame.KEYDOWN:
            if evento.key == K_SPACE and tempo_atual - ultimo_temporal_esquiva >= tempo_esquiva:
                esquivando = True
                ultimo_temporal_esquiva = tempo_atual

    # Desenha o fundo e as informações do jogador
    tela.blit(imagem_casa, (0, 0))

    saida_casa = pygame.draw.rect(tela, vermelho, (750, 600, 100, 80))

    pygame.draw.rect(tela, vermelho, (25, 13, vida_jogador, 30))  # Barra de vida
    pygame.draw.rect(tela, amarelo, (30, 65, defesa_jogador, 30))  # Barra de defesa
    tela.blit(imagem_coracao, (-18, -18))
    tela.blit(imagem_escudo, (-18, 35))

    # Renderiza textos
    tela.blit(fonte.render(f'      {vida_jogador}', False, branco), (30, 10))
    tela.blit(fonte.render(f'      {defesa_jogador}', False, branco), (30, 60))
    tela.blit(fonte.render(f'Nível: {nivel_jogador}', False, branco), (30, 120))
    tela.blit(fonte.render(f'XP: {xp_jogador}', False, roxo), (30, 160))

    # Mostrar o cooldown da esquiva
    if tempo_atual - ultimo_temporal_esquiva < tempo_esquiva:
        # Mostra a barra de cooldown
        cooldown_barra = pygame.Rect(25, 220, 200 * (1 - (tempo_atual - ultimo_temporal_esquiva) / tempo_esquiva), 20)
        pygame.draw.rect(tela, azul, cooldown_barra)

    # Movimentação do jogador
    teclas = pygame.key.get_pressed()
    dx, dy = 0, 0
    nova_direcao = None

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

    # Atualiza a direção apenas se estiver em movimento
    if nova_direcao:
        direcao = nova_direcao
        if tempo_atual - tempo_ultimo_frame >= tempo_por_frame:
            frame_atual = (frame_atual + 1) % len(animacao_cima)
            tempo_ultimo_frame = tempo_atual

    # Executa esquiva
    if esquivando:
        if direcao == "esquerda":
            dx -= 100
        elif direcao == "direita":
            dx += 100
        elif direcao == "cima":
            dy -= 100
        elif direcao == "baixo":
            dy += 100
        esquivando = False

    # Verifica colisões antes de mover
    novo_rect = pygame.Rect(pj_x + dx, pj_y + dy, 80, 120)
    if not any(novo_rect.colliderect(movel) for movel in paredes):
        pj_x += dx
        pj_y += dy

    # Limites da tela para o movimento
    pj_x = max(0, min(pj_x, largura - 80))
    pj_y = max(0, min(pj_y, altura - 120))

    # Seleciona a imagem do jogador baseada na direção
    if direcao == "cima":
        sprite_atual = animacao_cima[frame_atual]
    elif direcao == "baixo":
        sprite_atual = animacao_baixo[frame_atual]
    elif direcao == "esquerda":
        sprite_atual = animacao_esquerda[frame_atual]
    elif direcao == "direita":
        sprite_atual = animacao_direita[frame_atual]

    # Desenha o jogador
    tela.blit(sprite_atual, (pj_x, pj_y))

    # Atualiza a tela
    pygame.display.flip()
