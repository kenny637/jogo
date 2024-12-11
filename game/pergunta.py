import pygame
import sys
import random

# Inicializa o pygame
pygame.init()

# Configurações da tela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo de Perguntas")

# Cores
# Carregar a imagem de fundo
imagem_fundo = pygame.image.load("pergunta.jpg")
# Redimensionar a imagem para cobrir toda a tela
imagem_fundo = pygame.transform.scale(imagem_fundo, (LARGURA, ALTURA))


# Perguntas e respostas
PERGUNTAS_NIVEL_1 = [
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    # (adicione outras perguntas iniciais)
]

PERGUNTAS_NIVEL_2 = [
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    # (adicione outras perguntas adicionais)
]

PERGUNTAS_NIVEL_3 = [
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    {"pergunta": "Quanto é 5 + 3?", "respostas": ["8", "7", "9", "10"]},
    # (adicione outras perguntas para o terceiro nível)
]

# Contador de respostas corretas
respostas_corretas = 0

# Função para desenhar texto
def desenhar_texto(texto, cor, x, y, tamanho=36):
    fonte = pygame.font.Font(None, tamanho)
    superficie_texto = fonte.render(texto, True, cor)
    rect_texto = superficie_texto.get_rect(center=(x, y))
    tela.blit(superficie_texto, rect_texto)

# Função genérica para criar telas de perguntas
def criar_tela_com_pergunta(perguntas, numero, total_perguntas):
    def tela_pergunta():
        global respostas_corretas

        pergunta = perguntas[numero - 1]
        respostas = pergunta["respostas"][:]
        resposta_correta = respostas[0]

        # Embaralha as respostas
        random.shuffle(respostas)

        rodando = True
        selecionada = 0  # Índice da resposta selecionada

        while rodando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_UP:  # Sobe na lista de opções
                        selecionada = (selecionada - 1) % len(respostas)
                    if evento.key == pygame.K_DOWN:  # Desce na lista de opções
                        selecionada = (selecionada + 1) % len(respostas)
                    if evento.key == pygame.K_RETURN:  # Confirma a resposta
                        if respostas[selecionada] == resposta_correta:
                            respostas_corretas += 1
                        else:
                            # Exibe a resposta correta antes de avançar
                            tela.blit(imagem_fundo, (0, 0))
                            desenhar_texto("Resposta incorreta!", (255, 0, 0), LARGURA // 2, ALTURA - 100, tamanho=36)
                            desenhar_texto(f"Resposta correta: {resposta_correta}", (0, 255, 0), LARGURA // 2, ALTURA - 50, tamanho=36)
                            pygame.display.flip()
                            pygame.time.wait(2000)  # Aguarda 2 segundos
                        return numero  # Retorna o mesmo número de pergunta para continuar corretamente

            # Desenha o fundo e a pergunta
            tela.blit(imagem_fundo, (0, 0))  # Troca o fundo pela imagem única
            desenhar_texto(f"Pergunta {numero} de {total_perguntas}", (255, 255, 255), LARGURA // 2, 100, tamanho=48)
            desenhar_texto(f"Respostas corretas: {respostas_corretas}", (255, 255, 255), LARGURA // 2, 150, tamanho=28)
            desenhar_texto(pergunta["pergunta"], (255, 255, 255), LARGURA // 2, 200)


            # Desenha as respostas
            for i, resposta in enumerate(respostas):
                cor = (255, 255, 0) if i == selecionada else (255, 255, 255)
                desenhar_texto(resposta, cor, LARGURA // 2, 290 + i * 68)

            pygame.display.flip()
    return tela_pergunta

# Função para verificar se o jogador ganhou
def verificar_vitoria(nivel):
    global respostas_corretas  # Garantir que estamos usando a variável global

    tela.fill((0, 0, 0))  # Limpar a tela

    if nivel == 3 and respostas_corretas >= 17:  # Condição para vencer no Nível 3
        desenhar_texto("Você ganhou o jogo! Parabéns!", (0, 255, 0), LARGURA // 2, ALTURA // 2 - 50, tamanho=36)
        desenhar_texto("Deseja reiniciar? (S para sim / N para não)", (255, 255, 255), LARGURA // 2, ALTURA // 2 + 50, tamanho=28)
        pygame.display.flip()
        return perguntar_reinicio()

    elif nivel == 2 and respostas_corretas >= 12:  # Avança para o nível 3
        desenhar_texto("Você avançou para o Nível 3!", (0, 255, 0), LARGURA // 2, ALTURA // 2, tamanho=36)
        pygame.display.flip()
        pygame.time.wait(3000)  # Mostra a mensagem por 3 segundos
        respostas_corretas = 0
        return "nivel_3"  # Avança para o nível 3

    elif nivel == 1 and respostas_corretas >= 7:  # Avança para o nível 2
        desenhar_texto("Você avançou para o Nível 2!", (0, 255, 0), LARGURA // 2, ALTURA // 2, tamanho=36)
        pygame.display.flip()
        pygame.time.wait(3000)  # Mostra a mensagem por 3 segundos
        respostas_corretas = 0
        return "nivel_2"  # Avança para o nível 2

    else:  # Fim do jogo se não atingir o mínimo necessário
        desenhar_texto("Fim de jogo! Você não atingiu o mínimo necessário.", (255, 0, 0), LARGURA // 2, ALTURA // 2 - 50, tamanho=36)
        desenhar_texto("Deseja reiniciar? (S para sim / N para não)", (255, 255, 255), LARGURA // 2, ALTURA // 2 + 50, tamanho=28)
        pygame.display.flip()
        return perguntar_reinicio()

def perguntar_reinicio():
    esperando_resposta = True
    while esperando_resposta:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_s:  # Jogador deseja reiniciar
                    return "reiniciar"
                elif evento.key == pygame.K_n:  # Jogador deseja encerrar
                    return "fim"


# Função para reiniciar o jogo
def reiniciar_jogo():
    global respostas_corretas
    respostas_corretas = 0
    return "telas_iniciais"

# Criação de telas
PERGUNTAS_1 = [criar_tela_com_pergunta(PERGUNTAS_NIVEL_1, i + 1, len(PERGUNTAS_NIVEL_1)) for i in range(len(PERGUNTAS_NIVEL_1))]
PERGUNTAS_2 = [criar_tela_com_pergunta(PERGUNTAS_NIVEL_2, i + 1, len(PERGUNTAS_NIVEL_2)) for i in range(len(PERGUNTAS_NIVEL_2))]
PERGUNTAS_3 = [criar_tela_com_pergunta(PERGUNTAS_NIVEL_3, i + 1, len(PERGUNTAS_NIVEL_3)) for i in range(len(PERGUNTAS_NIVEL_3))]

# Loop principal
estado_atual = "telas_iniciais"
nivel_atual = 1  # Nível inicial
indice_pergunta = 0
while True:
    if estado_atual == "telas_iniciais":
        if indice_pergunta < len(PERGUNTAS_1):
            indice_pergunta = PERGUNTAS_1[indice_pergunta]()
        else:
            estado_atual = verificar_vitoria(nivel_atual)
            indice_pergunta = 0
    elif estado_atual == "nivel_2":
        if indice_pergunta < len(PERGUNTAS_2):
            indice_pergunta = PERGUNTAS_2[indice_pergunta]()
            nivel_atual = 2
        else:
            estado_atual = verificar_vitoria(nivel_atual)
            indice_pergunta = 0
    elif estado_atual == "nivel_3":
        nivel_atual = 3
        if indice_pergunta < len(PERGUNTAS_3):
            indice_pergunta = PERGUNTAS_3[indice_pergunta]()
        else:
            estado_atual = verificar_vitoria(nivel_atual)
            indice_pergunta = 0
    elif estado_atual == "reiniciar":
        estado_atual = reiniciar_jogo()  # Reinicia o jogo
        indice_pergunta = 0
        nivel_atual = 1  # Reinicia no nível 1
    elif estado_atual == "fim":
        pygame.quit()
        sys.exit()
