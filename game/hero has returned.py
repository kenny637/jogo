import pygame
import sys
import math

# Inicializa o Pygame
pygame.init()

# Configurações da janela
largura, altura = 800, 800
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Animação com 7 Imagens Redimensionadas")

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

# Posições iniciais
x, y = 60, 40  # Ajuste conforme necessário
pj_x = largura/2
pj_y = altura/1.8
# Controle da animação
indice_quadro = 0  # Índice do quadro atual
relógio = pygame.time.Clock()
fps = 10  # FPS (quantos quadros por segundo)
velocidade = 3
inimigos = [
    {'x': 100, 'y': 100, 'velocidade': 3},  # Inimigo 1
    {'x': 500, 'y': 100, 'velocidade': 2},  # Inimigo 2
]

fundo = pygame.image.load("chão.png")  # Imagem de fundo
largura_fundo = fundo.get_width()  # Largura da imagem de fundo
altura_fundo = fundo.get_height()

fundo2 = pygame.transform.scale(frame_1, (nova_largura, nova_altura))

# Botões do menu
retangulo_iniciar = pygame.draw.rect(tela, (0, 0, 0), (320, 320, 170, 60))
retangulo_sair = pygame.draw.rect(tela, (0, 0, 0), (320, 400, 170, 60))

# Botão de restart
retangulo_restart = pygame.draw.rect(tela, (0, 255, 0), (180, 300, 150, 60))

# Variáveis de controle
estado_tela = 'menu_principal'  # Tela atual, pode ser 'menu_principal', 'tela_jogo' ou 'game_over'
vida_jogador = 200  # Vida inicial do jogador

# Função para desenhar a tela inicial (menu)
def desenhar_menu_principal():
    tela.fill((255, 255, 255))  # Fundo branco
    pygame.display.flip()       


# Função para desenhar a tela de jogo (pode ser qualquer outra tela)
def desenhar_tela_jogo():
    tela.fill((0, 0, 255))  # Fundo azul para a tela de jogo
    tela.blit(fundo, (0, 0))

    jogador = pygame.draw.rect(tela, (0, 255, 0), (pj_x, pj_y, 50, 50))  # Jogador

    # Desenhar os inimigos
    for inimigo in inimigos:
        pygame.draw.rect(tela, (255, 0, 0), (inimigo['x'], inimigo['y'], 50, 50))  # Inimigos

    # Exibir vida do jogador
    font = pygame.font.SysFont('Arial', 30)
    texto_vida = font.render(f'Vida: {vida_jogador}', True, (255, 255, 255))
    tela.blit(texto_vida, (10, 10))  # Exibir no canto superior esquerdo

    pygame.display.flip()

# Função para desenhar a tela de Game Over
def desenhar_game_over():
    tela.fill((0, 0, 0))  # Fundo preto
    
    fonte_game_over = pygame.font.SysFont('Arial', 50)
    texto_game_over = fonte_game_over.render("GAME OVER", True, (255, 0, 0))
    tela.blit(texto_game_over, (180, 200))

    fonte_restart = pygame.font.SysFont('Arial', 30)
    texto_restart = fonte_restart.render("Clique para Reiniciar", True, (255, 255, 255))
    tela.blit(texto_restart, (185, 300))

    pygame.display.flip()

# Função para mover os inimigos em direção ao jogador
def mover_inimigo(inimigo, x_jogador, y_jogador):
    # Calcular a direção
    dx = x_jogador - inimigo['x']
    dy = y_jogador - inimigo['y']
    
    # Calcular a distância entre o inimigo e o jogador
    distancia = math.sqrt(dx**2 + dy**2)

    if distancia != 0:  # Evita divisão por zero
        # Normalizar a direção
        dx /= distancia
        dy /= distancia

        # Mover o inimigo na direção do jogador
        inimigo['x'] += dx * inimigo['velocidade']
        inimigo['y'] += dy * inimigo['velocidade']

# Função para verificar colisão entre o jogador e os inimigos
def verificar_colisao(pj_rect, inimigos):
    for inimigo in inimigos:
        inimigo_rect = pygame.Rect(inimigo['x'], inimigo['y'], 50, 50)  # Criando o retângulo do inimigo
        if pj_rect.colliderect(inimigo_rect):  # Verifica se o retângulo do jogador colide com o retângulo do inimigo
            return True  # Colisão detectada
    return False  # Nenhuma colisão

# Loop principal do jogo
rodando = True
while rodando:
    # Verifica os eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        # Verifica se o botão do mouse foi pressionado
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if estado_tela == 'menu_principal':
                # Verifica se o clique foi dentro da área do retângulo 'iniciar'
                if retangulo_iniciar.collidepoint(evento.pos):
                    estado_tela = 'tela_jogo'
                    fps = 120
                # Verifica se o clique foi dentro da área do retângulo 'sair'
                if retangulo_sair.collidepoint(evento.pos):
                    rodando = False
            elif estado_tela == 'game_over':
                # Verifica se o clique foi dentro do retângulo de restart
                if retangulo_restart.collidepoint(evento.pos):
                    vida_jogador = 200
                    pj_x, pj_y = 200, 300
                    inimigos = [
                        {'x': 100, 'y': 100, 'velocidade': 3},
                        {'x': 500, 'y': 100, 'velocidade': 2},
                    ]
                    estado_tela = 'tela_jogo'

    # Controle do jogador (movimento com as setas)
    if estado_tela == 'tela_jogo':
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP]:  # Cima
            pj_y -= velocidade
        if teclas[pygame.K_DOWN]:  # Baixo
            pj_y += velocidade
        if teclas[pygame.K_LEFT]:  # Esquerda
            pj_x -= velocidade
        if teclas[pygame.K_RIGHT]:  # Direita
            pj_x += velocidade

        # Criando o retângulo do jogador
    pj_rect = pygame.Rect(pj_x, pj_y, 50, 50)

        # Mover os inimigos em direção ao jogador
    for inimigo in inimigos:
        mover_inimigo(inimigo, pj_x, pj_y-40)

    posicao_fundo_x = -pj_x // 2  # Mover o fundo metade da velocidade do personagem

        # Desenhar a tela
    tela.fill((0, 0, 0))  # Limpar a tela com a cor preta
    #tela.blit(imagem_aumentada, (cont, x_1 + 500))    # Desenhar o fundo movendo-se com o personagem
        # Verificar colisão
    if verificar_colisao(pj_rect, inimigos):
        vida_jogador -= 0.5  # Subtrai 1 da vida do jogador
            
        if vida_jogador <= 0:
            estado_tela = 'game_over'  # Muda para a tela de Game Over

    # Desenha a tela de acordo com o estado atual
    if estado_tela == 'menu_principal':
        desenhar_menu_principal()  # Desenha a tela principal
        # Desenha a animação enquanto está no menu
        tela.blit(quadros[indice_quadro], (x, y))
        indice_quadro = (indice_quadro + 1) % len(quadros)  # Atualiza o índice da animação
    
    elif estado_tela == 'tela_jogo':
        desenhar_tela_jogo()  # Desenha a tela do jogo
    
    elif estado_tela == 'game_over':
        desenhar_game_over()  # Exibe a tela de Game Over

    # Atualiza a tela
    pygame.display.flip()

    # Controla a taxa de atualização (FPS)
    relógio.tick(fps)

# Encerra o Pygame
pygame.quit()
sys.exit()
