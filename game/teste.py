import pygame
import sys

# Inicializando o Pygame
pygame.init()

# Definindo as dimensões da janela
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Movimento do Fundo")

# Carregar imagens
fundo = pygame.image.load("chão.png")  # Imagem de fundo
largura_fundo = fundo.get_width()  # Largura da imagem de fundo
altura_fundo = fundo.get_height()  # Altura da imagem de fundo

# Carregar personagem
personagem = pygame.image.load("car 2.png")  # Imagem do personagem
retangulo_personagem = personagem.get_rect()
retangulo_personagem.topleft = (100, 300)  # Posição inicial do personagem

# Velocidade do personagem
velocidade_personagem = 5

# Definir a posição do fundo
posicao_fundo_x = 0

# Loop principal do jogo
relogio = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimentação do personagem
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:  # Movendo para a esquerda
        retangulo_personagem.x -= velocidade_personagem
    if teclas[pygame.K_RIGHT]:  # Movendo para a direita
        retangulo_personagem.x += velocidade_personagem
    if teclas[pygame.K_UP]:  # Movendo para cima
        retangulo_personagem.y -= velocidade_personagem
    if teclas[pygame.K_DOWN]:  # Movendo para baixo
        retangulo_personagem.y += velocidade_personagem

    # Movimentar o fundo conforme o personagem
    posicao_fundo_x = -retangulo_personagem.x // 2  # Mover o fundo metade da velocidade do personagem

    # Desenhar a tela
    tela.fill((0, 0, 0))  # Limpar a tela com a cor preta
    tela.blit(fundo, (posicao_fundo_x, 0))  # Desenhar o fundo movendo-se com o personagem
    tela.blit(personagem, retangulo_personagem)  # Desenhar o personagem

    pygame.display.flip()  # Atualizar a tela
    relogio.tick(60)  # Definir FPS (frames por segundo)

