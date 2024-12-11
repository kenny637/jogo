import pygame
from pygame.locals import *
from sys import exit
import time
import random
import math
import sys

# Inicializa o Pygame
pygame.init()

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
vida_jogador = 100
defesa_jogador = 50
xp_jogador = 0
nivel_jogador = 1

#inimigos
tamanho_inimigo = 50
velocidade_inimigo = 2
vida_inimigos = [50, 50]  # Vida dos inimigos
inimigos = []
cooldown_ataque = 2  # Tempo em segundos entre ataques dos inimigos
ultimo_ataque = [0] * len(inimigos)  # Inicializa o tempo do último ataque de cada inimigo

# Raio de detecção dos inimigos
raio_deteccao = 200
# Carregar as imagens dos inimigos para as 4 direções (animadas)
try:
    inimigo_cima = [pygame.image.load(f'ladrao_costas{i}.png') for i in range(1, 5)]
    inimigo_baixo = [pygame.image.load(f'ladrao_frente{i}.png') for i in range(1, 5)]
    inimigo_esquerda = [pygame.image.load(f'ladrao_ladoE{i}.png') for i in range(1, 5)]
    inimigo_direita = [pygame.image.load(f'ladrao_lado{i}.png') for i in range(1, 5)]
except pygame.error as e:
    print("Erro ao carregar imagens:", e)
    pygame.quit()
    sys.exit()

# Criando 3 inimigos com posições aleatórias
for _ in range(3):
    inimigo_x = random.randint(500, 700 + metros2)
    inimigo_y = random.randint(100, 500)
    inimigos.append([inimigo_x, inimigo_y])

# Função para calcular a distância entre o jogador e o inimigo
def calcular_distancia(inimigo, jogador):
    inimigo_x, inimigo_y = inimigo
    jogador_x, jogador_y = jogador
    return math.sqrt((inimigo_x - jogador_x) ** 2 + (inimigo_y - jogador_y) ** 2)

# Definir obstáculos (paredes)
paredes = [
    pygame.Rect(200, 100, 50, 500),  # Paredes no cenário
    pygame.Rect(500, 300, 50, 400)
]

# Função para mover os inimigos com detecção de colisão
def mover_inimigos():
    global vida_jogador
    for i, inimigo in enumerate(inimigos):
        inimigo_x, inimigo_y = inimigo
        distancia = calcular_distancia(inimigo , (jogador_x, jogador_y))

        # Inicializar a direção do inimigo
        direcao_inimigo = None
        imagem_inimigo = None

        # Se o jogador estiver dentro do raio de detecção
        if distancia < raio_deteccao:
            if inimigo_x < jogador_x:
                inimigo_x += velocidade_inimigo
            elif inimigo_x > jogador_x:
                inimigo_x -= velocidade_inimigo
            if inimigo_y < jogador_y:
                inimigo_y += velocidade_inimigo
            elif inimigo_y > jogador_y:
                inimigo_y -= velocidade_inimigo

        # Verificando colisão com as paredes
        inimigo_rect = pygame.Rect(inimigo_x, inimigo_y, tamanho_inimigo, tamanho_inimigo)
        for parede in paredes:
            if inimigo_rect.colliderect(parede):
                # Colidiu com uma parede, mover o inimigo para o lado oposto
                if direcao_inimigo == 'direita':
                    inimigo_x -= velocidade_inimigo  # Empurrar para a esquerda
                elif direcao_inimigo == 'esquerda':
                    inimigo_x += velocidade_inimigo  # Empurrar para a direita
                elif direcao_inimigo == 'baixo':
                    inimigo_y -= velocidade_inimigo  # Empurrar para cima
                elif direcao_inimigo == 'cima':
                    inimigo_y += velocidade_inimigo  # Empurrar para baixo

        # Atualizando a posição do inimigo
        if direcao == "direita":
            inimigos[i] = [inimigo_x + -1, inimigo_y]
        else:
            inimigos[i] = [inimigo_x, inimigo_y]

    
        # Ataque ao jogador com verificação de colisão
        if pygame.Rect(inimigo_x, inimigo_y, tamanho_inimigo, tamanho_inimigo).colliderect(
            pygame.Rect(jogador_x, jogador_y, 80, 120)
        ):
            vida_jogador -= 1
            if vida_jogador <= 0:
                print("Você foi derrotado!")
                pygame.quit()
                exit()


        # Alterar entre as imagens das direções para animar
        if direcao_inimigo == 'direita':
            imagem_inimigo = inimigo_direita
        elif direcao_inimigo == 'esquerda':
            imagem_inimigo = inimigo_esquerda
        elif direcao_inimigo == 'cima':
            imagem_inimigo = inimigo_cima
        elif direcao_inimigo == 'baixo':
            imagem_inimigo = inimigo_baixo
        else:
            imagem_inimigo = inimigo_baixo  # Padrão para baixo

        # Alternando as imagens a cada 200ms
        tempo_animacao = pygame.time.get_ticks() // 200 % 4  # Cada 200ms alterna
        tela.blit(imagem_inimigo[tempo_animacao], (inimigo_x, inimigo_y))

    pygame.display.flip()  # Atualiza a tela

def desenhar_tela():
    tela.fill(branco)
    tela.blit(imagem_rua, (metros, -12))
    tela.blit(sprite_atual, (jogador_x, jogador_y))
    pygame.display.flip()

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

# Imagens de fundo
imagem_arvore = pygame.image.load('arvore.png')
novo_tamanho = (imagem_arvore.get_width() * 6, imagem_arvore.get_height() * 6)
imagem_aumentada = pygame.transform.scale(imagem_arvore, novo_tamanho)

imagem_arvore2 = pygame.image.load('arvore2.png')
novo_tamanho2 = (imagem_arvore.get_width() * 6, imagem_arvore2.get_height() * 6)
imagem_aumentada2 = pygame.transform.scale(imagem_arvore2, novo_tamanho2)
# Imagens de fundo e HUD
imagem_rua = pygame.image.load('chão.png')
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
        if metros <= 0:
            metros += 2
            metros2 += 2
    elif teclas[K_RIGHT]:
        dx = velocidade   
        nova_direcao = "direita"
        metros -= velocidade
        metros2 -= velocidade
    elif teclas[K_UP]:
        dy = -velocidade
        nova_direcao = "cima"
    elif teclas[K_DOWN]:
        dy = velocidade
        nova_direcao = "baixo"
    # Atualiza a direção apenas se estiver em movimento
    if nova_direcao:
        direcao = nova_direcao
        if time.time() - tempo_ultimo_frame >= tempo_por_frame:
            frame_atual = (frame_atual + 1) % len(animacao_cima)
            tempo_ultimo_frame = time.time()

    # Aplica esquiva se ativada
    if esquivando:
        if direcao == "esquerda":
            dx -= 50
        elif direcao == "direita":
            dx += 50
        elif direcao == "cima":
            dy -= 50
        elif direcao == "baixo":
            dy += 50
        esquivando = False  # Termina a esquiva após aplicar

    # Verifica colisões antes de mover
    jogador_rect = pygame.Rect(jogador_x, jogador_y, 80, 120)
    if not any(jogador_rect.colliderect(movel) for movel in paredes):
        jogador_x = max(0, min(jogador_x + dx, largura - 80))
        jogador_y = max(0, min(jogador_y + dy, altura - 120))

    # Movendo inimigos sem ultrapassar limites
    novo_rect = pygame.Rect(inimigo_x, inimigo_y, tamanho_inimigo, tamanho_inimigo)
    if not any(novo_rect.colliderect(parede) for parede in paredes):
        inimigo_x += dx
        inimigo_y += dy


    # Limites da tela para o movimento
    pj_x = max(0, min(jogador_x, largura - 80))
    pj_y = max(0, min(jogador_y, altura - 120))

    # Seleciona a imagem do jogador baseada na direção
    if direcao == "cima":
        sprite_atual = animacao_cima[frame_atual]
    elif direcao == "baixo":
        sprite_atual = animacao_baixo[frame_atual]
    elif direcao == "esquerda":
        sprite_atual = animacao_esquerda[frame_atual]
    elif direcao == "direita":
        sprite_atual = animacao_direita[frame_atual]

    if metros <= -750:
        metros = 0
    
    saida_rua = pygame.draw.rect(tela, vermelho, (780, 100, 10, 400))

    if metros2 <= -3000 and jogador_rect.colliderect(saida_rua):
        pygame.quit()
        exit()
        
    # Desenha o fundo e as informações do jogador
    tela.blit(imagem_rua, (metros, -12))
    # Desenha o jogador
    tela.blit(sprite_atual, (jogador_x, jogador_y))
    
    tela.blit(imagem_aumentada, (1000 + metros2 + 1, 130))
    tela.blit(imagem_aumentada2, (2000 + metros2 + 1, 170))
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


    mover_inimigos()
    font = pygame.font.SysFont(None, 36)
    # Exibir a vida dos inimigos
    # Exemplo ao detectar ataque do jogador
    for i, inimigo in enumerate(inimigos):
        distancia = calcular_distancia(inimigo, (jogador_x, jogador_y))
        if distancia < 50:  # Verifica se o jogador está próximo
            if evento.type == pygame.KEYDOWN and evento.key == K_f:  # Exemplo de ataque
                vida_inimigos[i] -= 10
                if vida_inimigos[i] <= 0:
                    del inimigos[i]
                    del vida_inimigos[i]
                    break


    # Atualiza a tela
    pygame.display.flip()
 