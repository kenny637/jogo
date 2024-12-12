import pygame
from pygame.locals import *
from sys import exit
import time

# Inicializa o Pygame
pygame.init()

# Configurações da janela
largura, altura = 800, 700
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Personagem e Dragão")

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
FPS = 60

# Carregar imagens com tratamento de erro
def carregar_imagem(caminho, tamanho=None):
    try:
        imagem = pygame.image.load(caminho)
        if tamanho:
            imagem = pygame.transform.scale(imagem, tamanho)
        return imagem
    except pygame.error as e:
        print(f"Erro ao carregar imagem {caminho}: {e}")
        return None

# Carregar imagens
imagem_dragao_dormindo = carregar_imagem("dragao sono.png", (100, 50))
imagem_dragao_acordado = carregar_imagem("dragao voo.png", (300, 150))
imagem_dragao_ataque = carregar_imagem("dragao ataque_certo.png", (300, 150))
imagem_bola_fogo = carregar_imagem("bola de fogo (1).png", (100, 60))

# Jogador
jogador = pygame.Rect(100, 350, 60, 100)
velocidade_jogador = 3
vida_jogador = 300
defesa_jogador = 200
xp_jogador = 0
nivel_jogador = 1

# Animações do jogador
animacao_ataque = {
    "cima": [pygame.image.load(f"protagonista_costa{i}.png") for i in range(1, 4)],
    "baixo": [pygame.image.load(f"protagonista_frente_espa{i}.png") for i in range(1, 3)],
    "esquerda": [pygame.image.load(f"p_ladoE_espa_atak{i}.png") for i in range(2, 4)],
    "direita": [pygame.image.load(f"p_lado_espa_atak{i}.png") for i in range(2, 4)],
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

# Esquiva
esquivando = False
tempo_esquiva = 2  # 2 segundos entre esquivas
ultimo_temporal_esquiva = 0

# Configurações do dragão
dragao = pygame.Rect(480, 100, 300, 150)  # Posição x do dragão ajustada
velocidade_dragao = 3
direcao_dragao = 1
dragao_parado = False
imagem_dragao = imagem_dragao_dormindo
temporizador_acordar = 0
COOLDOWN_BOLA_FOGO = 10
DURAÇÃO_PARADA = 60
temporizador_ataque_dragao = 0  # Temporizador para a imagem de ataque
temporizador_parada_dragao = 0

# Configurações do ataque do dragão
bola_fogo = None
velocidade_bola_fogo = 7
temporizador_bola_fogo = 0

# Adicionando vida ao dragão
vida_dragao = 600  # Vida inicial do dragão

# Loop principal
rodando = True
frame_atual = 0
tempo_por_frame = 0.1  # Segundos por frame
tempo_ultimo_frame = time.time()

while rodando:
    tempo_atual = time.time()
    relogio.tick(FPS)  # 60 FPS

    for evento in pygame.event.get():
        if evento.type == QUIT:
            rodando = False

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
            dx = -velocidade_jogador
            nova_direcao = "esquerda"
        elif teclas[K_RIGHT]:
            dx = velocidade_jogador
            nova_direcao = "direita"
        elif teclas[K_UP]:
            dy = -velocidade_jogador
            nova_direcao = "cima"
        elif teclas[K_DOWN]:
            dy = velocidade_jogador
            nova_direcao = "baixo"

    if nova_direcao:
        direcao = nova_direcao
        if tempo_atual - tempo_ultimo_frame >= tempo_por_frame:
            frame_atual = (frame_atual + 1) % len(animacao_normal[direcao])

    jogador.x += dx
    jogador.y += dy

    # Seleciona a animação correta
    if atacando:
        if frame_atual < len(animacao_ataque[direcao]):
            sprite_atual = animacao_ataque[direcao][frame_atual]
            if tempo_atual - ultimo_ataque >= tempo_por_frame:
                frame_atual += 1
        else:
            atacando = False  # Fim do ataque
            frame_atual = 0  # Reinicia a animação para o próximo movimento
    else:
        # Definir a direção para uma direção padrão (por exemplo, 'baixo') caso não haja movimentação
        if nova_direcao:
            direcao = nova_direcao
        

    # Atualiza a animação do jogador
    if not atacando:  # Usa animação normal quando não está atacando
        sprite_atual = animacao_normal[direcao][frame_atual]

    # Limites da tela
    jogador.x = max(0, min(jogador.x, largura - 80))
    jogador.y = max(0, min(jogador.y, altura - 120))

    # Desenha o fundo e o jogador
    tela.blit(imagem_rua, (0, -12))
    tela.blit(sprite_atual, (jogador.x, jogador.y))

    # Movimentação do dragão
    if temporizador_acordar < 180:  # Dragão desperta após 3 segundos
        temporizador_acordar += 1
    elif imagem_dragao == imagem_dragao_dormindo:
        imagem_dragao = imagem_dragao_acordado  # Mudar para imagem de dragão em pé

    if not dragao_parado:
        # Movimentação do dragão (apenas vertical)
        dragao.y += velocidade_dragao * direcao_dragao
        if dragao.top <= 100 or dragao.bottom >= 550:
            direcao_dragao *= -1

        # Disparar uma única bola de fogo
        temporizador_bola_fogo += 1
        if temporizador_bola_fogo >= COOLDOWN_BOLA_FOGO and bola_fogo is None:
            bola_fogo = pygame.Rect(dragao.centerx, dragao.centery, 40, 20)
            temporizador_bola_fogo = 0
            imagem_dragao = imagem_dragao_ataque  # Mudar para imagem de ataque
            temporizador_ataque_dragao = 0  # Reiniciar o temporizador de ataque
            dragao_parado = True
    else:
        # Contador para pausa após ataque
        if imagem_dragao == imagem_dragao_ataque:
            temporizador_ataque_dragao += 1
            if temporizador_ataque_dragao >= 60:  # 1 segundo para voltar à imagem de voo
                imagem_dragao = imagem_dragao_acordado

        temporizador_parada_dragao += 1
        if temporizador_parada_dragao >= DURAÇÃO_PARADA:
            dragao_parado = False
            temporizador_parada_dragao = 0

    # Movimentação da bola de fogo
    if bola_fogo:
        bola_fogo.x -= velocidade_bola_fogo
        if bola_fogo.right < 0:
            bola_fogo = None

    # Verificar colisão entre o jogador e a bola de fogo
    if bola_fogo and jogador.colliderect(bola_fogo):
        if defesa_jogador > 0:
            defesa_jogador -= 50
            bola_fogo = None
        else:
            vida_jogador -= 50  # Diminui vida do jogador
            bola_fogo = None  # Destrói a bola de fogo

    # Verificar colisão entre o ataque do jogador e o dragão
    if atacando and jogador.colliderect(dragao):
        vida_dragao -= 20  # Dano causado ao dragão
        atacando = False  # Desativa o ataque após o golpe
        

    # Desenha o dragão e a bola de fogo
    lava1 = pygame.draw.rect(tela, vermelho, (0, 0, 800, 150))
    lava2 = pygame.draw.rect(tela, vermelho, (0, 530, 800, 150))
    # Verificar colisão entre o jogador e a lava
    if jogador.colliderect(lava1) or jogador.colliderect(lava2):
        vida_jogador -= 1

    tela.blit(imagem_rua, (0, -12))

    tela.blit(sprite_atual, (jogador.x, jogador.y))

    pygame.draw.rect(tela, vermelho, (25, 13, vida_jogador, 30))  # Barra de vida
    pygame.draw.rect(tela, amarelo, (30, 65, defesa_jogador, 30))  # Barra de defesa
    tela.blit(imagem_coracao, (-18, -18))
    tela.blit(imagem_escudo, (-18, 35))

    # Renderiza textos
    tela.blit(fonte.render(f'      {vida_jogador}', False, branco), (30, 10))
    tela.blit(fonte.render(f'      {defesa_jogador}', False, branco), (30, 60))
    tela.blit(fonte.render(f'Nível: {nivel_jogador}', False, branco), (30, 120))
    tela.blit(fonte.render(f'XP: {xp_jogador}', False, roxo), (30, 160))

    # Barra de vida do dragão
    pygame.draw.rect(tela, vermelho, (largura - 700, 600, vida_dragao, 30))  # Barra de vida do dragão
    tela.blit(fonte.render(f'      {vida_dragao}', False, branco), (largura - 480, 600))  # Texto da vida do dragão

    tela.blit(imagem_dragao, (dragao.x, dragao.y))
    if bola_fogo:
        tela.blit(imagem_bola_fogo, (bola_fogo.x, bola_fogo.y))

    # Atualiza a tela
    
    pygame.display.flip()

pygame.quit()
